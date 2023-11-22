from readline import set_completion_display_matches_hook
from lib.menu import *
from lib.customer import *
from unittest.mock import Mock 

def test_initializes_with_empty_order():
    customer = Customer('Liam', 'menu', sendsms)
    result = customer.order
    assert result == []

def test_add_item_sets_up_order_dictionary_properly():
    menu = Menu()
    menu.add_item('Fish', 3.50)
    customer = Customer('Liam', menu, sendsms)
    customer.add('Fish')
    result = customer.order
    assert result == [{'Dish' : 'Fish', 'Price' : 3.50, 'Quantity' : 1}]

def test_add_multiple_of_an_item():
    menu = Menu()
    menu.add_item('Fish', 3.50)
    customer = Customer('Liam', menu, sendsms)
    customer.add('Fish', 2)
    result = customer.order
    assert result == [{'Dish' : 'Fish', 'Price' : 3.50, 'Quantity' : 2}]

def test_get_total():
    menu = Menu()
    menu.add_item('Fish', 3.50)
    menu.add_item('Coffee', 3)
    customer = Customer('Liam', menu, sendsms)
    customer.add('Fish', 2)
    customer.add('Coffee',)
    result = customer.get_total()
    assert result == 10

def test_view_order():
    menu = Menu()
    menu.add_item('Fish', 3.50)
    menu.add_item('Coffee', 3)
    customer = Customer('Liam', menu, sendsms)
    customer.add('Fish', 2)
    customer.add('Coffee',)
    result = customer.view_order()
    assert result == 'Your order:\n2 x Fish: £7.00\n1 x Coffee: £3.00\nYour total: £10.00'


def test_remove_item_from_multiple_order():
    menu = Menu()
    menu.add_item('Coffee', 3)
    customer = Customer('Liam', menu, sendsms)
    customer.add('Coffee', 3)
    customer.remove('Coffee', 2)
    result = customer.order
    assert result == [{'Dish' : 'Coffee', 'Price' : 3.00, 'Quantity' : 1}]


def test_remove_item_completely_if_quantity_less_than_zero():
    menu = Menu()
    menu.add_item('Coffee', 3)
    customer = Customer('Liam', menu, sendsms)
    customer.add('Coffee', 3)
    customer.remove('Coffee', 5)
    result = customer.order
    assert result == []

def test_remove_if_quantity_exactly_zero():
    menu = Menu()
    menu.add_item('Coffee', 3)
    customer = Customer('Liam', menu, sendsms)
    customer.add('Coffee', 3)
    customer.remove('Coffee', 3)
    result = customer.order
    assert result == []

def test_remove_unadded_item():
    menu = Menu()
    menu.add_item('Coffee', 3)
    customer = Customer('Liam', menu, sendsms)    
    result = customer.remove('Coffee')
    assert result == 'You haven\'t added that yet.'

def test_send_sms_message():
    service = Mock(name='service')
    menu = Menu()
    menu.add_item('Fish', 3.50)
    menu.add_item('Coffee', 3)
    customer = Customer('Liam', menu, service)
    customer.add('Fish', 2)
    customer.add('Coffee',)
    customer.place_order()
    service.assert_called()
    service.assert_called_with(customer.name, customer.view_order())