from app.app import flask_app, render_template, Category


@flask_app.route('/')
def index():
    products = Category.query.all()
    return render_template('index.html', products=products)


@flask_app.route('/single/<int:product_id>')
def single(product_id):
    return render_template('single.html')
