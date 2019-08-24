from django.test import TestCase
from .models import TutorProfile
from datetime import datetime

# Tutor Profile Test
class TestTutorProfile(TestCase):
    def setUp(self):
        self.Bob = TutorProfile(first_name='Bob', last_name='Axe', email='ba@etutor.com',
                                specialization='trading 101', created_on=datetime.now() )

    def test_instance(self): # Test if is instance of Tutor Profile
        self.assertTrue(isinstance(self.Bob, TutorProfile))

    def tearDown(self):
        TutorProfile.objects.all().delete()

