class Customer:
    def __init__(self, name, menu_list):
        self.name = name
        self.menu_list = menu_list 
        self.order = []


    def add(self, item, quantity=1):
        price = None
        for dish in self.menu_list.menu_items:
            if dish['Dish'] == item:
                price = dish['Price']
                break
        if price == None:
            return 'We don\'t have that dish.'
        for dish in self.order:
            if dish['Dish'] == item:
                dish['Quantity'] += quantity
                return
        self.order.append({'Dish' : item, 'Price' : price, 'Quantity' : quantity})

    
    def get_total(self):
        return sum([(dish['Price'] * dish['Quantity']) for dish in self.order])
    

    def view_order(self):
        output = 'Your order:\n'
        for dish in self.order:
            output += f"{dish['Quantity']} x {dish['Dish']}: £{(dish['Price'] * dish['Quantity']):.2f}\n"
        total = self.get_total()
        output += f'Your total: £{total:.2f}'
        return output 
    
    def remove(self, item, quantity=1):
        dict = next((entry for entry in self.order if entry['Dish'] == item), None)
        if dict == None:
            return 'You haven\'t added that yet.'
        elif dict['Quantity'] - quantity <= 0:
              self.order = [entry for entry in self.order if entry['Dish'] != item]
        else: 
            dict['Quantity'] -= quantity