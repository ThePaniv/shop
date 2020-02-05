from .app import db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return self.name


class Basket(db.Model):
    __tablename__ = 'basket'

    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer, nullable=False)
    num_of_products = db.Column(db.Integer, nullable=False)


class BasketStorage(db.Model):
    __tablename__ = 'basket_storage'

    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return 'Basket ID: {}, Product ID: {}'.format(self.basket_id, self.product_id)
