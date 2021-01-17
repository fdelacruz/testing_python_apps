from unittest import TestCase

from models.item import ItemModel


class TestItem(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 0.99)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 0.99,
                         "The price of the item after creation does not equal the constructor argument.")

    def test_item_json(self):
        item = ItemModel('test', 0.99)

        expected = {
            'name': item.name,
            'price': 0.99
        }

        self.assertEqual(expected, item.json(), "The JSON export of the item is incorrect. Expected {}, received {}.".format(expected, item.json()))
