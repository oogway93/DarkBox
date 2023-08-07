from django.test import TestCase


class HomePageTest(TestCase):
    def test_base_page(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.endswith("</html>"))
        self.assertIn("<hr>", html)
        self.assertTemplateUsed(response, 'base.html')
