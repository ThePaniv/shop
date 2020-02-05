from .app import db
from .models import Category, Product

product1 = Product(name='Світшот чорний', description="None", price=70.0, rating=3, image='p28.jpg', category_id=1)
product2 = Product(name='Годинник Daniel Klein', description="None", price=120.40, rating=4, image='p29.jpg', category_id=1)
product3 = Product(name='Рюкзак American Tourister', description="None", price=85.0, rating=5, image='s1.jpg', category_id=1)
product4 = Product(name='Кеди чоловічі чорні', description="None", price=40.0, rating=2, image='s3.jpg', category_id=1)
product5 = Product(name='Мешти чоловічі класичні', description="None", price=19.0, rating=4, image='r2.jpg', category_id=1)
product6 = Product(name='Традиційне Індійське вбрання ', description="None", price=100.0, rating=3, image='r1.jpg', category_id=2)
product7 = Product(name='Комплект майка + шорти ', description="None", price=29.0, rating=3, image='r.jpg', category_id=2)

db.session.add(product1)
db.session.add(product2)
db.session.add(product3)
db.session.add(product4)
db.session.add(product5)
db.session.add(product6)
db.session.add(product7)
db.session.commit()