class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item, price):
        price = round(float(price), 2)
        self.menu_items.append({'Dish' : item, 'Price' : price})

    def view(self):
        formatted_menu = ''
        for dish in self.menu_items:
            formatted_menu += f'{dish["Dish"].capitalize()} : £{dish["Price"]:.2f}\n'
        return formatted_menu
    
    def remove_item(self, item):
        self.menu_items = [dish for dish in self.menu_items if dish['Dish'] != item]