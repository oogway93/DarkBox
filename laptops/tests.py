from django.test import TestCase
from django.urls import reverse, resolve

from laptops.models import Laptop
from laptops.views import CatalogLaptop
from phones.models import Manufacturer


class LaptopTest(TestCase):
    def test_laptop_urls(self):
        url = reverse('laptop')
        self.assertEqual(resolve(url).func, CatalogLaptop)

    def test_laptop_views(self):
        response = self.client.get(f"{reverse('laptop')}")
        self.assertTemplateUsed(response, 'laptops/Catalog_Laptop.html')
        self.assertEqual(response.status_code, 200)

    def test_models(self):
        manuf = Manufacturer.objects.create(manufacturer='SamSung')
        manuf.save()
        manuf2 = Manufacturer.objects.create(manufacturer='Apple')
        manuf2.save()

        manufs = Manufacturer.objects.all()
        self.assertEqual(manufs.count(), 2)

        lap = Laptop.objects.create(manufacturer_id=1, operating_system='Windows', model='t2000', release_year='2005-09-17', memory=512, color='Full Black', price=52000, delivery=2000)
        lap.save()
        lap2 = Laptop.objects.create(manufacturer_id=2, operating_system='IOS', model='MacBook PRO', release_year='2015-10-05', memory=1024, color='Space Grey', price=40000, delivery=1000)
        lap2.save()

        laps = Laptop.objects.all()
        self.assertEqual(laps.count(), 2)
        response = self.client.get(reverse('laptop'))
        self.assertTrue(response.status_code, 201)
        self.assertGreater(lap.price, 40000)
        self.assertGreaterEqual(lap2.price, 40000)
        self.assertIn('IOS', lap2.operating_system)
        self.assertNotEqual(lap, lap2)
        self.assertIsInstance(lap, object)
        self.assertEqual(Laptop._meta.db_table, 'Laptop')
        self.assertTrue(Laptop.__doc__)
