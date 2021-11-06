from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale


locale.setlocale(locale.LC_ALL, 'en_US')

choice = "y"
while choice == "y":

    # get user entry
    order_total = Decimal(input("Enter order total:     "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()

    # determine discount percent
    if 0 < order_total < 100:
        discount_percent = Decimal("0")
    elif 100 <= order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calc results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
    subtotal = order_total - discount
    shipping_rate = Decimal(".085")
    shipping_cost = subtotal * shipping_rate
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)
    invoice_total = subtotal + sales_tax

    # display results

    s1 = ">10"  # formatting spec 1
    s2 = "10,"  # formatting spec 2
    w1 = "20"   # formatting width of string literals

    print(f"{'Order total:':{w1}}{locale.currency(order_total, grouping=True):{s1}}")
    print(f"{'Discount amount:':{w1}}{discount:{s2}}")
    print(f"{'Subtotal:':{w1}}{subtotal:{s2}}")
    print(f"{'Shipping cost:':{w1}}{shipping_cost:{s2}}")
    print(f"{'Sales tax:':{w1}}{sales_tax:{s2}}")
    print(f"{'Invoice total:':{w1}}{locale.currency(invoice_total, grouping=True):{s1}}")
    print()

    choice = input("Continue? (y/n): ")
    print()

print("Bye!")

# if __name__ == '__main__':
#     main()
