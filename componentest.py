from wsgi import app, db, Videocard, Motherboard, PowerSupplyUnit, RAM, HardDrive, Case, Keyboard, Mouse, Monitor, CoolingSystem, Processor
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

with app.app_context():
# Проверяем данные о процессорах
    processors = Processor.query.all()
for processor in processors:
    print(processor.id, processor.name, processor.manufacturer, processor.cores, processor.base_clock, processor.boost_clock, processor.socket, processor.price, processor.tdp)



    # Коммит изменений
db.session.commit()
