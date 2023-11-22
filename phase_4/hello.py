import sys
from lib.customer import * 
from lib.menu import *

print('hello')

menu = Menu()
menu.add_item('coke', 2)
menu.add_item('chips', 3)
menu.add_item('chicken', 5)

customer = Customer('Liam', menu)
customer.add('chicken', 2)
customer.add('coke', 2)
customer.add('chips', 2)
print(customer.view_order())

customer.place_order()

sys.stdout.flush()