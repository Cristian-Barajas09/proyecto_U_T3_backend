"""Inventory API views"""
from rest_framework import viewsets ,permissions,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from config.utils import save_image
from api.permissions import AdminPermission
from api.pagination import CustomPagination
from inventory.models import Plates,Category
from inventory.serializers import PlatesSerializers,CategorySerializers



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
