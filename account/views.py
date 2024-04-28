from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
 

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class GoogleRegistration(CreateAPIView):
    serializer_class = GoogleAuthSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        return super().get_serializer_class()

    def post(self, request):
        email = request.data.get('email')

        if not User.objects.filter(email=email).exists():
            serializer = GoogleAuthSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['is_google'] = True
                user = serializer.save()
        user = User.objects.filter(email=email).first()
        if user is not None:
            token = create_jwt_pair_tokens(user)
            response_data = {
                'status': 'success',
                'msg': 'Registratin Successfully',
                'token': token,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'msg': serializer.errors})


def create_jwt_pair_tokens(user):
    refresh = RefreshToken.for_user(user)
    refresh['email'] = user.email
    refresh['is_active'] = user.is_active
    refresh['is_google'] = user.is_google

    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return {
        "access": access_token,
        "refresh": refresh_token,
    }


class UserDetils(ListAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.kwargs.get('id')
        return User.objects.exclude(id=user).exclude(first_name='admin')


class AuthUser(ListAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.kwargs.get('id')
        return User.objects.filter(id=user)


# class LogoutView(APIView):
#     def post(self, request):
#         try:
#             refresh_token_value = request.data.get("refresh")
#             token = RefreshToken(refresh_token_value)
#             token.blacklist()
#             return Response(status=status.HTTP_200_OK)
#         except Exception as e:
#             print("Error occurred during logout:", e)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
