import json


name=input("enter your name:")
age=input("enter your age:")
price=input("enter the price:")
discountp=input("enter discount %:")
vatp=input("enter vat %:")
def finalprice(price, discountp, vatp):
    discount = price * discountp / 100
    nprice = price - discount
    vat = nprice * vatp / 100
    fprice = nprice + vat
    return fprice

user_profile = {
    "name": name,
    "age": int(age),
    "price": int(price),
    "discount": float(discountp),
    "vat": float(vatp)
}
file_name="user profile.json"
with open(file_name,"w") as f:
    json.dump(user_profile,f)

print(f"user data for {name} save succesfully to {file_name}")