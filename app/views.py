from app.app import flask_app, render_template, Product


@flask_app.route('/')
def index():
    products = Product.query.filter(Product.category_id == 1).all()
    return render_template('index.html', products=products)


@flask_app.route('/category/<int:category_id>')
def category(category_id):
    pass


@flask_app.route('/product/<int:product_id>')
def product(product_id):
    return render_template('single.html')
