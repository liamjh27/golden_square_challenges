Classes
Menu class to display menu
attributes:
dictionary containing the name of the dish and prices for dishes
methods:
add() to add an item to the menu. parameters: str representing dish, float represeinting price. side effects: modifies menu dictionary.
remove() to remove items from the menu. parameters: str representing the dish to remove. side effects: modifies menu dictionary.
view() to display the menu. no parameters no side effects.

Customer:
attributes:
name, to store the customers name and personalise messages. str.
current order: a list of dictionaries representing a dish and quantity currently in the customers order. initialises empty. 

methods:
add() to add to current order. parameters: str name of dish, int representing quantity required. side effects: modifies current order list.
remove() attributes: str representing dish name. int representing number to remove. side effects: modifies current order list.
view_order() parameters: none. returns a breakdown of the current order and total. 