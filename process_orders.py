import json
import sys

def process_orders(file_name):
    with open(file_name, 'r') as file:
        orders = json.load(file)

    customers = {}
    items = {}

    for order in orders:
        # Update customers dictionary
        phone = order['phone']
        name = order.get('customer', 'Unknown')

        customers[phone] = name

        # Update items dictionary
        for item in order['items']:
            item_name = item['name']
            item_price = item['price']
            if item_name in items:
                items[item_name]['orders'] += 1
            else:
                items[item_name] = {'price': item_price, 'orders': 1}

    return customers, items

def write_json(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    if len(sys.argv) != 2:
        print("Usage: python process_orders.py <filename>")
        sys.exit(1)

    file_name = sys.argv[1]
    customers, items = process_orders(file_name)

    write_json('customers.json', customers)
    write_json('items.json', items)

if __name__ == "__main__":
    main()
