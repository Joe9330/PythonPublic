from flask import render_template
from app import app

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 库存页面
@app.route('/inventory')
def inventory_page():  # 确保函数名唯一，避免冲突
    return render_template('inventory.html')

# 采购页面
@app.route('/purchase')
def purchase_page():  # 确保函数名唯一，避免冲突
    return render_template('purchase.html')

# 生产订单页面
@app.route('/orders')
def orders_page():  # 确保函数名唯一，避免冲突
    return render_template('orders.html')

from app import Inventory, PurchaseOrder, ProductionOrder
from app import db

@app.route('/add_sample_data')
def add_sample_data():
    # 添加一些测试数据
    sample_item = Inventory(item_name="Air Filter", quantity=100)
    sample_purchase = PurchaseOrder(supplier="Supplier A", item_name="Air Filter", quantity=50)
    sample_production = ProductionOrder(product_name="Shock Absorber", quantity=200, status="进行中")

    db.session.add(sample_item)
    db.session.add(sample_purchase)
    db.session.add(sample_production)
    db.session.commit()

    return "Sample data added successfully!"
