prices = [4.95, 9.95, 14.95, 19.95, 24.95]
print("Original Price | Discount | New Price")
for price in prices:
    discount = price * 0.6
    new_price = price - discount
    print(f"{price:.2f} | {discount:.2f} | {new_price:.2f}")