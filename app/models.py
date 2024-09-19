from app import db

# 库存模型
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# 采购订单模型
class PurchaseOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(64), nullable=False)
    item_name = db.Column(db.String(64), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# 生产订单模型
class ProductionOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(64), nullable=False)  # 例如：进行中，已完成等
