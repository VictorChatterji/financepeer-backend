from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from io import StringIO
import json
from upload.models import Jdata
from upload.serializers import JdataSerializer
from django.db.models import Count

# Create your views here.


class UploadDataView(APIView):
    def post(self, request):
        result = {}
        result['message'] = 'Unauthorized Access !'
        if request.user.is_authenticated:
            ext = str(request.FILES['json_file']).split('.')[1]
            if ext != 'json':
                result['message'] = 'Please upload JSON file'
                return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            try:
                data = StringIO(request.FILES['json_file'].read().decode('utf-8-sig'))
                reader = json.load(data)
                serializer = JdataSerializer(data=reader, many=True)
                if serializer.is_valid() == False:
                    result['message'] = 'Please upload valid JSON file'
                    return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            except:
                result['message'] = 'Invalid JSON'
                return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                for row in reader:
                    Jdata.objects.create(
                        userId = row['userId'],
                        title = row['title'],
                        body = row['body']
                    )
            result['message'] = 'Data Uploaded to database !'
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_403_FORBIDDEN)

class DataCount(APIView):
    def get(self, request):
        result = {}
        result['message'] = 'Unauthorized Access !'
        if request.user.is_authenticated:
            data = Jdata.objects.values('userId').annotate(count=Count('userId'))
            result['data'] = data
            result['message'] = 'Data fetched !'
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_403_FORBIDDEN)


class ParticularData(APIView):
    def post(self, request):
        result = {}
        result['message'] = 'Unauthorized Access !'
        if request.user.is_authenticated:
            userid = request.data['id']
            data = Jdata.objects.filter(userId=userid).values()
            result['data'] = data
            result['message'] = 'Data fetched !'
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_403_FORBIDDEN)
