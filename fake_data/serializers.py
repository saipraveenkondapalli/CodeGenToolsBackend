from rest_framework import serializers

from .utils import fake_data_generator


class FakeDataSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        valid_values = fake_data_generator.all_fields()
        # no need to validate "count" field

        for value in data.values():
            if not fake_data_generator.binary_search(value, valid_values):
                raise serializers.ValidationError({"error": f"Invalid value {value}"})

        return data
