groceries = {}

while True:
    product = input("Item and quantity: ").lower()
    if product == "":
        break
    parts = product.split()
    item = parts[0]

    try:
        quantity = int(parts[1])
    except:
        print("Provide an item and quantity")
        quantity = 0

    if item in groceries:
        groceries[item] = groceries[item] + quantity
    elif quantity > 0:
        groceries[item] = quantity

print(groceries)
