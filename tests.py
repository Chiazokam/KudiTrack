import unittest
from main_app import app


class TestKudiApp(unittest.TestCase):
    def test_rootPage(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_rootPageContent(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Date: yyyy-mm-dd' in response.data)

    def test_businessPage(self):
        tester = app.test_client(self)
        response = tester.get('/business', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_personalPage(self):
        tester = app.test_client(self)
        response = tester.get('/personal', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
