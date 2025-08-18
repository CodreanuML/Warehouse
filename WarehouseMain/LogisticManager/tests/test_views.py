from django.test import TestCase, Client
from django.urls import reverse
from LogisticManager.models import TransportType, Route , LandTransport , AirTransport , NavalTransport
from django.contrib.auth.models import User, Group
from UsersManager.models import Profile 

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


        #creeaza user pentru logistics lvl 1 
        self.user = User.objects.create_user(
            username="testuser_logistics_lvl_1",
            password="secret123"
        )    
        self.profile = Profile.objects.create(
            user=self.user,
            role="logistic_user_lvl1",
            id_number=123
        )
        group, _ = Group.objects.get_or_create(name=self.profile.role)
        self.user.groups.add(group)


        #creeaza user pentru warehouse lvl 1 
        self.user = User.objects.create_user(
            username="testuser_warehouse_lvl_1",
            password="secret123"
        )    
        self.profile = Profile.objects.create(
            user=self.user,
            role="warehouse_user_lvl1",
            id_number=123
        )
        group, _ = Group.objects.get_or_create(name=self.profile.role)
        self.user.groups.add(group)


    # Testează accesarea paginea de listare a transport_type
    def test_transport_type_list_all(self):

        #logheaza userl pentru testare
        self.client.login(username="testuser_logistics_lvl_1", password="secret123")


        response = self.client.get(reverse('LogisticManager:transport_type_list_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/transport_type_list.html')

"""
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
            route_type='land',
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


class LandTransportViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.TransportType = TransportType.objects.create(
            name="TIR",
            category='cargo',
            capacity=1000,
            capacity_unit="kg"
        )

        self.TransportTypeUpdate = TransportType.objects.create(
            name="Lorry",
            category='cargo',
            capacity=1000,
            capacity_unit="kg"
        )


        self.Route = Route.objects.create(
            route_type='land',
            from_T='City A',
            to_T='City B',
            length=200
        )

        self.RouteUpdate = Route.objects.create(
            route_type='land',
            from_T='City B',
            to_T='City C',
            length=300
        )


        self.LandTransport = LandTransport.objects.create(
            transport_type=self.TransportType,
            available=0,
            route=self.Route
            
        )

    # Testează accesarea paginea de listare a land transport
    def test_land_transport_list_all(self):
        response = self.client.get(reverse('LogisticManager:land_transport_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/land_transport_list.html')


    # Testează accesarea paginii de creare land transport (GET pe /routes/create/)
    def test_land_transport_create_get(self):
        response = self.client.get(reverse('LogisticManager:land_transport_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/land_transport_create.html')

    # Testează trimiterea unui formular valid pentru creare land transport (POST pe /routes/create/)
    def test_land_transport_create_post(self):
        response = self.client.post(reverse('LogisticManager:land_transport_create'), {
            'transport_type': self.TransportType.id,
            'available': 1,
            'route': self.Route.id ,
            
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertTrue(LandTransport.objects.filter(transport_type=self.TransportType).exists())

    # Testează actualizarea unui land transport existente (POST pe /routes/update/<pk>/)
    def test_land_transport_update_post(self):
        url = reverse('LogisticManager:land_transport_update', kwargs={'pk': self.LandTransport.pk})
        response = self.client.post(url, {
            'transport_type': self.TransportTypeUpdate.id,
            'available': 1,
            'route': self.RouteUpdate.id ,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.LandTransport.refresh_from_db()
        self.assertEqual(self.LandTransport.transport_type, self.TransportTypeUpdate)


    # Testează ștergerea unui land transport existent (POST pe /routes/delete/<pk>/)
    def test_land_transport_delete_post(self):
        url = reverse('LogisticManager:land_transport_delete', kwargs={'pk': self.LandTransport.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertFalse(LandTransport.objects.filter(pk=self.LandTransport.pk).exists())




class AirTransportViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.TransportType = TransportType.objects.create(
            name="DHL",
            category='cargo',
            capacity=10000,
            capacity_unit="kg"
        )

        self.TransportTypeUpdate = TransportType.objects.create(
            name="PrioryPost",
            category='cargo',
            capacity=20000,
            capacity_unit="kg"
        )


        self.Route = Route.objects.create(
            route_type='air',
            from_T='City A',
            to_T='City B',
            length=200
        )

        self.RouteUpdate = Route.objects.create(
            route_type='air',
            from_T='City B',
            to_T='City C',
            length=300
        )


        self.AirTransport = AirTransport.objects.create(
            transport_type=self.TransportType,
            available=0,
            route=self.Route
            
        )

    # Testează accesarea paginea de listare a air transport
    def test_air_transport_list_all(self):
        response = self.client.get(reverse('LogisticManager:land_transport_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/land_transport_list.html')


    # Testează accesarea paginii de creare air transport (GET pe /routes/create/)
    def test_air_transport_create_get(self):
        response = self.client.get(reverse('LogisticManager:air_transport_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/air_transport_create.html')

    # Testează trimiterea unui formular valid pentru creare air transport (POST pe /routes/create/)
    def test_air_transport_create_post(self):
        response = self.client.post(reverse('LogisticManager:air_transport_create'), {
            'transport_type': self.TransportType.id,
            'available': 1,
            'route': self.Route.id ,
            
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertTrue(AirTransport.objects.filter(transport_type=self.TransportType).exists())

    # Testează actualizarea unui air transport existent (POST pe /routes/update/<pk>/)
    def test_air_transport_update_post(self):
        url = reverse('LogisticManager:air_transport_update', kwargs={'pk': self.AirTransport.pk})
        response = self.client.post(url, {
            'transport_type': self.TransportTypeUpdate.id,
            'available': 1,
            'route': self.RouteUpdate.id ,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.AirTransport.refresh_from_db()
        self.assertEqual(self.AirTransport.transport_type, self.TransportTypeUpdate)


    # Testează ștergerea unui air transport existent (POST pe /routes/delete/<pk>/)
    def test_air_transport_delete_post(self):
        url = reverse('LogisticManager:air_transport_delete', kwargs={'pk': self.AirTransport.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertFalse(AirTransport.objects.filter(pk=self.AirTransport.pk).exists())




class NavalTransportViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.TransportType = TransportType.objects.create(
            name="EgeanNavy",
            category='cargo',
            capacity=10000,
            capacity_unit="kg"
        )

        self.TransportTypeUpdate = TransportType.objects.create(
            name="NorwayNavy",
            category='cargo',
            capacity=20000,
            capacity_unit="kg"
        )


        self.Route = Route.objects.create(
            route_type='naval',
            from_T='City A',
            to_T='City B',
            length=200
        )

        self.RouteUpdate = Route.objects.create(
            route_type='naval',
            from_T='City B',
            to_T='City C',
            length=300
        )


        self.NavalTransport = NavalTransport.objects.create(
            transport_type=self.TransportType,
            available=0,
            route=self.Route
            
        )

    # Testează accesarea paginea de listare a naval transport
    def test_naval_transport_list_all(self):
        response = self.client.get(reverse('LogisticManager:naval_transport_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/naval_transport_list.html')


    # Testează accesarea paginii de creare naval transport (GET pe /routes/create/)
    def test_naval_transport_create_get(self):
        response = self.client.get(reverse('LogisticManager:naval_transport_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogisticManager/naval_transport_create.html')

    # Testează trimiterea unui formular valid pentru creare naval transport (POST pe /routes/create/)
    def test_naval_transport_create_post(self):
        response = self.client.post(reverse('LogisticManager:naval_transport_create'), {
            'transport_type': self.TransportType.id,
            'available': 1,
            'route': self.Route.id ,
            
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertTrue(NavalTransport.objects.filter(transport_type=self.TransportType).exists())

    # Testează actualizarea unui naval transport existent (POST pe /routes/update/<pk>/)
    def test_naval_transport_update_post(self):
        url = reverse('LogisticManager:naval_transport_update', kwargs={'pk': self.NavalTransport.pk})
        response = self.client.post(url, {
            'transport_type': self.TransportTypeUpdate.id,
            'available': 1,
            'route': self.RouteUpdate.id ,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.NavalTransport.refresh_from_db()
        self.assertEqual(self.NavalTransport.transport_type, self.TransportTypeUpdate)


    # Testează ștergerea unui naval transport existent (POST pe /routes/delete/<pk>/)
    def test_naval_transport_delete_post(self):
        url = reverse('LogisticManager:naval_transport_delete', kwargs={'pk': self.NavalTransport.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('LogisticManager:successful'))
        self.assertFalse(NavalTransport.objects.filter(pk=self.NavalTransport.pk).exists())





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



"""