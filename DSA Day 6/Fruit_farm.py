class FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            return FruitInfo.fruit_price_list[FruitInfo.fruit_name_list.index(fruit_name)]
        else:
            return -1


class Purchase:
    counter = 101

    def __init__(self, customer_name, fruit_name, quantity, customer_type):
        self.purchase_id = 'P' + str(Purchase.counter)
        Purchase.counter += 1
        self.customer_name = customer_name
        self.fruit_name = fruit_name
        self.quantity = quantity
        self.customer_type = customer_type

    def calculate_price(self):
        fruit_price = FruitInfo.get_fruit_price(self.fruit_name)
        if fruit_price != -1:
            total_price = fruit_price * self.quantity
            if fruit_price == max(FruitInfo.fruit_price_list) and self.quantity > 1:
                total_price *= 0.98
            elif fruit_price == min(FruitInfo.fruit_price_list) and self.quantity >= 5:
                total_price *= 0.95
            if self.customer_type == 'wholesale':
                total_price *= 0.9
            return total_price
        else:
            return -1


class Customer:
    def __init__(self, customer_name, customer_type):
        self.customer_name = customer_name
        self.customer_type = customer_type


# Testing the classes
customer = Customer('John', 'wholesale')
purchase = Purchase(customer.customer_name, 'Grape', 6, customer.customer_type)
print('Purchase ID:', purchase.purchase_id)
print('Customer Name:', purchase.customer_name)
print('Fruit Name:', purchase.fruit_name)
print('Quantity:', purchase.quantity)
print('Customer Type:', purchase.customer_type)
print('Total Price:', purchase.calculate_price())
