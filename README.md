
Order Processing System

This project provides a simple yet effective order processing system designed to manage customer and item records based on incoming order data. The main functionality is encapsulated in the `process_orders.py` script. which reads order information from a JSON file and updates records for customers and items accordingly. Then outputs these records into separate JSON files for further use.

Features

Order Processing**: Efficiently processes orders from a JSON file in extracting relevant information such as customer details and item orders.
Customer Record Management**: Maintains a comprehensive record of customers which is indexed by their phone numbers and updates this record with each processed order.
Item Record Tracking**: Keeps track of items ordered including the total number of orders per item and the price of each item.
Data Output: Outputs updated customer and item records into separate readable JSON files (`customers.json` and `items.json`).

How It Works

The script `process_orders.py` performs the following operations:

1. Reads order data from a specified JSON file, where each order includes the customer's phone number, optional customer name, and a list of items ordered.
2. Updates a dictionary of customers with the customer's phone number as the key. If the customer's name is not provided, it defaults to 'Unknown'.
3. Updates a dictionary of items, where each item's name is the key, and the value is a dictionary containing the item's price and the total number of orders for that item.
4. Outputs the updated customer and item records to `customers.json` and `items.json`, respectively.

Usage

To use this script, you need to have Python installed on your system. Then, you can process an orders file by running:

python process_orders.py <path_to_orders_json_file>


For example:


python process_orders.py orders.json


This command will process the orders in `orders.json`, update the records for customers and items, and save these records to `customers.json` and `items.json`.

Design

The project is designed with simplicity and modularity in mind, making it easy to integrate into larger systems or to be used as a standalone tool for order processing tasks. It consists of two main functions:

`process_orders(file_name)`: Processes the orders from the given file and updates the customer and item records.
`write_json(file_name, data)`: Outputs the specified data to a JSON file with the given filename.




