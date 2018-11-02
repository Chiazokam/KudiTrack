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

if __name__ == '__main__':
    unittest.main()
