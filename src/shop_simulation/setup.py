from setuptools import find_packages, setup

package_name = 'shop_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'messager = shop_simulation.shop_messager:main',
        'receiver = shop_simulation.shop_receiver:main',
    ],
    'rosidl_interface': ['msg/Shop.msg = shop_simulation.msg:Shop']
},
)
