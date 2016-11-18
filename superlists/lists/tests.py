from django.test import TestCase

# Create your tests here.
# run command: python3 manage.py test
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(2, 3)