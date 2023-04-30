import unittest
from classes import *
from datetime import datetime, timedelta
from data import personnel, stock
from unittest.mock import patch, MagicMock

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item('New', 'Shirt', '2022-12-31 23:59:59')

    def test_last_stocked(self):
        self.assertEqual(self.item.last_stocked(), 'Last stocked: 120 days ago')

    def test_get_product_name(self):
        self.assertEqual(self.item.get_product_name(), 'New Shirt')

    def test_str(self):
        self.assertEqual(str(self.item), 'New Shirt')

    class TestWarehouse(unittest.TestCase):
        def setUp(self):
            self.warehouse = Warehouse(1)
            self.item1 = Item('New', 'Shirt', '2022-12-31 23:59:59')
            self.item2 = Item('Used', 'Jacket', '2022-12-30 23:59:59')
            self.warehouse.add_item(self.item1)
            self.warehouse.add_item(self.item2)

    def test_occupancy(self):
        self.assertEqual(self.warehouse.occupancy(), 2)

    def test_add_item(self):
        item3 = Item('Old', 'Hat', '2022-12-29 23:59:59')
        self.warehouse.add_item(item3)
        self.assertEqual(self.warehouse.occupancy(), 3)

    def test_search(self):
        class MockUser:
            def __init__(self):
                self.history = []

            def add_to_history(self, search_string):
                self.history.append(search_string)

        mock_user = MockUser()
        matches = self.warehouse.search('New Shirt', mock_user)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], self.item1)
        self.assertEqual(mock_user.history, ['Searched for New Shirt in New Shirt'])

class TestWarehouse(unittest.TestCase):

    def setUp(self):
        self.warehouse_id = 1
        self.warehouse = Warehouse(self.warehouse_id)
        self.item1 = Item('state1', 'category1', '2023-01-01 00:00:00', self.warehouse)
        self.item2 = Item('state2', 'category2', '2023-02-01 00:00:00', self.warehouse)
        self.item3 = Item('state3', 'category3', '2023-03-01 00:00:00', self.warehouse)
        self.inventory = [
            {'state': 'state1', 'category': 'category1', 'date_of_stock': '2023-01-01 00:00:00', 'warehouse': 1},
            {'state': 'state2', 'category': 'category2', 'date_of_stock': '2023-02-01 00:00:00', 'warehouse': 1},
            {'state': 'state3', 'category': 'category3', 'date_of_stock': '2023-03-01 00:00:00', 'warehouse': 2},
        ]

    def test_occupancy(self):
        self.assertEqual(self.warehouse.occupancy(), 0)
        self.warehouse.add_item(self.item1)
        self.assertEqual(self.warehouse.occupancy(), 1)

    def test_add_item(self):
        self.assertEqual(len(self.warehouse.stock), 0)
        self.warehouse.add_item(self.item1)
        self.assertEqual(len(self.warehouse.stock), 1)
        self.assertIn(self.item1, self.warehouse.stock)

    def test_search(self):
        user_mock = MagicMock()
        matches = self.warehouse.search('category1', user_mock)
        self.assertEqual(len(matches), 1)
        self.assertIn(self.item1, matches)
        user_mock.add_to_history.assert_called_once_with('Searched for category1 in state1 category1')

    def test_order(self):
        matches = [self.item1, self.item2]
        user_mock = MagicMock()
        with patch('builtins.input', side_effect=[2]):
            order_amount = Warehouse.order(self.warehouse, matches, user_mock)
        self.assertEqual(order_amount, 2)
        user_mock.add_to_history.assert_called_once_with('Ordered "2" - "state1 category1(s)" from "1"')

    def test_get_warehouse_stock(self):
        self.assertEqual(len(self.warehouse.stock), 0)
        self.warehouse.get_warehouse_stock(self.inventory)
        self.assertEqual(len(self.warehouse.stock), 2)
        self.assertIn(self.item1, self.warehouse.stock)
        self.assertIn(self.item2, self.warehouse.stock)

    def test_display_warehouse(self):
        user_mock = MagicMock()
        with patch('builtins.print'):
            self.warehouse.display_warehouse(user_mock)
        user_mock.add_to_history.assert_called_once_with('Browsed "0" product(s) in "Warehouse 1"')

    def test_total_stock(self):
        warehouses = Warehouse.total_stock(self.inventory)
        self.assertEqual(warehouses, {1, 2})
        self.assertEqual(len(Warehouse.warehouses_total_stock), 3)
        self.assertEqual(len(Warehouse.warehouses_list), 2)

    def test_delete_item(self):
        item_to_delete = Item('item1', 'category1')
        self.warehouse.stock = [item_to_delete, Item('item2', 'category2')]

        self.warehouse.delete_item('item1')
        self.assertNotIn(item_to_delete, self.warehouse.stock)

    def test_str(self):
        self.assertEqual(str(self.warehouse), 'Warehouse test_warehouse')


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User('John')

    def test_get_user_name(self):
        self.assertEqual(self.user.get_user_name(), 'John')

    def test_greet(self):
        self.assertEqual(self.user.greet(), "Hello, John!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,please ask one of our staff members to assist you.")

    def test_bye(self):
        self.assertEqual(self.user.bye(), "Thank you for your visit, John")

    def test_check_user(self):
        staff_db = [{"user_name": "Alice"}, {"user_name": "Bob", "head_of": [{"user_name": "Charlie"}]}]
        self.assertEqual(User.check_user(staff_db, "Charlie"), {"user_name": "Charlie"})
        self.assertFalse(User.check_user(staff_db, "Dave"))

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("JohnDoe", "mypassword")

    def test_authenticate(self):
        self.assertTrue(self.employee.authenticate("mypassword"))
        self.assertFalse(self.employee.authenticate("wrongpassword"))

    def test_greet(self):
        expected_greeting = f'Hello, {self.employee.get_user_name()}!\n If you experience a problem with the system, please contact technical support.'
        self.assertEqual(self.employee.greet(), expected_greeting)

    def test_add_to_history(self):
        Employee.add_to_history("Logged in as JohnDoe")
        self.assertIn("Logged in as JohnDoe", Employee.history)



if __name__ == '__main__':
    unittest.main()