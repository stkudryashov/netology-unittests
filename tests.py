from unittest import TestCase
from unittest.mock import patch

from app import *


class TestSecretaryProgram(TestCase):

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf(), '1')

    @patch('builtins.input', side_effect=['11-3', 'passport', 'Алеша Шишкин', '3'])
    def test_add_new_doc(self, mock_input):
        self.assertEqual(add_new_doc(), '3')

        test_new_doc = {
            "type": 'passport',
            "number": '11-3',
            "name": 'Алеша Шишкин'
        }

        self.assertIn(test_new_doc, documents)
        self.assertIn('11-3', directories['3'])

    @patch('builtins.input', lambda *args: '4')
    def test_add_new_shelf(self):
        test_shelf_number, test_added = add_new_shelf()
        self.assertEqual(test_shelf_number, '4')
        self.assertEqual(test_added, True)

    @patch('builtins.input', lambda *args: '10006')
    def test_delete_doc(self):
        test_doc_number, test_deleted = delete_doc()
        self.assertEqual(test_doc_number, '10006')
        self.assertEqual(test_deleted, True)

        test_deleted_doc = {
            "type": 'insurance',
            "number": '10006',
            "name": 'Аристарх Павлов'
        }

        self.assertNotIn(test_deleted_doc, documents)
        self.assertNotIn('10006', directories['2'])
