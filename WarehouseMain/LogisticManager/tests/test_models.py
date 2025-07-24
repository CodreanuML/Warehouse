from django.test import TestCase
from django.core.exceptions import ValidationError
from LogisticManager.models import Transport, TransportType, Route, LandTransport, NavalTransport, AirTransport

class TransportModelTests(TestCase):

    def setUp(self):
        # Crează date de bază pentru teste
        self.land_type = TransportType.objects.create(
            name='Truck',
            category='cargo',
            capacity=1000,
            capacity_unit='kg'
        )
        self.naval_type = TransportType.objects.create(
            name='Boat',
            category='personnel',
            capacity=50,
            capacity_unit='pers'
        )
        self.air_type = TransportType.objects.create(
            name='Plane',
            category='military',
            capacity=5,
            capacity_unit='units'
        )

        self.land_route = Route.objects.create(
            route_type='land',
            from_T='CityA',
            to_T='CityB',
            length=100
        )
        self.naval_route = Route.objects.create(
            route_type='naval',
            from_T='PortA',
            to_T='PortB',
            length=300
        )
        self.air_route = Route.objects.create(
            route_type='air',
            from_T='AirportA',
            to_T='AirportB',
            length=800
        )


    #Route Tests
    
    def test_land_route_unit_km(self):
        #testeaza daca se salveaza corect unitatea pentru transport terestru
        r=self.land_route
        self.assertEqual(r.unit,"Km")

    def test_naval_route_unit_nm(self):
        #testaza daca se salveaza corect unitatea pentru transport naval
        r=self.naval_route
        self.assertEqual(r.unit,"NM")    

    def test_air_route_unit_nm(self):
        #testaza daca se salveaza corect unitatea pentru transport aerian
        r=self.air_route
        self.assertEqual(r.unit,"NM")    


    #Transport Air/Land/Naval Tests    

    def test_transport_str(self):
        # Testează metoda __str__ pentru Transport
        t = Transport.objects.create(name='GenericTransport')
        self.assertEqual(str(t), 'GenericTransport')

    def test_transporttype_str(self):
        # Testează metoda __str__ pentru TransportType
        self.assertEqual(str(self.land_type), 'Truck (cargo) - 1000 kg')

    def test_route_str(self):
        # Testează metoda __str__ pentru Route
        self.assertEqual(str(self.land_route), 'CityA-CityB (Land)')

    def test_land_transport_valid(self):
        # Verifică că se poate crea LandTransport cu o rută corectă
        lt = LandTransport(
            name='Truck1',
            transport_type=self.land_type,
            available=True,
            route=self.land_route
        )
        lt.full_clean()

    def test_land_transport_invalid_route(self):
        # Verifică că LandTransport nu acceptă o rută navală
        lt = LandTransport(
            name='Truck2',
            transport_type=self.land_type,
            available=True,
            route=self.naval_route
        )
        with self.assertRaises(ValidationError):
            lt.full_clean()

    def test_naval_transport_invalid_route(self):
        # Verifică că NavalTransport nu acceptă o rută aeriană
        nt = NavalTransport(
            name='Boat1',
            transport_type=self.naval_type,
            available=True,
            route=self.air_route
        )
        with self.assertRaises(ValidationError):
            nt.full_clean()

    def test_air_transport_invalid_route(self):
        # Verifică că AirTransport nu acceptă o rută terestră
        at = AirTransport(
            name='Jet1',
            transport_type=self.air_type,
            available=True,
            route=self.land_route
        )
        with self.assertRaises(ValidationError):
            at.full_clean()

    def test_transporttype_requires_name(self):
        # Verifică că numele nu poate fi null în TransportType
        with self.assertRaises(Exception):
            TransportType.objects.create(
                name=None,
                category='cargo',
                capacity=100,
                capacity_unit='kg'
            )
            

    def test_route_duplicate_allowed_by_default(self):
        # Verifică că se pot crea două rute cu aceeași origine și destinație
        Route.objects.create(
            route_type='land',
            from_T='CityA',
            to_T='CityB',
            length=150
        )
        self.assertEqual(Route.objects.filter(from_T='CityA', to_T='CityB').count(), 2)

    def test_transporttype_capacity_unit_blank(self):
        # Verifică că capacity_unit poate fi gol
        t = TransportType.objects.create(
            name='Unitless',
            category='cargo',
            capacity=500,
            capacity_unit=''
        )
        self.assertEqual(t.capacity_unit, '')

    def test_get_method_empty_queryset(self):
        # Testează metoda get() când queryset-ul e gol
        TransportType.objects.all().delete()
        self.assertEqual(TransportType.get(), [])

    def test_delete_transporttype_cascades(self):
        # Verifică ștergerea în cascadă a LandTransport când TransportType e șters
        lt = LandTransport.objects.create(
            name='TruckCascade',
            transport_type=self.land_type,
            available=True,
            route=self.land_route
        )
        self.land_type.delete()
        self.assertEqual(LandTransport.objects.count(), 0)

    def test_route_max_length_exceeded(self):
        # Verifică eroare la lungime prea mare pentru from_T
        too_long = 'X' * 60
        r = Route(
            route_type='land',
            from_T=too_long,
            to_T='CityY',
            length=200
        )
        with self.assertRaises(ValidationError):
            r.full_clean()

    def test_landtransport_available_flag(self):
        # Verifică valoarea atributului available
        lt = LandTransport.objects.create(
            name='TruckAvailable',
            transport_type=self.land_type,
            available=False,
            route=self.land_route
        )
        self.assertFalse(lt.available)

    def test_route_name_generated_correctly(self):
        # Verifică generarea corectă a numelui pentru rută
        r = Route.objects.create(
            route_type='land',
            from_T='Town1',
            to_T='Town2',
            length=150
        )
        self.assertEqual(r.name, 'Town1-Town2')

    def test_unicode_name(self):
        # Verifică suportul pentru caractere unicode în nume
        t = Transport.objects.create(name='🚛 UnicodeTruck')
        self.assertIn('🚛', str(t))

    def test_landtransport_str(self):
        # Verifică metoda __str__ pentru LandTransport
        lt = LandTransport.objects.create(
            name='TestLandTruck',
            transport_type=self.land_type,
            available=True,
            route=self.land_route
        )
        self.assertEqual(str(lt), 'TestLandTruck')