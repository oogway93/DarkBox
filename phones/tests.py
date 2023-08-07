from django.urls import reverse, resolve
from django.test import TestCase

from phones.models import Phone, Manufacturer
from phones.views import CatalogPhone, Base


class TypicalTest(TestCase):
    def test_calc_operations(self):
        self.assertTrue(2 + 2, 4)


class HomePageTest(TestCase):
    def test_base_page(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.endswith("</html>"))
        self.assertIn("<hr>", html)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTrue(response.status_code, 200)
        self.assertContains(response, 'List of catalogs')


class PhoneTest(TestCase):
    def test_phone_models(self):
        manuf = Manufacturer()
        manuf.manufacturer = 'Apple'
        manuf.save()

        manu = Manufacturer.objects.all()
        self.assertTrue(manu.count(), 1)

        phone = Phone()
        phone.manufacturer_id = 1
        phone.model = 'Iphone 11 pro max'
        phone.operating_system = 'IOS'
        phone.release_year = '2010-08-19'
        phone.memory = 64
        phone.color = 'Light Green'
        phone.price = 59000
        phone.delivery = 1000
        phone.is_out_of_stocks = True
        phone.save()

        phones = Phone.objects.all()
        p = Phone.objects.get(id=1)
        self.assertTrue(phones.count(), 1)
        self.assertGreater(p.price, 50000)
        self.assertNotEqual(p.color, 'White')
        self.assertLess(p.memory, 100)
        response = self.client.get('/')
        self.assertTrue(response.status_code, 201)

    def test_phone_views(self):
        response = self.client.get('/phones')
        self.assertTemplateUsed(response, 'phones/Catalog_Phone.html')

    def test_phone_urls(self):
        url = reverse('phone')
        url2 = reverse('home')
        self.assertEqual(resolve(url).func, CatalogPhone)
        self.assertEqual(resolve(url2).func, Base)
