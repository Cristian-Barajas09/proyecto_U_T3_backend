"""Event Tests"""
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from api.roles import AdminRole, ClientRole
from rolepermissions.roles import assign_role
from rest_framework.test import APIClient
from .models import Event


def create_image():
    """Create an image"""
    return SimpleUploadedFile(
        name='test_image.jpg',
        content=open('events/tests/test.jpg', 'rb').read(),
        content_type='image/jpeg'
    )

# Create your tests here.
class EventDatabaseTest(TestCase):
    """Event Database Test"""
    ENDPOINT = '/api/v1/events/'

    def test_create_event(self):
        """Test creating an event"""
        date = timezone.now()
        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=date,
            image='https://example.com/image.jpg'
        )

        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.description, 'This is a test event')
        self.assertEqual(event.date, date)
        self.assertEqual(event.image, 'https://example.com/image.jpg')
        self.assertEqual(event.deleted_at, None)

    def delete_logic_event(self):
        """Test deleting an event"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        event.delete()

        self.assertEqual(Event.objects.filter(title='Test Event').count(), 0)
        self.assertEqual(Event.logic.all().count(), 0)

    def test_update_event(self):
        """Test updating an event"""


        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        event.title = 'Updated Test Event'
        event.save()

        self.assertEqual(event.title, 'Updated Test Event')
        self.assertEqual(Event.objects.get(pk=event.pk).title, 'Updated Test Event')

    def test_get_event(self):
        """Test getting an event"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        self.assertEqual(Event.logic.get(pk=event.pk).title, 'Test Event')

    def test_get_all_events(self):
        """Test getting all events"""

        Event.logic.create(
            title='Test Event 1',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        Event.logic.create(
            title='Test Event 2',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        self.assertEqual(Event.logic.all().count(), 2)

    def test_get_all_events_deleted(self):
        """Test getting all events including deleted"""

        Event.logic.create(
            title='Test Event 1',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        event = Event.logic.create(
            title='Test Event 2',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        event.delete()

        self.assertEqual(Event.objects.all().count(), 2)


class EventAPITest(TestCase):
    """Event API Test"""
    ENDPOINT = '/api/v1/events/'

    user: User

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

        assign_role(self.user, AdminRole)

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_create_event(self):
        """Test creating an event"""

        image = create_image()


        response = self.client.post(
            self.ENDPOINT,
            {
                'title': 'Test Event',
                'description': 'This is a test event',
                'date': timezone.now(),
                'image': image
            },
            format='multipart',

        )

        if isinstance(response, HttpResponseBadRequest):
            with open('events/tests/fail.html', 'w',encoding="utf-8") as f:
                f.write(response.content)

        self.assertEqual(response.status_code, 201)

    def test_get_all_events(self):
        """Test getting all events"""

        Event.logic.create(
            title='Test Event 1',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        Event.logic.create(
            title='Test Event 2',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        response = self.client.get(self.ENDPOINT)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_event(self):
        """Test getting an event"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        response = self.client.get(f'{self.ENDPOINT}{event.pk}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Event')

    def test_update_event(self):
        """Test updating an event"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        image = create_image()
        response = self.client.put(
            f'{self.ENDPOINT}{event.pk}/',
            {
                'title': 'Updated Test Event',
                'description': 'This is a test event',
                'date': timezone.now(),
                'image': image
            },
            format='multipart',
        )

        if isinstance(response, HttpResponseBadRequest):
            with open('events/tests/fail.html', 'w',encoding="utf-8") as f:
                f.write(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Test Event')

    def test_delete_event(self):
        """Test deleting an event"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        response = self.client.delete(f'{self.ENDPOINT}{event.pk}/')

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Event.logic.filter(pk=event.pk).count(), 0)

    def test_delete_event_not_found(self):
        """Test deleting an event that does not exist"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        self.client.delete(f'{self.ENDPOINT}{event.pk}/')

        response = self.client.delete(f'{self.ENDPOINT}{event.pk}/')

        self.assertEqual(response.status_code, 404)

    def test_delete_event_already_deleted(self):
        """Test deleting an event that is already deleted"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        event.delete()

        response = self.client.delete(f'{self.ENDPOINT}{event.pk}/')

        self.assertEqual(response.status_code, 404)

    def test_create_event_unauthorized(self):
        """Test creating an event without authorization"""

        client = APIClient()

        response = client.post(
            self.ENDPOINT,
            {
                'title': 'Test Event',
                'description': 'This is a test event',
                'date': timezone.now(),
                'image': create_image()
            },
            format='multipart',
        )

        self.assertEqual(response.status_code, 401)

    def test_update_event_unauthorized(self):
        """Test updating an event without authorization"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        client = APIClient()

        response = client.put(
            f'{self.ENDPOINT}{event.pk}/',
            {
                'title': 'Updated Test Event',
                'description': 'This is a test event',
                'date': timezone.now(),
                'image': create_image()
            },
            format='multipart',
        )

        self.assertEqual(response.status_code, 401)


    def test_delete_event_unauthorized(self):
        """Test deleting an event without authorization"""

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        client = APIClient()

        response = client.delete(f'{self.ENDPOINT}{event.pk}/')

        self.assertEqual(response.status_code, 401)


    def test_create_event_invalid_data(self):
        """Test creating an event with invalid data"""

        response = self.client.post(
            self.ENDPOINT,
            {
                'title': 'Test Event',
                'description': 'This is a test event',
                'date': timezone.now(),
                'image': 'invalid_image.jpg'
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)


    def test_create_event_with_role_client(self):
        """Test creating an event with a client role"""

        user_client = User.objects.create_user(
            username='testclient',
            password='password'
        )

        assign_role(user_client, ClientRole)

        client = APIClient()

        client.force_authenticate(user=user_client)

        response = client.post(
            self.ENDPOINT,
            {
                'title': 'Test Event',
                'description': 'This is a test event',
                'date': timezone.now(),
                'image': create_image()
            },
            format='multipart',
        )

        self.assertEqual(response.status_code, 403)

    def test_delete_event_with_role_client(self):
        """Test deleting an event with a client role"""

        user_client = User.objects.create_user(
            username='testclient',
            password='password'
        )

        assign_role(user_client, ClientRole)

        client = APIClient()

        client.force_authenticate(user=user_client)

        event = Event.logic.create(
            title='Test Event',
            description='This is a test event',
            date=timezone.now(),
            image='https://example.com/image.jpg'
        )

        response = client.delete(f'{self.ENDPOINT}{event.pk}/')

        self.assertEqual(response.status_code, 403)
