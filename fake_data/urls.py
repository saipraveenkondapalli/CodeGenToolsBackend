from django.urls import path

from .views import FakeDataView, FakeDataFieldsApiView

urlpatterns = [
    path('data/', FakeDataView.as_view()),
    path('fields/', FakeDataFieldsApiView.as_view()),
]
