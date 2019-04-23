# pages/tests.py

from django.test import SimpleTestCase # This import package is used since no database is present.  TestCase is used if there is database.



class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) # 200 is std http request


    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
