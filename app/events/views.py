from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_spectacular.utils import extend_schema,OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .serializers import EventSerializer
from .models import Event
from config.utils import save_image
# Create your views here.

class EventAPIView(APIView):
    @extend_schema(
        tags=['Event'],
        responses={200: OpenApiTypes.OBJECT},
    )
    def get(self, request: Request):
        events = Event.logic.all()
        events_response = EventSerializer(events, many=True)
        return Response({'data': events_response.data})

    @extend_schema(
        tags=['Event'],
        request=EventSerializer,
        responses={201: OpenApiTypes.OBJECT},
    )
    def post(self, request: Request):
        data = request.data

        print(data)
        serializer = EventSerializer(data=data)

        if 'image' in data:
            image: InMemoryUploadedFile = data['image']

            image_response = save_image(
                image.read(),
                image.content_type
            )
            response = image_response.get('data')
            if 'error' not in response:

                data['image'] = response.get('url')
            else:
                return Response(response,status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():

            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class EventOneAPIView(APIView):
    @extend_schema(
        tags=['Event'],
        responses={200: OpenApiTypes.OBJECT},
        parameters=[
            OpenApiParameter(
                name='event_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='Event ID',
            ),
        ]
    )
    def get(self,request,event_id=None):
        try:
            event = Event.objects.get(id=event_id)
            return Response({'data': EventSerializer(event).data})
        except ObjectDoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
            tags=['Event'],
            responses={200: OpenApiTypes.OBJECT},
            parameters=[
                OpenApiParameter(
                    name='event_id',
                    type=OpenApiTypes.INT,
                    location=OpenApiParameter.PATH,
                    description='Event ID',
                ),
            ]
    )
    def put(self,request,event_id=None):
        data = request.data
        try:
            event = Event.objects.get(id=event_id)
            serializer = EventSerializer(event, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data})

            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        tags=['Event'],
        responses={200: OpenApiTypes.OBJECT},
        parameters=[
            OpenApiParameter(
                name='event_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='Event ID',
            ),
        ]
    )
    def delete(self,request,event_id=None):
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)


class EventTrashAPIView(APIView):
    @extend_schema(
        tags=['Event', 'Trash'],
        responses={200: OpenApiTypes.OBJECT},
    )
    def get(self,request):
        events = Event.objects.filter(deleted_at__isnull=False).all()

        return Response({'data': EventSerializer(events, many=True).data})
class EventOneTrashAPIView(APIView):
    @extend_schema(
        tags=['Event', 'Trash'],
        responses={200: OpenApiTypes.OBJECT},
        parameters=[OpenApiParameter(
            name='event_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description='Event ID',
        )]
    )
    def get(self,request,event_id=None):
        try:
            event = Event.objects.filter(deleted_at__isnull=False,id=event_id).first()
            return Response({'data': EventSerializer(event).data})
        except ObjectDoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        tags=['Event', 'Trash'],
        responses={200: OpenApiTypes.OBJECT},
        parameters=[
            OpenApiParameter(
                name='event_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='Event ID',
            ),
        ]
    )
    def patch(self,request,event_id=None):

        try:
            event = Event.objects.filter(deleted_at__isnull=False,id=event_id).first()
            event.restore()
            return Response({'data': EventSerializer(event).data})
        except ObjectDoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)