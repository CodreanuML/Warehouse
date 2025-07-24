from django.test import TestCase, Client
from django.urls import reverse
from LogisticManager.models import TransportType, Route


class MainViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    # Testează accesarea paginii principale (GET pe /main/)
    def test_main_view_get(self):
        response = self.client.get(reverse('LogisticManager:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/main.html')


class TransportTypeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.transport = TransportType.objects.create(
            name="Original",
            category='cargo',
            capacity=1000,
            capacity_unit="kg"
        )

    # Testează accesarea paginea de listare a transport_type
    def test_transport_type_list_all(self):
        response = self.client.get(reverse('LogisticManager:transport_type_list_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/transport_type_list.html')


    # Testează accesarea paginii de creare a unui tip de transport (GET pe /transport_type/create/)
    def test_transport_type_create_get(self):
        response = self.client.get(reverse('LogisticManager:transport_type_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/transport_type_create.html')

    # Testează trimiterea unui formular valid pentru creare transport (POST pe /transport_type/create/)
    def test_transport_type_create_post(self):
        response = self.client.post(reverse('LogisticManager:transport_type_create'), {
            'name': 'TIR',
            'category': 'cargo',
            'capacity': 20000,
            'capacity_unit': 'kg',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertTrue(TransportType.objects.filter(name='TIR').exists())

    # Testează actualizarea unui transport existent (POST pe /transport_type/update/<pk>/)
    def test_transport_type_update_post(self):
        url = reverse('LogisticManager:transport_type_update', kwargs={'pk': self.transport.pk})
        response = self.client.post(url, {
            'name': 'Updated',
            'category': 'cargo',
            'capacity': 3000,
            'capacity_unit': 'kg',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.transport.refresh_from_db()
        self.assertEqual(self.transport.name, 'Updated')

    # Testează ștergerea unui transport existent (POST pe /transport_type/delete/<pk>/)
    def test_transport_type_delete_post(self):
        url = reverse('LogisticManager:transport_type_delete', kwargs={'pk': self.transport.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertFalse(TransportType.objects.filter(pk=self.transport.pk).exists())


class RouteViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.route = Route.objects.create(
            route_type='Highway',
            from_T='City A',
            to_T='City B',
            length=200
        )

    # Testează accesarea paginea de listare a routelor
    def test_routes_list_all(self):
        response = self.client.get(reverse('LogisticManager:routes_list_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/routes_list.html')


    # Testează accesarea paginii de creare rută (GET pe /routes/create/)
    def test_route_create_get(self):
        response = self.client.get(reverse('LogisticManager:routes_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/routes_create.html')

    # Testează trimiterea unui formular valid pentru creare rută (POST pe /routes/create/)
    def test_route_create_post(self):
        response = self.client.post(reverse('LogisticManager:routes_create'), {
            'route_type': 'land',
            'from_T': 'Town X',
            'to_T': 'Town Y',
            'length': 350
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertTrue(Route.objects.filter(from_T='Town X', to_T='Town Y').exists())

    # Testează actualizarea unei rute existente (POST pe /routes/update/<pk>/)
    def test_route_update_post(self):
        url = reverse('LogisticManager:routes_update', kwargs={'pk': self.route.pk})
        response = self.client.post(url, {
            'route_type': 'naval',
            'from_T': self.route.from_T,
            'to_T': self.route.to_T,
            'length': 300
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.route.refresh_from_db()
        self.assertEqual(self.route.route_type, 'naval')

    # Testează ștergerea unei rute existente (POST pe /routes/delete/<pk>/)
    def test_route_delete_post(self):
        url = reverse('LogisticManager:routes_delete', kwargs={'pk': self.route.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertFalse(Route.objects.filter(pk=self.route.pk).exists())


class SuccessFailPagesTest(TestCase):
    def setUp(self):
        self.client = Client()

    # Testează afișarea paginii de succes (GET pe /successful/)
    def test_success_page(self):
        response = self.client.get(reverse('LogisticManager:successful'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'general/successful.html')

    # Testează afișarea paginii de eroare/invalidare (GET pe /failled/)
    def test_failled_page(self):
        response = self.client.get(reverse('LogisticManager:failled'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'general/failled.html')