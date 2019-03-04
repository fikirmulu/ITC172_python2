
from django.test import TestCase
from .models import Resource, Meeting, Event
from django.urls import reverse

# Create your tests here.
# model tests

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='computer')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='salary increment')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class EnentTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='New years')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')
