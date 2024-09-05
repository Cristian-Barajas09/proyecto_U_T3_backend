"""Inventory API views"""
from rest_framework import viewsets ,permissions,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema
from config.utils import save_image
from api.permissions import AdminPermission
from api.pagination import CustomPagination
from inventory.models import Plates,Category
from inventory.serializers import PlatesSerializers,CategorySerializers

@extend_schema_view(
    list=extend_schema(
        tags=['inventory'],
        summary='Get all plates',
        description='Get all plates'
    ),
    create=extend_schema(
        tags=['inventory'],
        summary='Create a plate',
        description='Create a plate'
    ),
    retrieve=extend_schema(
        tags=['inventory'],
        summary='Get a plate',
        description='Get a plate'
    ),
    update=extend_schema(
        tags=['inventory'],
        summary='Update a plate',
        description='Update a plate'
    ),
    destroy=extend_schema(
        tags=['inventory'],
        summary='Delete a plate',
        description='Delete a plate'
    ),
)

class PlatesViewset(viewsets.ModelViewSet):
    """Get all plates and create a plate"""
    queryset = Plates.objects.filter( # pylint: disable=no-member
        deleted_at__isnull=True
    ).order_by('created_at').all()

    permission_classes = [permissions.AllowAny]
    serializer_class = PlatesSerializers
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated,AdminPermission]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):

        data = request.data

        if 'image' in data:
            image = data['image']
            try:
                image_response = save_image(
                    image.read(),
                    image.content_type
                )

                response = image_response.get('data')

                data['image'] = response.get('name')
            except ValueError as error:
                return Response(
                    {
                        'error': str(error)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )


        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        data = request.data

        if 'image' in data:
            image = data['image']
            try:
                image_response = save_image(
                    image.read(),
                    image.content_type
                )

                response = image_response.get('data')

                data['image'] = response.get('name')
            except ValueError as error:
                return Response(
                    {
                        'error': str(error)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        return super().update(request, *args, **kwargs)


@extend_schema_view(
    list=extend_schema(
        tags=['inventory'],
        summary='Get all categories',
        description='Get all categories'
    ),
    create=extend_schema(
        tags=['inventory'],
        summary='Create a category',
        description='Create a category'
    ),
    retrieve=extend_schema(
        tags=['inventory'],
        summary='Get a category',
        description='Get a category'
    ),
    update=extend_schema(
        tags=['inventory'],
        summary='Update a category',
        description='Update a category'
    ),
    destroy=extend_schema(
        tags=['inventory'],
        summary='Delete a category',
        description='Delete a category'
    ),

    get_plates_by_category=extend_schema(
        tags=['inventory'],
        summary='Get all plates by category',
        description='Get all plates by category'
    )
)
class CategoryViewset(viewsets.ModelViewSet):
    """Get all categories and create a category"""
    queryset = Category.objects.filter(# pylint: disable=no-member
        deleted_at__isnull=True
    ).all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializers

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated,AdminPermission]
        return super().get_permissions()

    @action(detail=True, methods=['get'], url_path='plates', url_name='plates')
    def get_plates_by_category(self, request, pk=None): # pylint: disable=unused-argument
        """Get all plates by category"""
        category = Category.objects.get(pk=pk)

        plates = Plates.objects.filter( # pylint: disable=no-member
            categories=category,
            deleted_at__isnull=True
        ).all()


        serializer = PlatesSerializers(plates, many=True)

        return Response(serializer.data)
