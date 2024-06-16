from wsgi import app, db, Videocard, Motherboard, PowerSupplyUnit, RAM, HardDrive, Case, Keyboard, Mouse, Monitor, CoolingSystem, Processor
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'Database.db')
db = SQLAlchemy(app)


with app.app_context():
    # Заполнение таблицы Videocard
    videocard_data = [
        {"name": "NVIDIA GeForce RTX 3080", "manufacturer": "NVIDIA", "interface": "PCI Express 4.0", "price": 699, "chipset_brand": "NVIDIA", "core_clock": 1440, "boost_clock": 1710, "vram_type": "GDDR6X", "vram_capacity": "10GB"},
        {"name": "AMD Radeon RX 6800 XT", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 649, "chipset_brand": "AMD", "core_clock": 1825, "boost_clock": 2250, "vram_type": "GDDR6", "vram_capacity": "16GB"},
        {"name": "NVIDIA GeForce RTX 3070", "manufacturer": "NVIDIA", "interface": "PCI Express 4.0", "price": 499, "chipset_brand": "NVIDIA", "core_clock": 1500, "boost_clock": 1725, "vram_type": "GDDR6", "vram_capacity": "8GB"},
        {"name": "AMD Radeon RX 6700 XT", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 479, "chipset_brand": "AMD", "core_clock": 2424, "boost_clock": 2581, "vram_type": "GDDR6", "vram_capacity": "12GB"},
        {"name": "NVIDIA GeForce GTX 1660 Ti", "manufacturer": "NVIDIA", "interface": "PCI Express 3.0", "price": 279, "chipset_brand": "NVIDIA", "core_clock": 1500, "boost_clock": 1770, "vram_type": "GDDR6", "vram_capacity": "6GB"},
        {"name": "AMD Radeon RX 5700 XT", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 399, "chipset_brand": "AMD", "core_clock": 1605, "boost_clock": 1905, "vram_type": "GDDR6", "vram_capacity": "8GB"},
        {"name": "NVIDIA GeForce GTX 1650", "manufacturer": "NVIDIA", "interface": "PCI Express 3.0", "price": 149, "chipset_brand": "NVIDIA", "core_clock": 1485, "boost_clock": 1665, "vram_type": "GDDR6", "vram_capacity": "4GB"},
        {"name": "AMD Radeon RX 5600 XT", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 279, "chipset_brand": "AMD", "core_clock": 1375, "boost_clock": 1560, "vram_type": "GDDR6", "vram_capacity": "6GB"},
        {"name": "NVIDIA GeForce RTX 3090", "manufacturer": "NVIDIA", "interface": "PCI Express 4.0", "price": 1499, "chipset_brand": "NVIDIA", "core_clock": 1395, "boost_clock": 1695, "vram_type": "GDDR6X", "vram_capacity": "24GB"},
        {"name": "AMD Radeon RX 6900 XT", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 999, "chipset_brand": "AMD", "core_clock": 2015, "boost_clock": 2250, "vram_type": "GDDR6", "vram_capacity": "16GB"},
        {"name": "NVIDIA GeForce RTX 3060", "manufacturer": "NVIDIA", "interface": "PCI Express 4.0", "price": 329, "chipset_brand": "NVIDIA", "core_clock": 1320, "boost_clock": 1777, "vram_type": "GDDR6", "vram_capacity": "12GB"},
        {"name": "AMD Radeon RX 6600 XT", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 379, "chipset_brand": "AMD", "core_clock": 1968, "boost_clock": 2359, "vram_type": "GDDR6", "vram_capacity": "8GB"},
        {"name": "NVIDIA GeForce GTX 1050 Ti", "manufacturer": "NVIDIA", "interface": "PCI Express 3.0", "price": 169, "chipset_brand": "NVIDIA", "core_clock": 1290, "boost_clock": 1392, "vram_type": "GDDR5", "vram_capacity": "4GB"},
        {"name": "AMD Radeon RX 5500 XT", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 229, "chipset_brand": "AMD", "core_clock": 1607, "boost_clock": 1845, "vram_type": "GDDR6", "vram_capacity": "8GB"},
        {"name": "NVIDIA GeForce RTX 3060 Ti", "manufacturer": "NVIDIA", "interface": "PCI Express 4.0", "price": 399, "chipset_brand": "NVIDIA", "core_clock": 1410, "boost_clock": 1665, "vram_type": "GDDR6", "vram_capacity": "8GB"},
        {"name": "AMD Radeon RX 6700", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 479, "chipset_brand": "AMD", "core_clock": 2321, "boost_clock": 2424, "vram_type": "GDDR6", "vram_capacity": "12GB"},
        {"name": "NVIDIA GeForce GTX 1660 Super", "manufacturer": "NVIDIA", "interface": "PCI Express 3.0", "price": 239, "chipset_brand": "NVIDIA", "core_clock": 1530, "boost_clock": 1785, "vram_type": "GDDR6", "vram_capacity": "6GB"},
        {"name": "AMD Radeon RX 5600", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 279, "chipset_brand": "AMD", "core_clock": 1130, "boost_clock": 1560, "vram_type": "GDDR6", "vram_capacity": "6GB"},
        {"name": "NVIDIA GeForce GTX 1650 Super", "manufacturer": "NVIDIA", "interface": "PCI Express 3.0", "price": 159, "chipset_brand": "NVIDIA", "core_clock": 1530, "boost_clock": 1725, "vram_type": "GDDR6", "vram_capacity": "4GB"},
        {"name": "AMD Radeon RX 550", "manufacturer": "AMD", "interface": "PCI Express 3.0", "price": 129, "chipset_brand": "AMD", "core_clock": 1100, "boost_clock": 1183, "vram_type": "GDDR5", "vram_capacity": "4GB"},
        {"name": "NVIDIA GeForce GT 1030", "manufacturer": "NVIDIA", "interface": "PCI Express 3.0", "price": 89, "chipset_brand": "NVIDIA", "core_clock": 1227, "boost_clock": 1468, "vram_type": "GDDR5", "vram_capacity": "2GB"},
        {"name": "AMD Radeon RX 5300", "manufacturer": "AMD", "interface": "PCI Express 4.0", "price": 149, "chipset_brand": "AMD", "core_clock": 1168, "boost_clock": 1448, "vram_type": "GDDR6", "vram_capacity": "3GB"},
        {"name": "NVIDIA GeForce GTX 1050", "manufacturer": "NVIDIA", "interface": "PCI Express 3.0", "price": 139, "chipset_brand": "NVIDIA", "core_clock": 1354, "boost_clock": 1455, "vram_type": "GDDR5", "vram_capacity": "2GB"},
        {"name": "AMD Radeon RX 550X", "manufacturer": "AMD", "interface": "PCI Express 3.0", "price": 129, "chipset_brand": "AMD", "core_clock": 1183, "boost_clock": 1287, "vram_type": "GDDR5", "vram_capacity": "4GB"}
    ]

    for data in videocard_data:
        videocard = Videocard(**data)
        db.session.add(videocard)

    # Заполнение таблицы Processor
    processor_data = [
        {"name": "Intel Core i9-11900K", "manufacturer": "Intel", "cores": 8, "threads": 16, "base_clock": 3.5, "boost_clock": 5.3, "socket": "LGA 1200", "price": 539.99, "tdp": 125},
        {"name": "AMD Ryzen 9 5950X", "manufacturer": "AMD", "cores": 16, "threads": 32, "base_clock": 3.4, "boost_clock": 4.9, "socket": "AM4", "price": 799.99, "tdp": 105},
        {"name": "Intel Core i7-11700K", "manufacturer": "Intel", "cores": 8, "threads": 16, "base_clock": 3.6, "boost_clock": 5.0, "socket": "LGA 1200", "price": 399.99, "tdp": 125},
        {"name": "AMD Ryzen 7 5800X", "manufacturer": "AMD", "cores": 8, "threads": 16, "base_clock": 3.8, "boost_clock": 4.7, "socket": "AM4", "price": 449.99, "tdp": 105},
        {"name": "Intel Core i5-11600K", "manufacturer": "Intel", "cores": 6, "threads": 12, "base_clock": 3.9, "boost_clock": 4.9, "socket": "LGA 1200", "price": 269.99, "tdp": 125},
        {"name": "AMD Ryzen 5 5600X", "manufacturer": "AMD", "cores": 6, "threads": 12, "base_clock": 3.7, "boost_clock": 4.6, "socket": "AM4", "price": 299.99, "tdp": 65},
        {"name": "Intel Core i9-10900K", "manufacturer": "Intel", "cores": 10, "threads": 20, "base_clock": 3.7, "boost_clock": 5.3, "socket": "LGA 1200", "price": 529.99, "tdp": 125},
        {"name": "AMD Ryzen 9 5900X", "manufacturer": "AMD", "cores": 12, "threads": 24, "base_clock": 3.7, "boost_clock": 4.8, "socket": "AM4", "price": 549.99, "tdp": 105},
        {"name": "Intel Core i5-10600K", "manufacturer": "Intel", "cores": 6, "threads": 12, "base_clock": 4.1, "boost_clock": 4.8, "socket": "LGA 1200", "price": 319.99, "tdp": 125},
        {"name": "AMD Ryzen 7 5800", "manufacturer": "AMD", "cores": 8, "threads": 16, "base_clock": 3.4, "boost_clock": 4.6, "socket": "AM4", "price": 349.99, "tdp": 65},
        {"name": "Intel Core i7-10700K", "manufacturer": "Intel", "cores": 8, "threads": 16, "base_clock": 3.8, "boost_clock": 5.1, "socket": "LGA 1200", "price": 399.99, "tdp": 125},
        {"name": "AMD Ryzen 5 5600", "manufacturer": "AMD", "cores": 6, "threads": 12, "base_clock": 3.6, "boost_clock": 4.6, "socket": "AM4", "price": 219.99, "tdp": 65},
        {"name": "Intel Core i5-10600KF", "manufacturer": "Intel", "cores": 6, "threads": 12, "base_clock": 4.1, "boost_clock": 4.8, "socket": "LGA 1200", "price": 269.99, "tdp": 125},
        {"name": "AMD Ryzen 7 5700G", "manufacturer": "AMD", "cores": 8, "threads": 16, "base_clock": 3.8, "boost_clock": 4.6, "socket": "AM4", "price": 359.99, "tdp": 65},
        {"name": "Intel Core i9-9900K", "manufacturer": "Intel", "cores": 8, "threads": 16, "base_clock": 3.6, "boost_clock": 5.0, "socket": "LGA 1151", "price": 359.99, "tdp": 95},
        {"name": "AMD Ryzen 5 5500G", "manufacturer": "AMD", "cores": 6, "threads": 12, "base_clock": 3.8, "boost_clock": 4.4, "socket": "AM4", "price": 189.99, "tdp": 65},
        {"name": "Intel Core i3-10100F", "manufacturer": "Intel", "cores": 4, "threads": 8, "base_clock": 3.6, "boost_clock": 4.3, "socket": "LGA 1200", "price": 99.99, "tdp": 65},
        {"name": "AMD Ryzen 3 5300G", "manufacturer": "AMD", "cores": 4, "threads": 8, "base_clock": 4.0, "boost_clock": 4.2, "socket": "AM4", "price": 149.99, "tdp": 65},
        {"name": "Intel Core i7-9700K", "manufacturer": "Intel", "cores": 8, "threads": 8, "base_clock": 3.6, "boost_clock": 4.9, "socket": "LGA 1151", "price": 299.99, "tdp": 95},
        {"name": "AMD Ryzen 5 3400G", "manufacturer": "AMD", "cores": 4, "threads": 8, "base_clock": 3.7, "boost_clock": 4.2, "socket": "AM4", "price": 149.99, "tdp": 65},
        {"name": "Intel Core i5-10400F", "manufacturer": "Intel", "cores": 6, "threads": 12, "base_clock": 2.9, "boost_clock": 4.3, "socket": "LGA 1200", "price": 159.99, "tdp": 65},
        {"name": "AMD Ryzen 3 3200G", "manufacturer": "AMD", "cores": 4, "threads": 4, "base_clock": 3.6, "boost_clock": 4.0, "socket": "AM4", "price": 99.99, "tdp": 65},
        {"name": "Intel Core i3-10100", "manufacturer": "Intel", "cores": 4, "threads": 8, "base_clock": 3.6, "boost_clock": 4.3, "socket": "LGA 1200", "price": 119.99, "tdp": 65},
        {"name": "AMD Ryzen 3 3100", "manufacturer": "AMD", "cores": 4, "threads": 8, "base_clock": 3.6, "boost_clock": 3.9, "socket": "AM4", "price": 129.99, "tdp": 65},
        {"name": "Intel Core i5-9600K", "manufacturer": "Intel", "cores": 6, "threads": 6, "base_clock": 3.7, "boost_clock": 4.6, "socket": "LGA 1151", "price": 219.99, "tdp": 95},
        {"name": "AMD Ryzen 3 3100X", "manufacturer": "AMD", "cores": 4, "threads": 8, "base_clock": 3.9, "boost_clock": 4.3, "socket": "AM4", "price": 119.99, "tdp": 65},
        {"name": "Intel Core i5-9400F", "manufacturer": "Intel", "cores": 6, "threads": 6, "base_clock": 2.9, "boost_clock": 4.1, "socket": "LGA 1151", "price": 159.99, "tdp": 65},
        {"name": "AMD Ryzen 3 3200", "manufacturer": "AMD", "cores": 4, "threads": 4, "base_clock": 3.6, "boost_clock": 4.0, "socket": "AM4", "price": 99.99, "tdp": 65},
        {"name": "Intel Core i3-9100F", "manufacturer": "Intel", "cores": 4, "threads": 4, "base_clock": 3.6, "boost_clock": 4.2, "socket": "LGA 1151", "price": 79.99, "tdp": 65},
        {"name": "AMD Ryzen 3 3100G", "manufacturer": "AMD", "cores": 4, "threads": 8, "base_clock": 3.8, "boost_clock": 4.2, "socket": "AM4", "price": 109.99, "tdp": 45},
        {"name": "Intel Core i3-10100T", "manufacturer": "Intel", "cores": 4, "threads": 8, "base_clock": 3.0, "boost_clock": 3.8, "socket": "LGA 1200", "price": 89.99, "tdp": 35},
        {"name": "AMD Ryzen 3 3200GE", "manufacturer": "AMD", "cores": 4, "threads": 4, "base_clock": 3.3, "boost_clock": 3.8, "socket": "AM4", "price": 109.99, "tdp": 35},
        {"name": "Intel Core i3-10105F", "manufacturer": "Intel", "cores": 4, "threads": 8, "base_clock": 3.7, "boost_clock": 4.4, "socket": "LGA 1200", "price": 99.99, "tdp": 65}
    ]

    for data in processor_data:
        processor = Processor(**data)
        db.session.add(processor)


    # Заполнение таблицы Motherboard
    motherboard_data = [
        {"name": "ASUS ROG Strix B550-F Gaming", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 189, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "B550"},
        {"name": "GIGABYTE Z490 AORUS ELITE AC", "manufacturer": "GIGABYTE", "socket": "LGA 1200", "form_factor": "ATX", "price": 199, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "Z490"},
        {"name": "MSI MPG B550 Gaming Plus", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 159, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "B550"},
        {"name": "ASRock B450M Steel Legend", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "Micro ATX", "price": 99, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "GIGABYTE X570 AORUS Elite", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "ATX", "price": 199, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "X570"},
        {"name": "ASUS Prime X570-P", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 169, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "MSI B450 TOMAHAWK MAX", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 114, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "ASRock B550M PRO4", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "Micro ATX", "price": 89, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "B550"},
        {"name": "ASUS ROG Strix X570-E Gaming", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 299, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "GIGABYTE B450 AORUS Elite", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "ATX", "price": 119, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "ASUS ROG Crosshair VIII Hero", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 379, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "MSI MAG B550M Bazooka", "manufacturer": "MSI", "socket": "AM4", "form_factor": "Micro ATX", "price": 129, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 1, "chipset": "B550"},
        {"name": "ASRock X570 Phantom Gaming 4", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "ATX", "price": 169, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "X570"},
        {"name": "GIGABYTE B550 AORUS Elite", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "ATX", "price": 159, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "B550"},
        {"name": "ASUS TUF Gaming X570-Plus", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 189, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "X570"},
        {"name": "MSI B550-A Pro", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 139, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "B550"},
        {"name": "ASRock B550 Phantom Gaming 4", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "ATX", "price": 119, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "B550"},
        {"name": "GIGABYTE B550M DS3H", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "Micro ATX", "price": 79, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 1, "chipset": "B550"},
        {"name": "ASUS ROG Crosshair VIII Dark Hero", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 399, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 4, "chipset": "X570"},
        {"name": "MSI MAG X570 Tomahawk WiFi", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 279, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "ASRock X570 Steel Legend", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "ATX", "price": 199, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "X570"},
        {"name": "GIGABYTE B450 AORUS M", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "Micro ATX", "price": 89, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "B450"},
        {"name": "ASUS ROG Strix B450-F Gaming", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 129, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "MSI B450 Gaming Plus Max", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 99, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "ASRock B450M-HDV R4.0", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "Micro ATX", "price": 69, "memory_type_support": "DDR4", "memory_slots": 2, "max_memory": "32GB", "pci_express_slots": 1, "chipset": "B450"},
        {"name": "GIGABYTE B450M DS3H", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "Micro ATX", "price": 79, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "B450"},
        {"name": "ASUS Prime B450M-A/CSM", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "Micro ATX", "price": 74, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "B450"},
        {"name": "MSI B450-A Pro Max", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 99, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "ASRock B550M-ITX/ac", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "Mini ITX", "price": 149, "memory_type_support": "DDR4", "memory_slots": 2, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "B550"},
        {"name": "GIGABYTE X570 I AORUS PRO WIFI", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "Mini ITX", "price": 219, "memory_type_support": "DDR4", "memory_slots": 2, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "X570"},
        {"name": "ASUS ROG Strix B550-I Gaming", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "Mini ITX", "price": 229, "memory_type_support": "DDR4", "memory_slots": 2, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "B550"},
        {"name": "MSI MPG B550I Gaming Edge WiFi", "manufacturer": "MSI", "socket": "AM4", "form_factor": "Mini ITX", "price": 199, "memory_type_support": "DDR4", "memory_slots": 2, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "B550"},
        {"name": "ASRock X570M Pro4", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "Micro ATX", "price": 189, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "X570"},
        {"name": "GIGABYTE B450M S2H", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "Micro ATX", "price": 59, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "B450"},
        {"name": "ASUS TUF Gaming B550M-PLUS", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "Micro ATX", "price": 139, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "B550"},
        {"name": "MSI MAG B550M Mortar WiFi", "manufacturer": "MSI", "socket": "AM4", "form_factor": "Micro ATX", "price": 149, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "B550"},
        {"name": "ASRock X570M Pro4", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "Micro ATX", "price": 189, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "X570"},
        {"name": "GIGABYTE B450 AORUS PRO WIFI", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "ATX", "price": 129, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "ASUS ROG Strix X570-I Gaming", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "Mini ITX", "price": 299, "memory_type_support": "DDR4", "memory_slots": 2, "max_memory": "64GB", "pci_express_slots": 1, "chipset": "X570"},
        {"name": "MSI MPG X570 GAMING PLUS", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 189, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 2, "chipset": "X570"},
        {"name": "ASRock B450M Pro4", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "Micro ATX", "price": 79, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "64GB", "pci_express_slots": 2, "chipset": "B450"},
        {"name": "GIGABYTE B550 AORUS PRO", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "ATX", "price": 179, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "B550"},
        {"name": "ASUS Prime B550-PLUS", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 149, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "B550"},
        {"name": "MSI MAG B550 Tomahawk", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 179, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "B550"},
        {"name": "ASRock X570 Taichi", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "ATX", "price": 299, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "GIGABYTE X570 AORUS PRO", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "ATX", "price": 249, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "ASUS TUF Gaming X570-PRO", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 219, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "MSI MEG X570 ACE", "manufacturer": "MSI", "socket": "AM4", "form_factor": "ATX", "price": 379, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "X570"},
        {"name": "ASRock B550 Extreme4", "manufacturer": "ASRock", "socket": "AM4", "form_factor": "ATX", "price": 179, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "B550"},
        {"name": "GIGABYTE B550 AORUS MASTER", "manufacturer": "GIGABYTE", "socket": "AM4", "form_factor": "ATX", "price": 279, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 3, "chipset": "B550"},
        {"name": "ASUS ROG Crosshair VIII Formula", "manufacturer": "ASUS", "socket": "AM4", "form_factor": "ATX", "price": 749, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 4, "chipset": "X570"},
        {"name": "MSI MEG X570 GODLIKE", "manufacturer": "MSI", "socket": "AM4", "form_factor": "E-ATX", "price": 799, "memory_type_support": "DDR4", "memory_slots": 4, "max_memory": "128GB", "pci_express_slots": 4, "chipset": "X570"}
    ]

    for data in motherboard_data:
        motherboard = Motherboard(**data)
        db.session.add(motherboard)

    # Заполнение таблицы PowerSupplyUnit
    power_supply_data = [
        {"name": "Corsair RM750x", "manufacturer": "Corsair", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 129.99, "modular": True},
        {"name": "EVGA SuperNOVA 750 G5", "manufacturer": "EVGA", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 129.99, "modular": True},
        {"name": "Seasonic Focus GX-650", "manufacturer": "Seasonic", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 109.99, "modular": True},
        {"name": "NZXT C850", "manufacturer": "NZXT", "wattage": 850, "efficiency_rating": "80 Plus Gold", "price": 149.99, "modular": True},
        {"name": "be quiet! Straight Power 11 750W", "manufacturer": "be quiet!", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 139.90, "modular": True},
        {"name": "Corsair CX650F RGB", "manufacturer": "Corsair", "wattage": 650, "efficiency_rating": "80 Plus Bronze", "price": 89.99, "modular": True},
        {"name": "Thermaltake Toughpower GF1 750W", "manufacturer": "Thermaltake", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 139.99, "modular": True},
        {"name": "EVGA 600 BQ", "manufacturer": "EVGA", "wattage": 600, "efficiency_rating": "80 Plus Bronze", "price": 64.99, "modular": False},
        {"name": "Seasonic S12III 550W", "manufacturer": "Seasonic", "wattage": 550, "efficiency_rating": "80 Plus Bronze", "price": 64.99, "modular": False},
        {"name": "Cooler Master MWE 650 White V2", "manufacturer": "Cooler Master", "wattage": 650, "efficiency_rating": "80 Plus White", "price": 64.99, "modular": False},
        {"name": "EVGA SuperNOVA 850 G5", "manufacturer": "EVGA", "wattage": 850, "efficiency_rating": "80 Plus Gold", "price": 159.99, "modular": True},
        {"name": "be quiet! Pure Power 11 700W", "manufacturer": "be quiet!", "wattage": 700, "efficiency_rating": "80 Plus Gold", "price": 109.90, "modular": False},
        {"name": "Corsair TX650M", "manufacturer": "Corsair", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 89.99, "modular": True},
        {"name": "NZXT E650", "manufacturer": "NZXT", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 119.99, "modular": True},
        {"name": "Antec NeoECO Gold ZEN 700W", "manufacturer": "Antec", "wattage": 700, "efficiency_rating": "80 Plus Gold", "price": 94.99, "modular": False},
        {"name": "Cooler Master MWE 750 White V2", "manufacturer": "Cooler Master", "wattage": 750, "efficiency_rating": "80 Plus White", "price": 69.99, "modular": False},
        {"name": "Thermaltake Smart BX1 RGB 650W", "manufacturer": "Thermaltake", "wattage": 650, "efficiency_rating": "80 Plus Bronze", "price": 79.99, "modular": False},
        {"name": "GIGABYTE P750GM", "manufacturer": "GIGABYTE", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 119.99, "modular": True},
        {"name": "EVGA 850 BQ", "manufacturer": "EVGA", "wattage": 850, "efficiency_rating": "80 Plus Bronze", "price": 89.99, "modular": False},
        {"name": "be quiet! System Power 9 600W", "manufacturer": "be quiet!", "wattage": 600, "efficiency_rating": "80 Plus Bronze", "price": 69.90, "modular": False},
        {"name": "SilverStone ET650-B", "manufacturer": "SilverStone", "wattage": 650, "efficiency_rating": "80 Plus Bronze", "price": 74.99, "modular": False},
        {"name": "FSP Dagger Pro 650W", "manufacturer": "FSP", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 149.99, "modular": True},
        {"name": "Thermaltake Toughpower GX2 700W", "manufacturer": "Thermaltake", "wattage": 700, "efficiency_rating": "80 Plus Gold", "price": 99.99, "modular": True},
        {"name": "Cooler Master MWE 700 White V2", "manufacturer": "Cooler Master", "wattage": 700, "efficiency_rating": "80 Plus White", "price": 59.99, "modular": False},
        {"name": "SilverStone SX650-G", "manufacturer": "SilverStone", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 124.99, "modular": True},
        {"name": "FSP Hydro G PRO 850W", "manufacturer": "FSP", "wattage": 850, "efficiency_rating": "80 Plus Gold", "price": 129.99, "modular": True},
        {"name": "Antec EarthWatts Gold Pro 750W", "manufacturer": "Antec", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 119.99, "modular": True},
        {"name": "Rosewill Hive Series 750W", "manufacturer": "Rosewill", "wattage": 750, "efficiency_rating": "80 Plus Bronze", "price": 89.99, "modular": True},
        {"name": "BitFenix Whisper M 650W", "manufacturer": "BitFenix", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 114.99, "modular": True},
        {"name": "EVGA 700 GD", "manufacturer": "EVGA", "wattage": 700, "efficiency_rating": "80 Plus Gold", "price": 79.99, "modular": False},
        {"name": "Cooler Master MWE Gold 750 V2", "manufacturer": "Cooler Master", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 119.99, "modular": True},
        {"name": "Seasonic CORE GX-650", "manufacturer": "Seasonic", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 99.99, "modular": True},
        {"name": "GIGABYTE P650B", "manufacturer": "GIGABYTE", "wattage": 650, "efficiency_rating": "80 Plus Bronze", "price": 64.99, "modular": False},
        {"name": "Corsair CV650", "manufacturer": "Corsair", "wattage": 650, "efficiency_rating": "80 Plus Bronze", "price": 59.99, "modular": False},
        {"name": "EVGA SuperNOVA 650 GM", "manufacturer": "EVGA", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 119.99, "modular": True},
        {"name": "be quiet! Pure Power 11 FM 650W", "manufacturer": "be quiet!", "wattage": 650, "efficiency_rating": "80 Plus Gold", "price": 109.90, "modular": True},
        {"name": "NZXT C750", "manufacturer": "NZXT", "wattage": 750, "efficiency_rating": "80 Plus Gold", "price": 139.99, "modular": True},
        {"name": "Corsair TX850M", "manufacturer": "Corsair", "wattage": 850, "efficiency_rating": "80 Plus Gold", "price": 119.99, "modular": True},
        {"name": "EVGA 850 B5", "manufacturer": "EVGA", "wattage": 850, "efficiency_rating": "80 Plus Bronze", "price": 89.99, "modular": False}
]

    for data in power_supply_data:
        psu = PowerSupplyUnit(**data)
        db.session.add(psu)

    # Заполнение таблицы RAM
    ram_data = [
        {"name": "Corsair Vengeance LPX 16GB", "manufacturer": "Corsair", "capacity": "16GB", "speed": "3200MHz", "price": 79.99, "memory_type": "DDR4"},
        {"name": "G.Skill Trident Z RGB 16GB", "manufacturer": "G.Skill", "capacity": "16GB", "speed": "3600MHz", "price": 99.99, "memory_type": "DDR4"},
        {"name": "Kingston HyperX Fury 8GB", "manufacturer": "Kingston", "capacity": "8GB", "speed": "2666MHz", "price": 44.99, "memory_type": "DDR4"},
        {"name": "Corsair Dominator Platinum 32GB", "manufacturer": "Corsair", "capacity": "32GB", "speed": "3200MHz", "price": 199.99, "memory_type": "DDR4"},
        {"name": "Crucial Ballistix 16GB", "manufacturer": "Crucial", "capacity": "16GB", "speed": "3200MHz", "price": 79.99, "memory_type": "DDR4"},
        {"name": "Team T-Force Vulcan Z 16GB", "manufacturer": "Team Group", "capacity": "16GB", "speed": "3000MHz", "price": 74.99, "memory_type": "DDR4"},
        {"name": "Corsair Vengeance RGB Pro 32GB", "manufacturer": "Corsair", "capacity": "32GB", "speed": "3200MHz", "price": 184.99, "memory_type": "DDR4"},
        {"name": "Patriot Viper Steel 16GB", "manufacturer": "Patriot", "capacity": "16GB", "speed": "3200MHz", "price": 69.99, "memory_type": "DDR4"},
        {"name": "G.Skill Ripjaws V 16GB", "manufacturer": "G.Skill", "capacity": "16GB", "speed": "3200MHz", "price": 74.99, "memory_type": "DDR4"},
        {"name": "Kingston Fury Beast 32GB", "manufacturer": "Kingston", "capacity": "32GB", "speed": "3200MHz", "price": 189.99, "memory_type": "DDR4"},
        {"name": "Corsair Vengeance LPX 8GB", "manufacturer": "Corsair", "capacity": "8GB", "speed": "2400MHz", "price": 39.99, "memory_type": "DDR4"},
        {"name": "G.Skill Trident Z RGB 32GB", "manufacturer": "G.Skill", "capacity": "32GB", "speed": "3600MHz", "price": 219.99, "memory_type": "DDR4"},
        {"name": "Crucial Ballistix 32GB", "manufacturer": "Crucial", "capacity": "32GB", "speed": "3200MHz", "price": 164.99, "memory_type": "DDR4"},
        {"name": "Team T-Force Delta RGB 16GB", "manufacturer": "Team Group", "capacity": "16GB", "speed": "3200MHz", "price": 84.99, "memory_type": "DDR4"},
        {"name": "Corsair Dominator Platinum 16GB", "manufacturer": "Corsair", "capacity": "16GB", "speed": "3200MHz", "price": 99.99, "memory_type": "DDR4"},
        {"name": "Patriot Viper Steel 32GB", "manufacturer": "Patriot", "capacity": "32GB", "speed": "3200MHz", "price": 139.99, "memory_type": "DDR4"},
        {"name": "G.Skill Ripjaws V 32GB", "manufacturer": "G.Skill", "capacity": "32GB", "speed": "3200MHz", "price": 149.99, "memory_type": "DDR4"},
        {"name": "Kingston HyperX Fury 16GB", "manufacturer": "Kingston", "capacity": "16GB", "speed": "2400MHz", "price": 74.99, "memory_type": "DDR4"},
        {"name": "Corsair Vengeance RGB Pro 16GB", "manufacturer": "Corsair", "capacity": "16GB", "speed": "3200MHz", "price": 89.99, "memory_type": "DDR4"},
        {"name": "Crucial Ballistix RGB 16GB", "manufacturer": "Crucial", "capacity": "16GB", "speed": "3200MHz", "price": 89.99, "memory_type": "DDR4"},
        {"name": "Team T-Force Night Hawk 16GB", "manufacturer": "Team Group", "capacity": "16GB", "speed": "3000MHz", "price": 79.99, "memory_type": "DDR4"},
        {"name": "Corsair Dominator Platinum RGB 16GB", "manufacturer": "Corsair", "capacity": "16GB", "speed": "3200MHz", "price": 119.99, "memory_type": "DDR4"},
        {"name": "Patriot Viper Elite II 16GB", "manufacturer": "Patriot", "capacity": "16GB", "speed": "3200MHz", "price": 64.99, "memory_type": "DDR4"},
        {"name": "G.Skill Trident Z Neo 32GB", "manufacturer": "G.Skill", "capacity": "32GB", "speed": "3600MHz", "price": 249.99, "memory_type": "DDR4"},
        {"name": "Crucial Ballistix MAX 16GB", "manufacturer": "Crucial", "capacity": "16GB", "speed": "4000MHz", "price": 139.99, "memory_type": "DDR4"},
        {"name": "Team T-Force Vulcan 16GB", "manufacturer": "Team Group", "capacity": "16GB", "speed": "3200MHz", "price": 74.99, "memory_type": "DDR4"},
        {"name": "Corsair Vengeance LPX 32GB", "manufacturer": "Corsair", "capacity": "32GB", "speed": "2400MHz", "price": 159.99, "memory_type": "DDR4"},
        {"name": "G.Skill Trident Z Royal 16GB", "manufacturer": "G.Skill", "capacity": "16GB", "speed": "3200MHz", "price": 109.99, "memory_type": "DDR4"},
        {"name": "Kingston HyperX Predator 32GB", "manufacturer": "Kingston", "capacity": "32GB", "speed": "3200MHz", "price": 189.99, "memory_type": "DDR4"},
        {"name": "Corsair Vengeance RGB Pro 64GB", "manufacturer": "Corsair", "capacity": "64GB", "speed": "3200MHz", "price": 329.99, "memory_type": "DDR4"},
        {"name": "Crucial Ballistix Elite 16GB", "manufacturer": "Crucial", "capacity": "16GB", "speed": "3600MHz", "price": 109.99, "memory_type": "DDR4"},
        {"name": "Team T-Force Xtreem ARGB 16GB", "manufacturer": "Team Group", "capacity": "16GB", "speed": "3600MHz", "price": 124.99, "memory_type": "DDR4"},
        {"name": "Patriot Viper Steel RGB 16GB", "manufacturer": "Patriot", "capacity": "16GB", "speed": "3200MHz", "price": 94.99, "memory_type": "DDR4"},
        {"name": "G.Skill Ripjaws V 64GB", "manufacturer": "G.Skill", "capacity": "64GB", "speed": "3200MHz", "price": 279.99, "memory_type": "DDR4"},
        {"name": "Kingston Fury Renegade 16GB", "manufacturer": "Kingston", "capacity": "16GB", "speed": "3600MHz", "price": 99.99, "memory_type": "DDR4"},
        {"name": "Corsair Dominator Platinum 64GB", "manufacturer": "Corsair", "capacity": "64GB", "speed": "3200MHz", "price": 349.99, "memory_type": "DDR4"},
        {"name": "Crucial Ballistix MAX 32GB", "manufacturer": "Crucial", "capacity": "32GB", "speed": "4000MHz", "price": 279.99, "memory_type": "DDR4"},
        {"name": "Team T-Force Delta RGB 32GB", "manufacturer": "Team Group", "capacity": "32GB", "speed": "3200MHz", "price": 149.99, "memory_type": "DDR4"},
        {"name": "Patriot Viper Elite II 32GB", "manufacturer": "Patriot", "capacity": "32GB", "speed": "3200MHz", "price": 124.99, "memory_type": "DDR4"},
        {"name": "G.Skill Trident Z Neo 64GB", "manufacturer": "G.Skill", "capacity": "64GB", "speed": "3600MHz", "price": 449.99, "memory_type": "DDR4"},
        {"name": "Corsair Vengeance LPX 64GB", "manufacturer": "Corsair", "capacity": "64GB", "speed": "3600MHz", "price": 389.99, "memory_type": "DDR4"},
        {"name": "Crucial Ballistix RGB 32GB", "manufacturer": "Crucial", "capacity": "32GB", "speed": "3200MHz", "price": 169.99, "memory_type": "DDR4"},
        {"name": "Team T-Force Vulcan Z 32GB", "manufacturer": "Team Group", "capacity": "32GB", "speed": "3000MHz", "price": 139.99, "memory_type": "DDR4"},
        {"name": "Patriot Viper Steel 64GB", "manufacturer": "Patriot", "capacity": "64GB", "speed": "3200MHz", "price": 269.99, "memory_type": "DDR4"}
    ]

    for data in ram_data:
        ram = RAM(**data)
        db.session.add(ram)

    # Заполнение таблицы HardDrive
    hard_drive_data = [
        {"name": "Seagate BarraCuda 1TB", "manufacturer": "Seagate", "capacity": "1TB", "interface": "SATA", "price": 49.99, "form_factor": "3.5"},
        {"name": "Western Digital Blue 1TB", "manufacturer": "Western Digital", "capacity": "1TB", "interface": "SATA", "price": 45.99, "form_factor": "3.5"},
        {"name": "Toshiba P300 1TB", "manufacturer": "Toshiba", "capacity": "1TB", "interface": "SATA", "price": 44.99, "form_factor": "3.5"},
        {"name": "Seagate BarraCuda 2TB", "manufacturer": "Seagate", "capacity": "2TB", "interface": "SATA", "price": 69.99, "form_factor": "3.5"},
        {"name": "Western Digital Blue 2TB", "manufacturer": "Western Digital", "capacity": "2TB", "interface": "SATA", "price": 64.99, "form_factor": "3.5"},
        {"name": "Toshiba P300 2TB", "manufacturer": "Toshiba", "capacity": "2TB", "interface": "SATA", "price": 62.99, "form_factor": "3.5"},
        {"name": "Seagate IronWolf 4TB", "manufacturer": "Seagate", "capacity": "4TB", "interface": "SATA", "price": 119.99, "form_factor": "3.5"},
        {"name": "Western Digital Red 4TB", "manufacturer": "Western Digital", "capacity": "4TB", "interface": "SATA", "price": 109.99, "form_factor": "3.5"},
        {"name": "Toshiba N300 4TB", "manufacturer": "Toshiba", "capacity": "4TB", "interface": "SATA", "price": 114.99, "form_factor": "3.5"},
        {"name": "Seagate Exos X16 10TB", "manufacturer": "Seagate", "capacity": "10TB", "interface": "SATA", "price": 319.99, "form_factor": "3.5"},
        {"name": "Western Digital Gold 10TB", "manufacturer": "Western Digital", "capacity": "10TB", "interface": "SATA", "price": 299.99, "form_factor": "3.5"},
        {"name": "Toshiba MG07ACA 14TB", "manufacturer": "Toshiba", "capacity": "14TB", "interface": "SATA", "price": 399.99, "form_factor": "3.5"},
        {"name": "Seagate IronWolf Pro 18TB", "manufacturer": "Seagate", "capacity": "18TB", "interface": "SATA", "price": 539.99, "form_factor": "3.5"},
        {"name": "Western Digital Ultrastar DC HC550 18TB", "manufacturer": "Western Digital", "capacity": "18TB", "interface": "SATA", "price": 529.99, "form_factor": "3.5"},
        {"name": "Toshiba MG08ACA16TE 16TB", "manufacturer": "Toshiba", "capacity": "16TB", "interface": "SATA", "price": 479.99, "form_factor": "3.5"},
        {"name": "Seagate FireCuda 2TB", "manufacturer": "Seagate", "capacity": "2TB", "interface": "SATA", "price": 89.99, "form_factor": "3.5"},
        {"name": "Western Digital Black 2TB", "manufacturer": "Western Digital", "capacity": "2TB", "interface": "SATA", "price": 119.99, "form_factor": "3.5"},
        {"name": "Toshiba X300 4TB", "manufacturer": "Toshiba", "capacity": "4TB", "interface": "SATA", "price": 104.99, "form_factor": "3.5"},
        {"name": "Seagate BarraCuda 500GB", "manufacturer": "Seagate", "capacity": "500GB", "interface": "SATA", "price": 39.99, "form_factor": "3.5"},
        {"name": "Western Digital Blue 500GB", "manufacturer": "Western Digital", "capacity": "500GB", "interface": "SATA", "price": 37.99, "form_factor": "3.5"},
        {"name": "Toshiba L200 1TB", "manufacturer": "Toshiba", "capacity": "1TB", "interface": "SATA", "price": 54.99, "form_factor": "2.5"},
        {"name": "Seagate FireCuda 2TB", "manufacturer": "Seagate", "capacity": "2TB", "interface": "SATA", "price": 89.99, "form_factor": "2.5"},
        {"name": "Western Digital Black 500GB", "manufacturer": "Western Digital", "capacity": "500GB", "interface": "SATA", "price": 49.99, "form_factor": "2.5"},
        {"name": "Toshiba MQ01ABD050 500GB", "manufacturer": "Toshiba", "capacity": "500GB", "interface": "SATA", "price": 34.99, "form_factor": "2.5"},
        {"name": "Seagate BarraCuda 5TB", "manufacturer": "Seagate", "capacity": "5TB", "interface": "SATA", "price": 129.99, "form_factor": "2.5"},
        {"name": "Western Digital Black 6TB", "manufacturer": "Western Digital", "capacity": "6TB", "interface": "SATA", "price": 249.99, "form_factor": "3.5"},
        {"name": "Toshiba N300 6TB", "manufacturer": "Toshiba", "capacity": "6TB", "interface": "SATA", "price": 199.99, "form_factor": "3.5"},
        {"name": "Seagate IronWolf 8TB", "manufacturer": "Seagate", "capacity": "8TB", "interface": "SATA", "price": 229.99, "form_factor": "3.5"},
        {"name": "Western Digital Red 8TB", "manufacturer": "Western Digital", "capacity": "8TB", "interface": "SATA", "price": 219.99, "form_factor": "3.5"},
        {"name": "Toshiba X300 8TB", "manufacturer": "Toshiba", "capacity": "8TB", "interface": "SATA", "price": 209.99, "form_factor": "3.5"},
        {"name": "Seagate FireCuda 1TB", "manufacturer": "Seagate", "capacity": "1TB", "interface": "SATA", "price": 64.99, "form_factor": "2.5"},
        {"name": "Western Digital Black 4TB", "manufacturer": "Western Digital", "capacity": "4TB", "interface": "SATA", "price": 174.99, "form_factor": "3.5"},
        {"name": "Toshiba L200 2TB", "manufacturer": "Toshiba", "capacity": "2TB", "interface": "SATA", "price": 79.99, "form_factor": "2.5"},
        {"name": "Seagate Exos X14 14TB", "manufacturer": "Seagate", "capacity": "14TB", "interface": "SATA", "price": 379.99, "form_factor": "3.5"},
        {"name": "Western Digital Ultrastar DC HC530 14TB", "manufacturer": "Western Digital", "capacity": "14TB", "interface": "SATA", "price": 359.99, "form_factor": "3.5"},
        {"name": "Toshiba N300 14TB", "manufacturer": "Toshiba", "capacity": "14TB", "interface": "SATA", "price": 349.99, "form_factor": "3.5"},
        {"name": "Seagate IronWolf Pro 12TB", "manufacturer": "Seagate", "capacity": "12TB", "interface": "SATA", "price": 299.99, "form_factor": "3.5"},
        {"name": "Western Digital Red Pro 12TB", "manufacturer": "Western Digital", "capacity": "12TB", "interface": "SATA", "price": 289.99, "form_factor": "3.5"},
        {"name": "Toshiba MG07ACA12TE 12TB", "manufacturer": "Toshiba", "capacity": "12TB", "interface": "SATA", "price": 279.99, "form_factor": "3.5"},
        {"name": "Seagate FireCuda 2.5TB", "manufacturer": "Seagate", "capacity": "2.5TB", "interface": "SATA", "price": 139.99, "form_factor": "2.5"},
        {"name": "Western Digital Black 1TB", "manufacturer": "Western Digital", "capacity": "1TB", "interface": "SATA", "price": 79.99, "form_factor": "3.5"},
        {"name": "Toshiba X300 3TB", "manufacturer": "Toshiba", "capacity": "3TB", "interface": "SATA", "price": 94.99, "form_factor": "3.5"},
        {"name": "Seagate IronWolf 2TB", "manufacturer": "Seagate", "capacity": "2TB", "interface": "SATA", "price": 79.99, "form_factor": "3.5"},
        {"name": "Western Digital Red 3TB", "manufacturer": "Western Digital", "capacity": "3TB", "interface": "SATA", "price": 99.99, "form_factor": "3.5"},
        {"name": "Toshiba N300 3TB", "manufacturer": "Toshiba", "capacity": "3TB", "interface": "SATA", "price": 89.99, "form_factor": "3.5"}
    ]

    for data in hard_drive_data:
        harddrive = HardDrive(**data)
        db.session.add(harddrive)

    # Заполнение таблицы Case
    case_data = [
        {"name": "NZXT H510", "manufacturer": "NZXT", "form_factor": "Mid Tower", "price": 69.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Corsair 4000D", "manufacturer": "Corsair", "form_factor": "Mid Tower", "price": 79.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Fractal Design Meshify C", "manufacturer": "Fractal Design", "form_factor": "Mid Tower", "price": 89.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 3x 2.5\""},
        {"name": "Cooler Master MasterBox Q300L", "manufacturer": "Cooler Master", "form_factor": "MicroATX", "price": 49.99, "usb_ports": 2, "drive_bays": "1x 3.5\", 2x 2.5\""},
        {"name": "Lian Li PC-O11 Dynamic", "manufacturer": "Lian Li", "form_factor": "Mid Tower", "price": 129.99, "usb_ports": 4, "drive_bays": "3x 3.5\", 6x 2.5\""},
        {"name": "Phanteks Eclipse P300A", "manufacturer": "Phanteks", "form_factor": "Mid Tower", "price": 59.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Thermaltake Core V21", "manufacturer": "Thermaltake", "form_factor": "MicroATX", "price": 59.99, "usb_ports": 2, "drive_bays": "3x 3.5\", 3x 2.5\""},
        {"name": "be quiet! Pure Base 500DX", "manufacturer": "be quiet!", "form_factor": "Mid Tower", "price": 99.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 5x 2.5\""},
        {"name": "Corsair iCUE 220T", "manufacturer": "Corsair", "form_factor": "Mid Tower", "price": 99.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "NZXT H210i", "manufacturer": "NZXT", "form_factor": "Mini ITX", "price": 109.99, "usb_ports": 2, "drive_bays": "1x 3.5\", 2x 2.5\""},
        {"name": "Cooler Master MasterCase H500", "manufacturer": "Cooler Master", "form_factor": "Mid Tower", "price": 149.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Lian Li Lancool II", "manufacturer": "Lian Li", "form_factor": "Mid Tower", "price": 89.99, "usb_ports": 2, "drive_bays": "3x 3.5\", 4x 2.5\""},
        {"name": "Fractal Design Define 7", "manufacturer": "Fractal Design", "form_factor": "Mid Tower", "price": 149.99, "usb_ports": 5, "drive_bays": "6x 3.5\", 2x 2.5\""},
        {"name": "Thermaltake View 71", "manufacturer": "Thermaltake", "form_factor": "Full Tower", "price": 189.99, "usb_ports": 4, "drive_bays": "4x 3.5\", 6x 2.5\""},
        {"name": "Phanteks Enthoo Pro", "manufacturer": "Phanteks", "form_factor": "Full Tower", "price": 109.99, "usb_ports": 4, "drive_bays": "6x 3.5\", 4x 2.5\""},
        {"name": "Cooler Master MasterBox TD500", "manufacturer": "Cooler Master", "form_factor": "Mid Tower", "price": 99.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "NZXT H510 Elite", "manufacturer": "NZXT", "form_factor": "Mid Tower", "price": 149.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Corsair 5000D", "manufacturer": "Corsair", "form_factor": "Mid Tower", "price": 164.99, "usb_ports": 4, "drive_bays": "4x 3.5\", 3x 2.5\""},
        {"name": "Lian Li PC-O11 Air", "manufacturer": "Lian Li", "form_factor": "Mid Tower", "price": 139.99, "usb_ports": 4, "drive_bays": "3x 3.5\", 6x 2.5\""},
        {"name": "Fractal Design Node 804", "manufacturer": "Fractal Design", "form_factor": "MicroATX", "price": 109.99, "usb_ports": 4, "drive_bays": "8x 3.5\", 4x 2.5\""},
        {"name": "Thermaltake Core P3", "manufacturer": "Thermaltake", "form_factor": "Mid Tower", "price": 139.99, "usb_ports": 4, "drive_bays": "3x 3.5\", 3x 2.5\""},
        {"name": "Phanteks Evolv X", "manufacturer": "Phanteks", "form_factor": "Mid Tower", "price": 199.99, "usb_ports": 4, "drive_bays": "4x 3.5\", 6x 2.5\""},
        {"name": "Cooler Master Cosmos C700P", "manufacturer": "Cooler Master", "form_factor": "Full Tower", "price": 319.99, "usb_ports": 4, "drive_bays": "5x 3.5\", 6x 2.5\""},
        {"name": "NZXT H700i", "manufacturer": "NZXT", "form_factor": "Mid Tower", "price": 199.99, "usb_ports": 2, "drive_bays": "3x 3.5\", 2x 2.5\""},
        {"name": "Corsair Crystal Series 680X", "manufacturer": "Corsair", "form_factor": "Mid Tower", "price": 219.99, "usb_ports": 2, "drive_bays": "3x 3.5\", 4x 2.5\""},
        {"name": "Lian Li PC-O11D Mini", "manufacturer": "Lian Li", "form_factor": "Mini Tower", "price": 109.99, "usb_ports": 4, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Fractal Design Define R6", "manufacturer": "Fractal Design", "form_factor": "Mid Tower", "price": 139.99, "usb_ports": 4, "drive_bays": "6x 3.5\", 2x 2.5\""},
        {"name": "Thermaltake S100", "manufacturer": "Thermaltake", "form_factor": "MicroATX", "price": 69.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Phanteks P500A", "manufacturer": "Phanteks", "form_factor": "Mid Tower", "price": 129.99, "usb_ports": 4, "drive_bays": "3x 3.5\", 3x 2.5\""},
        {"name": "Cooler Master NR200", "manufacturer": "Cooler Master", "form_factor": "Mini ITX", "price": 79.99, "usb_ports": 2, "drive_bays": "1x 3.5\", 2x 2.5\""},
        {"name": "NZXT H510 Flow", "manufacturer": "NZXT", "form_factor": "Mid Tower", "price": 69.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Corsair Obsidian Series 1000D", "manufacturer": "Corsair", "form_factor": "Super Tower", "price": 499.99, "usb_ports": 4, "drive_bays": "5x 3.5\", 6x 2.5\""},
        {"name": "Lian Li PC-O11D XL", "manufacturer": "Lian Li", "form_factor": "Full Tower", "price": 199.99, "usb_ports": 4, "drive_bays": "4x 3.5\", 6x 2.5\""},
        {"name": "Fractal Design Meshify S2", "manufacturer": "Fractal Design", "form_factor": "Mid Tower", "price": 169.99, "usb_ports": 4, "drive_bays": "3x 3.5\", 4x 2.5\""},
        {"name": "Thermaltake View 31", "manufacturer": "Thermaltake", "form_factor": "Mid Tower", "price": 89.99, "usb_ports": 2, "drive_bays": "2x 3.5\", 2x 2.5\""},
        {"name": "Phanteks Eclipse P600S", "manufacturer": "Phanteks", "form_factor": "Mid Tower", "price": 149.99, "usb_ports": 4, "drive_bays": "3x 3.5\", 3x 2.5\""},
        {"name": "Cooler Master HAF XB EVO", "manufacturer": "Cooler Master", "form_factor": "ATX", "price": 109.99, "usb_ports": 2, "drive_bays": "4x 3.5\", 4x 2.5\""}
    ]


    for data in case_data:
        case = Case(**data)
        db.session.add(case)

    # Заполнение таблицы Keyboard
    keyboard_data = [
        {"name": "Logitech G Pro X", "manufacturer": "Logitech", "connectivity": "Wired", "price": 129.99, "backlight": True},
        {"name": "Corsair K95 RGB Platinum", "manufacturer": "Corsair", "connectivity": "Wired", "price": 199.99, "backlight": True},
        {"name": "Razer Huntsman Elite", "manufacturer": "Razer", "connectivity": "Wired", "price": 169.99, "backlight": True},
        {"name": "SteelSeries Apex Pro", "manufacturer": "SteelSeries", "connectivity": "Wired", "price": 199.99, "backlight": True},
        {"name": "HyperX Alloy FPS Pro", "manufacturer": "HyperX", "connectivity": "Wired", "price": 89.99, "backlight": True},
        {"name": "Ducky One 2 Mini", "manufacturer": "Ducky", "connectivity": "Wired", "price": 99.99, "backlight": True},
        {"name": "Cooler Master SK621", "manufacturer": "Cooler Master", "connectivity": "Wireless", "price": 119.99, "backlight": True},
        {"name": "Anne Pro 2", "manufacturer": "Anne", "connectivity": "Wireless", "price": 89.99, "backlight": True},
        {"name": "Logitech K780", "manufacturer": "Logitech", "connectivity": "Wireless", "price": 59.99, "backlight": False},
        {"name": "Microsoft Surface Keyboard", "manufacturer": "Microsoft", "connectivity": "Wireless", "price": 99.99, "backlight": False},
        {"name": "Apple Magic Keyboard", "manufacturer": "Apple", "connectivity": "Wireless", "price": 99.99, "backlight": False},
        {"name": "Corsair K63 Wireless", "manufacturer": "Corsair", "connectivity": "Wireless", "price": 109.99, "backlight": True},
        {"name": "Razer BlackWidow V3 Pro", "manufacturer": "Razer", "connectivity": "Wireless", "price": 229.99, "backlight": True},
        {"name": "Logitech G915 TKL", "manufacturer": "Logitech", "connectivity": "Wireless", "price": 229.99, "backlight": True},
        {"name": "Keychron K2", "manufacturer": "Keychron", "connectivity": "Wireless", "price": 79.99, "backlight": True},
        {"name": "Das Keyboard 4Q", "manufacturer": "Das Keyboard", "connectivity": "Wired", "price": 199.99, "backlight": True},
        {"name": "SteelSeries Apex 7", "manufacturer": "SteelSeries", "connectivity": "Wired", "price": 159.99, "backlight": True},
        {"name": "HyperX Alloy Origins", "manufacturer": "HyperX", "connectivity": "Wired", "price": 109.99, "backlight": True},
        {"name": "Ducky One 2 SF", "manufacturer": "Ducky", "connectivity": "Wired", "price": 109.99, "backlight": True},
        {"name": "Cooler Master MK730", "manufacturer": "Cooler Master", "connectivity": "Wired", "price": 149.99, "backlight": True},
        {"name": "Anne Pro 2", "manufacturer": "Anne", "connectivity": "Wireless", "price": 99.99, "backlight": True},
        {"name": "Logitech MX Keys", "manufacturer": "Logitech", "connectivity": "Wireless", "price": 99.99, "backlight": True},
        {"name": "Microsoft Sculpt Ergonomic Keyboard", "manufacturer": "Microsoft", "connectivity": "Wireless", "price": 129.99, "backlight": False},
        {"name": "Razer Cynosa V2", "manufacturer": "Razer", "connectivity": "Wired", "price": 59.99, "backlight": True},
        {"name": "Logitech K380", "manufacturer": "Logitech", "connectivity": "Wireless", "price": 39.99, "backlight": False},
        {"name": "Corsair K70 RGB MK.2", "manufacturer": "Corsair", "connectivity": "Wired", "price": 159.99, "backlight": True},
        {"name": "Razer Ornata V2", "manufacturer": "Razer", "connectivity": "Wired", "price": 99.99, "backlight": True},
        {"name": "SteelSeries Apex 5", "manufacturer": "SteelSeries", "connectivity": "Wired", "price": 129.99, "backlight": True},
        {"name": "HyperX Alloy Elite 2", "manufacturer": "HyperX", "connectivity": "Wired", "price": 139.99, "backlight": True},
        {"name": "Ducky One 2 TKL", "manufacturer": "Ducky", "connectivity": "Wired", "price": 119.99, "backlight": True},
        {"name": "Cooler Master CK530 V2", "manufacturer": "Cooler Master", "connectivity": "Wired", "price": 89.99, "backlight": True}
    ]


    for data in keyboard_data:
        keyboard = Keyboard(**data)
        db.session.add(keyboard)

    # Заполнение таблицы Mouse
    mouse_data = [
        {"name": "Logitech G Pro Wireless", "manufacturer": "Logitech", "connectivity": "Wireless", "price": 149.99, "dpi": 16000},
        {"name": "Razer DeathAdder V2", "manufacturer": "Razer", "connectivity": "Wired", "price": 69.99, "dpi": 20000},
        {"name": "SteelSeries Rival 600", "manufacturer": "SteelSeries", "connectivity": "Wired", "price": 79.99, "dpi": 12000},
        {"name": "Corsair Dark Core RGB Pro SE", "manufacturer": "Corsair", "connectivity": "Wireless", "price": 89.99, "dpi": 18000},
        {"name": "HyperX Pulsefire FPS Pro", "manufacturer": "HyperX", "connectivity": "Wired", "price": 49.99, "dpi": 16000},
        {"name": "Finalmouse Ultralight 2 - Cape Town", "manufacturer": "Finalmouse", "connectivity": "Wired", "price": 119.99, "dpi": 3200},
        {"name": "Glorious Model O", "manufacturer": "Glorious", "connectivity": "Wired", "price": 49.99, "dpi": 12000},
        {"name": "Logitech MX Master 3", "manufacturer": "Logitech", "connectivity": "Wireless", "price": 99.99, "dpi": 4000},
        {"name": "Razer Viper Ultimate", "manufacturer": "Razer", "connectivity": "Wireless", "price": 149.99, "dpi": 20000},
        {"name": "SteelSeries Sensei Ten", "manufacturer": "SteelSeries", "connectivity": "Wired", "price": 69.99, "dpi": 18000},
        {"name": "Corsair Ironclaw Wireless", "manufacturer": "Corsair", "connectivity": "Wireless", "price": 79.99, "dpi": 18000},
        {"name": "HyperX Pulsefire Surge", "manufacturer": "HyperX", "connectivity": "Wired", "price": 54.99, "dpi": 16000},
        {"name": "Finalmouse Air58 Ninja", "manufacturer": "Finalmouse", "connectivity": "Wired", "price": 89.99, "dpi": 3200},
        {"name": "Glorious Model D", "manufacturer": "Glorious", "connectivity": "Wired", "price": 49.99, "dpi": 12000},
        {"name": "Logitech G502 HERO", "manufacturer": "Logitech", "connectivity": "Wired", "price": 79.99, "dpi": 16000},
        {"name": "Razer Basilisk Ultimate", "manufacturer": "Razer", "connectivity": "Wireless", "price": 169.99, "dpi": 20000},
        {"name": "SteelSeries Rival 310", "manufacturer": "SteelSeries", "connectivity": "Wired", "price": 49.99, "dpi": 12000},
        {"name": "Corsair Harpoon RGB Wireless", "manufacturer": "Corsair", "connectivity": "Wireless", "price": 49.99, "dpi": 10000},
        {"name": "HyperX Pulsefire Core", "manufacturer": "HyperX", "connectivity": "Wired", "price": 29.99, "dpi": 6200},
        {"name": "Finalmouse Ultralight Phantom", "manufacturer": "Finalmouse", "connectivity": "Wired", "price": 89.99, "dpi": 3200},
        {"name": "Glorious Model O-", "manufacturer": "Glorious", "connectivity": "Wired", "price": 49.99, "dpi": 12000},
        {"name": "Logitech G305 Lightspeed", "manufacturer": "Logitech", "connectivity": "Wireless", "price": 59.99, "dpi": 12000},
        {"name": "Razer DeathAdder Essential", "manufacturer": "Razer", "connectivity": "Wired", "price": 29.99, "dpi": 6400},
        {"name": "SteelSeries Rival 3", "manufacturer": "SteelSeries", "connectivity": "Wired", "price": 29.99, "dpi": 8500},
        {"name": "Corsair M65 RGB Elite", "manufacturer": "Corsair", "connectivity": "Wired", "price": 59.99, "dpi": 18000},
        {"name": "HyperX Pulsefire FPS", "manufacturer": "HyperX", "connectivity": "Wired", "price": 49.99, "dpi": 3200},
        {"name": "Finalmouse Ultralight Sunset", "manufacturer": "Finalmouse", "connectivity": "Wired", "price": 89.99, "dpi": 3200},
        {"name": "Glorious Model O Wireless", "manufacturer": "Glorious", "connectivity": "Wireless", "price": 79.99, "dpi": 19000}
    ]


    for data in mouse_data:
        mouse = Mouse(**data)
        db.session.add(mouse)

    # Заполнение таблицы Monitor
    monitor_data = [
        {"name": "ASUS VG248QE", "manufacturer": "ASUS", "display_size": "24 inches", "resolution": "1920x1080", "price": 249.99, "refresh_rate": 144, "panel_type": "TN"},
        {"name": "Dell S2716DG", "manufacturer": "Dell", "display_size": "27 inches", "resolution": "2560x1440", "price": 499.99, "refresh_rate": 144, "panel_type": "TN"},
        {"name": "Acer Predator XB271HU", "manufacturer": "Acer", "display_size": "27 inches", "resolution": "2560x1440", "price": 599.99, "refresh_rate": 144, "panel_type": "IPS"},
        {"name": "LG 27GL850-B", "manufacturer": "LG", "display_size": "27 inches", "resolution": "2560x1440", "price": 499.99, "refresh_rate": 144, "panel_type": "IPS"},
        {"name": "ASUS ROG Swift PG279Q", "manufacturer": "ASUS", "display_size": "27 inches", "resolution": "2560x1440", "price": 699.99, "refresh_rate": 144, "panel_type": "IPS"},
        {"name": "BenQ ZOWIE XL2411P", "manufacturer": "BenQ", "display_size": "24 inches", "resolution": "1920x1080", "price": 199.99, "refresh_rate": 144, "panel_type": "TN"},
        {"name": "MSI Optix MAG271CQR", "manufacturer": "MSI", "display_size": "27 inches", "resolution": "2560x1440", "price": 399.99, "refresh_rate": 144, "panel_type": "VA"},
        {"name": "AOC C24G1", "manufacturer": "AOC", "display_size": "24 inches", "resolution": "1920x1080", "price": 179.99, "refresh_rate": 144, "panel_type": "VA"},
        {"name": "Samsung Odyssey G7", "manufacturer": "Samsung", "display_size": "27 inches", "resolution": "2560x1440", "price": 699.99, "refresh_rate": 240, "panel_type": "VA"},
        {"name": "ViewSonic VX2458-MHD", "manufacturer": "ViewSonic", "display_size": "24 inches", "resolution": "1920x1080", "price": 159.99, "refresh_rate": 144, "panel_type": "TN"},
        {"name": "ASUS TUF Gaming VG27AQ", "manufacturer": "ASUS", "display_size": "27 inches", "resolution": "2560x1440", "price": 429.99, "refresh_rate": 165, "panel_type": "IPS"},
        {"name": "Dell S3220DGF", "manufacturer": "Dell", "display_size": "32 inches", "resolution": "2560x1440", "price": 449.99, "refresh_rate": 165, "panel_type": "VA"},
        {"name": "Acer Nitro XV272U", "manufacturer": "Acer", "display_size": "27 inches", "resolution": "2560x1440", "price": 399.99, "refresh_rate": 144, "panel_type": "IPS"},
        {"name": "LG 34GN850-B", "manufacturer": "LG", "display_size": "34 inches", "resolution": "3440x1440", "price": 999.99, "refresh_rate": 160, "panel_type": "IPS"},
        {"name": "ASUS ROG Strix XG279Q", "manufacturer": "ASUS", "display_size": "27 inches", "resolution": "2560x1440", "price": 599.99, "refresh_rate": 170, "panel_type": "IPS"},
        {"name": "BenQ EX2780Q", "manufacturer": "BenQ", "display_size": "27 inches", "resolution": "2560x1440", "price": 499.99, "refresh_rate": 144, "panel_type": "IPS"},
        {"name": "MSI Optix MPG341CQR", "manufacturer": "MSI", "display_size": "34 inches", "resolution": "3440x1440", "price": 799.99, "refresh_rate": 144, "panel_type": "VA"},
        {"name": "AOC Agon AG352UCG6", "manufacturer": "AOC", "display_size": "35 inches", "resolution": "3440x1440", "price": 899.99, "refresh_rate": 120, "panel_type": "VA"},
        {"name": "Samsung Odyssey G9", "manufacturer": "Samsung", "display_size": "49 inches", "resolution": "5120x1440", "price": 1499.99, "refresh_rate": 240, "panel_type": "VA"},
        {"name": "ViewSonic Elite XG270QG", "manufacturer": "ViewSonic", "display_size": "27 inches", "resolution": "2560x1440", "price": 599.99, "refresh_rate": 165, "panel_type": "IPS"}
    ]

    for data in monitor_data:
        monitor = Monitor(**data)
        db.session.add(monitor)

    # Заполнение таблицы CoolingSystem
    cooling_system_data = [
        {"name": "Noctua NH-D15", "manufacturer": "Noctua", "type": "Air", "price": 99.99, "fan_size": 140},
        {"name": "NZXT Kraken X63", "manufacturer": "NZXT", "type": "Liquid", "price": 149.99, "fan_size": 280},
        {"name": "Cooler Master Hyper 212 RGB Black Edition", "manufacturer": "Cooler Master", "type": "Air", "price": 44.99, "fan_size": 120},
        {"name": "Corsair H100i RGB PLATINUM", "manufacturer": "Corsair", "type": "Liquid", "price": 159.99, "fan_size": 240},
        {"name": "be quiet! Dark Rock Pro 4", "manufacturer": "be quiet!", "type": "Air", "price": 89.99, "fan_size": 135},
        {"name": "Arctic Liquid Freezer II 280", "manufacturer": "Arctic", "type": "Liquid", "price": 109.99, "fan_size": 140},
        {"name": "Deepcool GAMMAXX 400", "manufacturer": "Deepcool", "type": "Air", "price": 29.99, "fan_size": 120},
        {"name": "Thermaltake Water 3.0 360 ARGB", "manufacturer": "Thermaltake", "type": "Liquid", "price": 179.99, "fan_size": 360},
        {"name": "Scythe Mugen 5 Rev.B", "manufacturer": "Scythe", "type": "Air", "price": 49.99, "fan_size": 120},
        {"name": "EVGA CLC 240mm", "manufacturer": "EVGA", "type": "Liquid", "price": 119.99, "fan_size": 240},
        {"name": "Cooler Master MasterLiquid ML240L RGB", "manufacturer": "Cooler Master", "type": "Liquid", "price": 69.99, "fan_size": 240},
        {"name": "Arctic Freezer 34 eSports DUO", "manufacturer": "Arctic", "type": "Air", "price": 49.99, "fan_size": 120},
        {"name": "NZXT Kraken Z63", "manufacturer": "NZXT", "type": "Liquid", "price": 249.99, "fan_size": 280},
        {"name": "Noctua NH-U12S", "manufacturer": "Noctua", "type": "Air", "price": 69.99, "fan_size": 120},
        {"name": "Corsair iCUE H150i ELITE CAPELLIX", "manufacturer": "Corsair", "type": "Liquid", "price": 189.99, "fan_size": 360},
        {"name": "be quiet! Pure Rock 2", "manufacturer": "be quiet!", "type": "Air", "price": 39.99, "fan_size": 120},
        {"name": "Arctic Liquid Freezer II 360", "manufacturer": "Arctic", "type": "Liquid", "price": 129.99, "fan_size": 120},
        {"name": "Deepcool Castle 240EX", "manufacturer": "Deepcool", "type": "Liquid", "price": 99.99, "fan_size": 240},
        {"name": "Thermaltake Floe DX RGB 360 TT Premium Edition", "manufacturer": "Thermaltake", "type": "Liquid", "price": 199.99, "fan_size": 360},
        {"name": "Scythe Fuma 2", "manufacturer": "Scythe", "type": "Air", "price": 59.99, "fan_size": 120},
        {"name": "EVGA CLC 280mm", "manufacturer": "EVGA", "type": "Liquid", "price": 129.99, "fan_size": 280},
        {"name": "Cooler Master Hyper 212 EVO", "manufacturer": "Cooler Master", "type": "Air", "price": 34.99, "fan_size": 120},
        {"name": "Arctic Liquid Freezer II 240", "manufacturer": "Arctic", "type": "Liquid", "price": 99.99, "fan_size": 240},
        {"name": "NZXT Kraken X53", "manufacturer": "NZXT", "type": "Liquid", "price": 129.99, "fan_size": 240},
        {"name": "Noctua NH-L9i", "manufacturer": "Noctua", "type": "Air", "price": 39.99, "fan_size": 92},
        {"name": "Corsair H60", "manufacturer": "Corsair", "type": "Liquid", "price": 79.99, "fan_size": 120},
        {"name": "be quiet! Dark Rock 4", "manufacturer": "be quiet!", "type": "Air", "price": 74.99, "fan_size": 135}
    ]

    for data in cooling_system_data:
        coolingsystem = CoolingSystem(**data)
        db.session.add(coolingsystem)

    # Коммит изменений
    db.session.commit()

