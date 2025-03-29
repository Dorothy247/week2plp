def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"After applying a {discount_percent}% discount,")
    print(f"The final price is: ${final_price:.2f}")
else:
    print("No discount applied (needs to be 20% or higher).")
    print(f"The price remains: ${original_price:.2f}")
