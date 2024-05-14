"""API views."""
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema,OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .roles import ClientRole
from rolepermissions.roles import assign_role
# Create your views here.

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

class UserView(APIView):
    """Create User View"""
    @extend_schema(
        responses={200: OpenApiTypes.OBJECT},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            assign_role(user, ClientRole)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
