from rest_framework import status
from rest_framework.response import Response
from knox.views import LoginView, LogoutView
from rest_framework import permissions
from users.models import User
from users.serializers import LoginSerializer
from django.contrib.auth import authenticate, login


# Create your views here.

class Login(LoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    def post(self,request):
        result = {}
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user_data = authenticate(
                    email = serializer.validated_data['email'],
                    password = serializer.validated_data['password']
                )
            except:
                result['message'] = 'User not present'
                return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            if user_data is not None:
                user_details = User.objects.filter(email=user_data).values('name', 'email')
                login(request, user_data)
                data = super(Login, self).post(request)
                data = data.data
                result['user_info'] = user_details
                result['data'] = data
                result['message'] = 'Loggedin Successfully!'
                return Response(result, status=status.HTTP_200_OK)
        result['message'] = 'Credentials Wrong !'
        return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class Logout(LogoutView):
    def get(self, request):
        result = {}
        result['message'] = 'Unauthorized Access !'
        if request.user.is_authenticated:
            try:
                request._auth.delete()
            except:
                result['message'] = 'Error while logging out!'
                return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            result['message'] = 'Loggedout Successfully!'
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_403_FORBIDDEN)

