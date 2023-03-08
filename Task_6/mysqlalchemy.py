import json
import sqlalchemy


from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from settings import PASS

DSN = f"postgresql://postgres:{PASS}@localhost:5432/netology_db"

engine = sqlalchemy.create_engine(DSN)
create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()


with open("Task_6/book.json", "r") as f:
    data = json.load(f)

for record in data:
    model = {
        "publisher": Publisher,
        "shop": Shop,
        "book": Book,
        "stock": Stock,
        "sale": Sale,
    }[record.get("model")]
    session.add(model(id=record.get("pk"), **record.get("fields")))
session.commit()
session.close()

p_name = input("Введите название издателя: ")
t = (
    session.query(Publisher, Shop.name, Book.title, Sale.price, Sale.date_sale)
    .join(Book)
    .join(Stock)
    .join(Sale)
    .join(Shop)
    .filter(Publisher.name.like(f"%{p_name}%"))
    .all()
)

if __name__ == "__main__":
    for i in t:
        print(f" {i.Publisher.name} | {i.title} | {i.name} | {i.price} | {i.date_sale}")
