## 前置条件

> ROS2 Humble Desktop，参考 



创建项目

```shell
ros2 pkg create shop_simulation --build-type ament_python --dependencies rclpy std_msgs
```

给予执行权限

```shell
chmod +x shop_simulation/shop_simulation/*.py
```

运行结果示例（发布者）：

```
[INFO] [shop_messager]: 
New Transaction at 14:25:36
Customer: Bob
Product: Eggs
Quantity: 3
Total: $10.47
-------------------------
```

运行结果示例（订阅者）：

> [INFO] [shop_receiver]: RECEIVED: Bob bought 3x Eggs for $10.47
>
> Running Totals: 3 items sold, Total Sales: $10.47





