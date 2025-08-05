from django.urls import reverse
from django.test import TestCase, Client
from UsersManager.views import RegisterView

class RegisterViewTests(TestCase):

	def setUp(self):
		self.client = Client()

	def test_signup_status_code(self):
		response = self.client.get(reverse('UsersManager:register'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'UsersManager/register.html')


