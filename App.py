def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

def apply_discount(total, discount_percent):
    discount = total * (discount_percent / 100)
    return total - discount

def process_order(items, discount_percent=0):
    total = calculate_total(items)
    if discount_percent > 0:
        total = apply_discount(total, discount_percent)
    return round(total, 2)

def apply_refund(total):
    return total - total
