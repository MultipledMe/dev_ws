#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from shop_simulation.msg import Shop
import random
from datetime import datetime


class ShopMessager(Node):
    def __init__(self):
        super().__init__('shop_messager')
        self.publisher_ = self.create_publisher(Shop, 'shop_topic', 10)
        self.timer = self.create_timer(2.0, self.publish_message)
        self.products = [
            ("Milk", 2.99),
            ("Bread", 1.99),
            ("Eggs", 3.49),
            ("Apples", 4.99),
            ("Chicken", 5.99)
        ]
        self.customers = ["Alice", "Bob", "Charlie", "Diana", "Evan"]
        
        self.get_logger().info("Shop Messager started. Publishing messages...")

    def publish_message(self):
        msg = Shop()
        product = random.choice(self.products)
        msg.product_name = product[0]
        msg.price = product[1]
        msg.quantity = random.randint(1, 5)
        msg.customer_name = random.choice(self.customers)
        
        # Add timestamp
        now = datetime.now()
        self.get_logger().info(f"\nNew Transaction at {now.strftime('%H:%M:%S')}\n"
                             f"Customer: {msg.customer_name}\n"
                             f"Product: {msg.product_name}\n"
                             f"Quantity: {msg.quantity}\n"
                             f"Total: ${msg.price * msg.quantity:.2f}\n"
                             "-------------------------")
        
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ShopMessager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shop Messager stopped.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()