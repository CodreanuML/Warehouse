from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.core import mail
from UsersManager import views


class UsersManagerViewsAndURLsTest(TestCase):
    """
    Teste combinate pentru:
    - mapping-ul URL -> View corect
    - funcționalitatea view-urilor
    """

    def setUp(self):
        # Creăm un utilizator pentru testare
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )

    # ====================
    # TESTE URL -> VIEW
    # ====================
    def test_register_url_and_view(self):
        url = reverse('UsersManager:register')
        self.assertEqual(resolve(url).func.view_class, views.RegisterView)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UsersManager/register.html')

    def test_login_url_and_view(self):
        url = reverse('UsersManager:login')
        self.assertEqual(resolve(url).func.view_class, views.Login)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UsersManager/login.html')

    def test_prelogout_url_and_view(self):
        url = reverse('UsersManager:prelogout')
        self.assertEqual(resolve(url).func.view_class, views.PreLogOut)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UsersManager/logout.html')

    def test_logout_url_and_view(self):
        url = reverse('UsersManager:logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_password_reset_url_and_view(self):
        url = reverse('UsersManager:password_reset')
        self.assertEqual(resolve(url).func.view_class, views.MyPasswordResetView)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UsersManager/password_reset.html')

    def test_password_reset_done_url_and_view(self):
        url = reverse('UsersManager:password_reset_done')
        self.assertEqual(resolve(url).func.view_class, views.MyPasswordResetDoneView)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UsersManager/password_reset_done.html')

    def test_password_reset_confirm_url_and_view(self):
        url = reverse('UsersManager:password_reset_confirm', args=['uidb64', 'token'])
        self.assertEqual(resolve(url).func.view_class, views.MyPasswordResetConfirmView)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_url_and_view(self):
        url = reverse('UsersManager:password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, views.MyPasswordResetCompleteView)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UsersManager/password_reset_complete.html')

    # ====================
    # TESTE FUNCȚIONALE
    # ====================

    """
    def test_register_view_post_valid(self):
        """
        Testăm trimiterea formularului de înregistrare cu date valide
        """

        url=reverse("UsersManager:register")
        print("POST to URL:",url)
        data = self.client.post(reverse('UsersManager:register'), {
            'username': 'newuser',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'email': 'new@example.com',
            'role': 'logistic_user_lvl1',
            'id_number': 1234 ,
        	'first_name': 'John',
        	'last_name': 'Doe'
        })
        response = self.client.post(reverse('UsersManager:register'), data)
        print(response.context['form'].errors)
        self.assertEqual(response.status_code, 302)  # redirect la success_url
        self.assertTrue(User.objects.filter(username='newuser').exists())
	"""
    def test_login_view_post_valid(self):
        """
        Testăm autentificarea cu credențiale valide
        """
        response = self.client.post(reverse('UsersManager:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # redirect

    def test_password_reset_post_sends_email(self):
        """
        Testăm trimiterea email-ului de resetare a parolei
        """
        response = self.client.post(reverse('UsersManager:password_reset'), {
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)  # a fost trimis un email