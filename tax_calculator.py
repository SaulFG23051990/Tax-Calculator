def add_tax(price, tax_rate):
    float(tax_rate)
    after_tax= (price*tax_rate)+price
    return after_tax
print(add_tax(50,0.08))
print(add_tax(19.99, 0.07))
print(add_tax(0,0.10))
