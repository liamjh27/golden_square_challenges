from lib.menu import *

def test_menu_initialises_with_an_empty_menu():
    menu = Menu()
    result = menu.menu_items
    assert result == []

# def test_add_items_to_menu():
#     menu = Menu()
#     menu.add_item('soup of the day', 5)
#     menu.add_item('fish', 3.5)
#     result = menu.menu_items
#     assert result == {'soup of the day' : 5.00, 'fish' : 3.50}

def test_view_menu_displays_formatted_menu():
    menu = Menu()
    menu.add_item('soup of the day', 5)
    menu.add_item('fish', 3.5)
    result = menu.view()
    assert result == 'Soup of the day : £5.00\nFish : £3.50\n'

def test_remove_item_from_menu():
    menu = Menu()
    menu.add_item('soup of the day', 5)
    menu.add_item('fish', 3.5)
    menu.remove_item('fish')
    result = menu.menu_items
    assert result == [{'Dish' : 'soup of the day', 'Price' : 5.00}]