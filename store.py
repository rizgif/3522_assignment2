# You may need to import additional modules or classes, for example, a Factory class.
# from factory import Factory

class Store:
    def __init__(self):
        self.inventory = {}  # A dictionary to keep track of items in stock
        self.transactions = []  # A list to record transactions for the daily report

    def process_order(self, order):
        # Assuming 'order' is a dictionary with order details
        product_id = order['Product ID']
        quantity = order['Quantity']

        if self.check_and_update_inventory(product_id, quantity):
            # If the item is in stock and the required quantity is available,
            # add the transaction to the record.
            self.transactions.append(order)
        else:
            # If not enough stock, order more from the factory.
            self.order_items_from_factory(order)

    def check_and_update_inventory(self, product_id, quantity):
        # Check if the item exists and has enough stock
        if product_id in self.inventory and self.inventory[product_id]['quantity'] >= quantity:
            self.inventory[product_id]['quantity'] -= quantity
            return True
        else:
            # Item not in stock or not enough quantity
            return False

    def order_items_from_factory(self, order):
        product_id = order['Product ID']
        # We order 100 of the item as per the assignment's instruction
        # This will require a Factory class with a method like 'create_item'.
        new_items = Factory.create_item(product_id, 100)

        # Add the new items to the inventory
        self.inventory[product_id] = {
            'quantity': 100,
            'details': new_items  # This should be the item details as per your Factory implementation
        }

        # After ordering, process the order again
        self.process_order(order)

    def generate_daily_transaction_report(self):
        from datetime import datetime
        now = datetime.now()
        report_filename = f"DTR_{now.strftime('%d%m%y_%H%M')}.txt"

        with open(report_filename, 'w') as report_file:
            # Header for the daily transaction report
            report_file.write("HOLIDAY STORE - DAILY TRANSACTION REPORT\n")
            report_file.write(now.strftime("%d-%m-%Y %H:%M\n"))

            # Detail of each transaction
            for transaction in self.transactions:
                line = f"Order {transaction['Order number']}, Item {transaction['Item']}, Product ID {transaction['Product ID']}, Quantity {transaction['Quantity']}\n"
                report_file.write(line)

            # In case there were errors, you could log those too
            # For example, if there was an error processing an order, you could have:
            # report_file.write(f"Order {error_order_number}, Could not process order, Error: {error_reason}\n")

        print(f"Daily Transaction Report saved as {report_filename}")
