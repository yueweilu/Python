import unittest
from name_function import get_fomatted_name
class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name= get_fomatted_name('janis','joplin')
        self.assertEqual(formatted_name,'janis Joplin')
unittest.main()
