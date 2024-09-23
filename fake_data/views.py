from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FakeDataSerializer
from .utils import fake_data_generator


class FakeDataView(APIView):
    def post(self, request):
        data = request.data
        count = data.pop("count", 1)

        serializer = FakeDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        data: dict = fake_data_generator.gen_test_data(serializer.validated_data, count)
        return Response(data if count > 1 else data[0])


class FakeDataFieldsApiView(APIView):
    def get(self, request):
        return Response(fake_data_generator.all_fields())
