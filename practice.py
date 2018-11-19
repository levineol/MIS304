#Class header

import dessert
import ice_cream
import sundae
PRICE = .29
    
def purchase_sundae(item_list, cost_list):
    name = "Sundae"
    kind = input("What flavor of ice cream would you like? ")
    kind = kind[0].upper() + kind[1:]
    sundaes = sundae.Sundae(name, kind)
    size = input("What size would you like? ('S', 'M', or 'L') ")
    validate_sundae = sundaes.update_size(size)
    while validate_sundae == "FALSE":
        size = input("What size would you like? ('S', 'M', or 'L') ")
        validate_sundae = sundaes.update_size(size)
    toppings = int(input("How many toppings would you like to order? "))
    validate_toppings = sundaes.update_toppings(toppings)
    while validate_toppings == "FALSE":
        toppings = int(input("How many toppings would you like to order? "))
        validate_toppings = sundaes.update_toppings(toppings)
    
    cost_list.append(sundaes.calculate_cost())
    item_list.append(sundaes)
    
def main():
    items_list = []
    costs_list = []
    purchase_sundae(items_list, costs_list)
    for stuff in items_list:
        print(stuff.__str__())
main()
    
    
