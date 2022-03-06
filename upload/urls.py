from django.urls import path
from .views import *

urlpatterns = [
    path('jsonupload/', UploadDataView.as_view()),
    path('datacount/', DataCount.as_view()),
    path('particulardata/', ParticularData.as_view()),
]
