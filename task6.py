"""
Task 6: Electronics Store Nested Cart
Three friends, Tobi, Lami, and Chinedu, visit an electronics store together. 
They decide to share **one big smart cart** that can group items by the department they are picked from.
The cart keeps track of each department with the items selected inside it.

cart = {
    "phones": {},
    "laptops": {},
    "accessories": {}
}

Each product in the store is represented as a tuple: (product_name, price) because these details never change.

During shopping:
- Tobi picks up an iPhone for 750000 Naira in the "phones" department.
- Lami adds a Dell XPS Laptop for 1200000 Naira in the "laptops" department.
- Chinedu adds Wireless Earbuds for 50000 Naira in the "accessories" department.
- Tobi changes his mind and removes the iPhone from the cart.
- Lami then adds another accessory: a Gaming Mouse for 35000 Naira.

At checkout:
- A snapshot of the nested cart is taken as the order summary for the store record.
- The shared smart cart is then completely emptied to reset for the next customers.
"""

# Shared smart cart with departments
cart = {
    "phones": {},
    "laptops": {},
    "accessories": {}
}

# Products as tuples (name, price)
iphone = ("iPhone", 750000)
dell_xps = ("Dell XPS Laptop", 1200000)
earbuds = ("Wireless Earbuds", 50000)
gaming_mouse = ("Gaming Mouse", 35000)

# Shopping actions

# Tobi picks up an iPhone
cart["phones"][iphone] = "Tobi"
print("Tobi added:", iphone, "to phones")
print("\n Cart>>>>>:", cart)

# Lami adds a Dell XPS Laptop
cart["laptops"][dell_xps] = "Lami"
print("Lami added:", dell_xps, "to laptops")
print("\n Cart>>>>:", cart)

# Chinedu adds Wireless Earbuds
cart["accessories"][earbuds] = "Chinedu"
print("Chinedu added:", earbuds, "to accessories")
print("\n Cart>>>>>", cart)

# Tobi changes his mind and removes the iPhone
removed_item = cart["phones"].pop(iphone)
print("Tobi removed:", iphone)
print(removed_item)

# Lami adds Gaming Mouse
cart["accessories"][gaming_mouse] = "Lami"
print("Lami added:", gaming_mouse, "to accessories")
print("\n Cart>>>>", cart)

# Show the final state of the nested cart
print("\n Final Smart Cart:", cart)

cart.clear()
print(cart)
