#Program header

def get_price():
    price = float(input("Enter price: $"))
    return price
def calc_sales_tax(orig_price):
    tax = orig_price * .0825
    return tax
def main():
    item_price = get_price()
    sales_tax = calc_sales_tax(item_price)
    final_price = item_price + sales_tax
    print("Sales tax: $", format(sales_tax, ".2f"), sep="")
    print("Final price: $", format(final_price, ".2f"), sep="")
main()
