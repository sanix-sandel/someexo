"""
Product Inventory Project - Create an application which manages an inventory of products.
 Create a product class which has a price, id, and quantity on hand.
 Then create an inventory class which keeps track of various products and can sum up the inventory value.

"""
from operator import attrgetter
from itertools import groupby


fonction=lambda x: x[0]*x[1]

class Product:
    def __init__(self, name, id, price):
        self.name=name
        self.id=id
        self.price=price

    def __str__(self):
        return f"{self.name}"

class Inventory:
    def __init__(self):
        self.nbr_of_products=0
        self.liste_of_products=[]
        self.NbrItems=dict()

    def add_product(self, Product):
        self.liste_of_products.append(Product)
        self.nbr_of_products+=1

        self.NbrItems[Product.name]=self.NbrItems.get(Product.name, 0)+1


    def display(self):
        inventor=dict()
        #for x in self.liste_of_products:

            #inventor[x.name]=inventor.get(x, 0)+1
        liste=[(x.name, x.price, self.NbrItems[x.name]) for x in self.liste_of_products]
        return print(liste)

    def search_by_price(self):
        liste=groupby((self.liste_of_products), key=attrgetter('price'))
        for x, y in liste:
            print(x)
            for x in y:
                print(x)

    def search_by_id(self, id):
        for x in self.liste_of_products:
            try:
                if x.id==id:
                    product=x
                    return print(product)
                else:
                    return print('There is no product with such ID')
            except:
                return print('There is no product with such ID')

    def total_sum(self):
        liste = [(x.price, self.NbrItems[x.name]) for x in self.liste_of_products]
        a=sum(list(map(fonction, liste)))

        return print('This inventory is evaluated to {}'.format(a))

    def buy(self, name, quantity):
        if name not in self.NbrItems:
            return print("Such product isn't present right now")
        if self.NbrItems[name]<quantity:
            return print('Not sufficient qunatity')
        self.NbrItems[name]-=quantity
        return print('You brought {} {}'.format(quantity, name))

"""
    def search_by_price(self, price):

    def search_by_name(self, name):

"""

apple=Product('apple', 1, 40)
mango=Product('mango', 4, 10)

Inventor=Inventory()
Inventor.add_product(apple)
Inventor.add_product(mango)
Inventor.display()
print(Inventor.NbrItems)
Inventor.search_by_price()
Inventor.search_by_id(5)
Inventor.total_sum()
Inventor.buy('mango', 1)
Inventor.display()

#if __name__=='__main__':


