"""Views for events"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema_view, extend_schema
from api.permissions import AdminPermission
from config.utils import save_image
from .models import Event
from .serializers import EventSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['events'],
        summary='Get all events',
        description='Get all events'
    ),
    create=extend_schema(
        tags=['events'],
        summary='Create an event',
        description='Create an event'
    ),
    retrieve=extend_schema(
        tags=['events'],
        summary='Get an event',
        description='Get an event'
    ),
    update=extend_schema(
        tags=['events'],
        summary='Update an event',
        description='Update an event'
    ),
    destroy=extend_schema(
        tags=['events'],
        summary='Delete an event',
        description='Delete an event'
    ),
    get_trash_events=extend_schema(
        tags=['events'],
        summary='Get all trashed events',
        description='Get all trashed events'
    ),
    get_trash_event=extend_schema(
        tags=['events'],
        summary='Get a trashed event',
        description='Get a trashed event'
    ),
    restore_event=extend_schema(
        tags=['events'],
        summary='Restore a trashed event',
        description='Restore a trashed event'
    )
)
class EventViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """Viewset for events"""
    queryset = Event.logic.all()
    serializer_class = EventSerializer

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

            image_response = save_image(
                image.read(),
                image.content_type
            )
            response = image_response.get('data')
            if 'error' not in response:

                data['image'] = response.get('url')
            else:
                return Response(
                    {
                        'error': response.get('error')
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        data = request.data

        if 'image' in data:
            image = data['image']

            image_response = save_image(
                image.read(),
                image.content_type
            )
            response = image_response.get('data')
            if 'error' not in response:
                data['image'] = response.get('url')
            else:
                return Response(
                    {
                        'error': response.get('error')
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=['GET'], url_path='trash/all', url_name='trash')
    def get_trash_events(self, request):# pylint: disable=unused-argument
        """Get all trashed events"""
        events = Event.objects.filter(deleted_at__isnull=False).all()
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=True,methods=['GET'],url_path='trash',url_name='trash')
    def get_trash_event(self,request,pk=None):# pylint: disable=unused-argument
        """Get a trashed event"""
        event = Event.objects.filter(deleted_at__isnull=False).get(pk=pk)
        serializer = self.get_serializer(event)
        return Response(serializer.data)

    @action(detail=True,methods=['PATCH'],url_path='restore',url_name='restore')
    def restore_event(self,request,pk=None): # pylint: disable=unused-argument
        """Restore a trashed event"""
        event = Event.objects.filter(deleted_at__isnull=False).get(pk=pk)
        event.deleted_at = None
        event.save()
        serializer = self.get_serializer(event)
        return Response(serializer.data)
