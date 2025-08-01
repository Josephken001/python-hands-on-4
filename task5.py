"""
Task 5: Online Shopping Cart
Two friends, Daniella and Godiya, walk into a mall and pick up just one cart to shop with.
Once inside, they split up and go to different wings of the mall, 
but since they share the same cart, everything either of them adds goes into the same cart.

cart = {}
godiya = ???
daniella = ???

During shopping:
- Daniella finds and adds "Shoes" (2 quantity).
- Godiya picks up "Watch" (1 quantity).
- Daniella later changes her mind and removes "Shoes" from the cart.
- Godiya also adds a "Bag" (1 quantity), then later removes it.

At checkout:
- The store takes a snapshot of the final order as an order summary for records.
- The shared cart is then emptied to prepare it for the next customer.
"""


# print(godiya)
# print(daniella)
# print(godiya == daniella) # should return true
# print(summary_of_cart)
# print(cart)

# Shared cart

cart = {}

godiya = cart
daniella = cart

print(id(cart))
print(id(daniella))
print(id(godiya))


# Daniella adds "Shoes" (2 quantity)
daniella["Shoes"] = 2
print("Daniella added:", {"Shoes": 2})

# Godiya adds "Watch" (1 quantity)
godiya["Watch"] = 1
print("Godiya added:", {"Watch": 1})
print("Cart>>>>>>: ", cart)

# Daniella removes "Shoes"
removed_shoes = daniella.pop("Shoes")
print("Daniella removed:", {"Shoes": removed_shoes})
print("Cart>>>>>: ", cart)

# Godiya adds "Bag" (1 quantity)
godiya["Bag"] = 1
print("Godiya added:", {"Bag": 1})
print("Cart>>>>>>: ", cart)

# Godiya removes "Bag"
removed_bag = godiya.pop("Bag")
print("Godiya removed:", {"Bag": removed_bag})
print("Cart>>>>>: ", cart)

# Store takes a snapshot of the final order
order_summary = cart.copy()
print("\n Order Summary:", order_summary)

print(godiya == daniella) # should return true

# Empty the shared cart for the next customer
cart.clear()
print("Cart after checkout:", cart)

