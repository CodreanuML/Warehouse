from django.test import TestCase
import logging
from WarehouseManager.models import Transport,TransportType,Car_routes,Naval_routes,CarTransport,NavalTransport



class TransportModelTest(TestCase):

	def setUp(self):
		loglevel = logging.DEBUG
		logging.basicConfig(level=loglevel)
		TransportType.objects.create(name="Cargo")
		TransportType.objects.create(name="Petroleum")
		TransportType.objects.create(name="Personell")


		Car_routes.objects.create(from_T="Dragasani",to_T="Draganesti")
		Car_routes.objects.create(from_T="Bucuresti",to_T="Craiova")
		Car_routes.objects.create(from_T="Cricova",to_T="Dunareni")


		Naval_routes.objects.create(from_T="Burvas",to_T="Dragoslavia")
		Naval_routes.objects.create(from_T="Tenesee",to_T="NewYork")
		Naval_routes.objects.create(from_T="Canare",to_T="Sanchez")

		CarTransport.objects.create(name="Vivaro",CarTransportType=TransportType.objects.get(pk=1).get()[0],Parked=True,Route=Car_routes.objects.get(pk=1).get()[0])
		CarTransport.objects.create(name="Fiat",CarTransportType=TransportType.objects.get(pk=3).get()[0],Parked=True,Route=Car_routes.objects.get(pk=3).get()[0])

		NavalTransport.objects.create(name="ReginaMarii",NavalTransportType=TransportType.objects.get(pk=1).get()[0],Docked=True,Route=Naval_routes.objects.get(pk=1).get()[0])
		NavalTransport.objects.create(name="Ferdinand",NavalTransportType=TransportType.objects.get(pk=2).get()[0],Docked=True,Route=Naval_routes.objects.get(pk=2).get()[0])


# check all field length 

	def test_TransportType_length_true(self):
		transport_type1 = TransportType.objects.get(id=1)
		print(transport_type1._meta)
		max_length = transport_type1._meta.get_field('name').max_length
		self.assertEqual(max_length, 50)


	def test_CarRoutes_length_true(self):
		car_routes1 = Car_routes.objects.get(id=1)
		print(car_routes1._meta)
		max_length = car_routes1._meta.get_field('name').max_length
		self.assertEqual(max_length, 100)


	def test_NavalRoutes_length_true(self):
		naval_routes1 = Naval_routes.objects.get(id=1)
		print(naval_routes1._meta)
		max_length = naval_routes1._meta.get_field('name').max_length
		self.assertEqual(max_length, 100)



	def test_CarTransport_length_true(self):
		car_routes1 = CarTransport.objects.get(id=1)
		print(car_routes1._meta)
		max_length = car_routes1._meta.get_field('name').max_length
		self.assertEqual(max_length, 100)


	def test_NavalTransport_length_true(self):
		naval_routes1 = NavalTransport.objects.get(id=1)
		print(naval_routes1._meta)
		max_length = naval_routes1._meta.get_field('name').max_length
		self.assertEqual(max_length, 100)

#check overwritten saved method

	def test_CarRoutes_name_true(self):
		car_routes1 = Car_routes.objects.get(id=1)
		print(car_routes1._meta)
		car_routes_name = car_routes1.name
		logging.debug(car_routes_name)
		self.assertEqual(car_routes_name,"Dragasani-Draganesti")


	def test_NavalRoutes_name_true(self):
		naval_routes1 = Naval_routes.objects.get(id=1)
		print(naval_routes1._meta)
		naval_routes_name = naval_routes1.name
		self.assertEqual(naval_routes_name,"Burvas-Dragoslavia")


#check get() method if return tupple 