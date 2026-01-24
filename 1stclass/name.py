import json
import os

file_name = "users.json"

# Load existing data if file exists
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        users = json.load(f)
else:
    users = []

# Function to calculate final price
def finalprice(price, discountp, vatp):
    discount = price * discountp / 100
    nprice = price - discount
    vat = nprice * vatp / 100
    return nprice + vat

# Number of users
n = int(input("How many users? "))

for i in range(n):
    print(f"\nEnter details for user {i+1}")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    price = float(input("Enter price: "))
    discountp = float(input("Enter discount %: "))
    vatp = float(input("Enter VAT %: "))

    final_price = finalprice(price, discountp, vatp)

    user_profile = {
        "name": name,
        "age": age,
        "original_price": price,
        "discount_percent": discountp,
        "vat_percent": vatp,
        "final_price": final_price
    }

    users.append(user_profile)

# Save all users
with open(file_name, "w") as f:
    json.dump(users, f, indent=4)

print("\nAll user data saved successfully!")
import os
print(os.getcwd())
