import inflection
from faker import Faker

faker = Faker()


class FakeDataGenerator:
    def __init__(self) -> None:
        pass

    def validate_field_names(self, field_names) -> dict:
        field_mapping = {}
        for field in field_names:
            original_field = field.strip()
            snake_case_field = inflection.underscore(original_field).lower()
            if hasattr(faker, snake_case_field):
                field_mapping[original_field] = snake_case_field
        return field_mapping

    def check_invalid_field_names(self, field_names):
        invalid_fields = []
        for field in field_names:
            original_field = field.strip()
            snake_case_field = inflection.underscore(original_field).lower()
            if not hasattr(faker, snake_case_field):
                invalid_fields.append(original_field)
        return invalid_fields

    def generate_fake_data(self, field_names, count):
        if not field_names:
            raise ValueError("No valid field names provided")

        invalid_fields = self.check_invalid_field_names(field_names)

        if invalid_fields:
            raise ValueError(f"Invalid field names: {', '.join(invalid_fields)}")

        field_mapping = self.validate_field_names(field_names)

        data = []
        for _ in range(count):
            item = {
                original: getattr(faker, snake_case)()
                for original, snake_case in field_mapping.items()
            }
            data.append(item)

        return data

    def gen_test_data(self, fields: dict, count):
        return [
            {key: getattr(faker, value)() for key, value in fields.items()}
            for _ in range(count)
        ]

    def all_fields(self):
        return [field for field in dir(faker) if not field.startswith("_")]

    def binary_search(self, field: str, all_data: list[str]) -> bool:
        left, right = 0, len(all_data) - 1

        while left <= right:
            mid = (left + right) // 2
            if all_data[mid] == field:
                return True
            elif all_data[mid] < field:
                left = mid + 1
            else:
                right = mid - 1

        return False


fake_data_generator = FakeDataGenerator()  # singleton instance
