from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

p1 = Pet(name='Doug', species='dog', photo_url="https://img1.wsimg.com/isteam/ip/c5fd033a-f031-4f6b-ae5e-bac8d1582b81/Screenshot_20230324_113742_Gallery.jpg/:/rs=w:700,cg:true,m", age=3, notes='Loves to dig, hence the name.')
p2 = Pet(name='ZanZan', species="cat", photo_url="https://i.pinimg.com/474x/01/f1/b9/01f1b9f828e46d5354645dd9c0dfe84d.jpg", age=2, notes="Sibling to the bestest kitty in the whole wide world.")
p3 = Pet(name="Rupert", species="porcupine", photo_url="https://i.pinimg.com/564x/62/fc/0c/62fc0c069c5a8783844f75ff4fd1660a.jpg", age=8, notes='Not as soft as he appears, but just as friendly.')


db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

db.session.commit()