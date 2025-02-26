from app import db
from app.models import User
from faker import Faker
import os
fake = Faker()

def populate_users(count=10):
    if os.getenv("INIT_DB", "true").lower() == "false":
        return
    for _ in range(count):
        user_id = fake.unique.uuid4()
        name = fake.name()
        age = fake.random_int(min=18, max=100)
        points = fake.random_int(min=0, max=100)
        address = fake.address()
        
        existing_user = User.query.filter_by(id=user_id).first()
        if not existing_user:
            user = User(id=user_id, name=name, age=age, points=points, address=address)
            db.session.add(user)

    db.session.commit()
    print(f"{count} random users added successfully.")

if __name__ == "__main__":
    from leaderboard import app
    with app.app_context():
        populate_users()
