import unittest
from bs4 import BeautifulSoup as bs

from app import app, replace_words


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """ Ensuer flask was up correctly """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_replace_words(self):
        """ Ensuer that funtion replace words correctly """
        obj = bs('<p>Layouts and visual mockups.</p>', 'lxml')
        tester = replace_words(obj)
        self.assertEqual(str(tester).count('™'), 1)


if __name__ == '__main__':
    unittest.main()
