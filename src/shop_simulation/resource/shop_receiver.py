#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from shop_simulation.msg import Shop

class ShopReceiver(Node):
    def __init__(self):
        super().__init__('shop_receiver')
        self.subscription = self.create_subscription(
            Shop,
            'shop_topic',
            self.listener_callback,
            10)
        self.subscription  # Prevent unused variable warning
        self.total_sales = 0.0
        self.total_items = 0
        
        self.get_logger().info("Shop Receiver started. Waiting for messages...")

    def listener_callback(self, msg):
        transaction_total = msg.price * msg.quantity
        self.total_sales += transaction_total
        self.total_items += msg.quantity
        
        self.get_logger().info(f"RECEIVED: {msg.customer_name} bought {msg.quantity}x {msg.product_name} "
                             f"for ${transaction_total:.2f}\n"
                             f"Running Totals: {self.total_items} items sold, "
                             f"Total Sales: ${self.total_sales:.2f}\n"
                             "========================")

def main(args=None):
    rclpy.init(args=args)
    node = ShopReceiver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shop Receiver stopped.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()