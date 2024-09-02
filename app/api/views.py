"""API views."""
from django.contrib.auth.models import User

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets ,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

# drf_spectacular package
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

# role package
from rolepermissions.roles import assign_role, get_user_roles
# from rolepermissions.roles import RolesClassRegister
# api package
from api.roles import ClientRole
from api.models import Profile
from api.serializers import (
    ProfileSerializers,
    UserSerializer,
    # UserTokenReponseSerializer
)

class ExampleView(APIView):
    """Example View"""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='example',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Example query parameter',
            ),
        ],
        responses={200: OpenApiTypes.OBJECT},
    )
    def get(self, request):
        """GET request."""
        return Response(
            {'message': 'Hello, World!', 'example': request.query_params.get('example')}
        )


class ProfileViewset(viewsets.ModelViewSet):
    """Profile Viewset"""
    queryset = Profile.objects.all() # pylint: disable=no-member
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializers


class UserView(APIView):
    """Create User View"""
    @extend_schema(
        responses={200: OpenApiTypes.OBJECT},
    )
    def post(self, request):
        """Create a new user."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            assign_role(user, ClientRole)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom token view."""

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)


        if response.status_code == 200:
            user = User.objects.get(email=request.data['username'])
            roles = get_user_roles(user)

            roles = [role.get_name() for role in roles]

            return Response({'user': {
                'roles':roles,
                'email': user.email,
                'username': user.username,
                'id': user.id
            }, **response.data})

        return response
