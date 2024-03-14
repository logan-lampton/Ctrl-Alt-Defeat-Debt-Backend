from random import randint, choice as rc

from faker import Faker

from config import db, app
from models.models import *

if __name__ == "__main__":
    fake = Faker()
    with app.app_context():
        print("Beginning Seed...")
        # deletes database
        User.query.delete()
        Account.query.delete()
        Group.query.delete()
        Goal.query.delete()

        #Creates fake users
        users = []
        print("    Seeding Users...")
        email_endpoints = ["@gmail.com", "@yahoo.com", "@outlook.com"]
        for i in range(10):
            email_endpoint = rc(email_endpoints)
            fake_user = fake.unique.first_name()
            fake_number = fake.msisdn()
            user = User(
                username = fake_user,
                email = f"{fake_user}{email_endpoint}",
                phone = fake_number
            )
            user.password_hash = user.username

            db.session.add(user)
            db.session.commit()

            users.append(user)

        #Creates fake groups
        groups = []
        print("    Seeding Groups...")
        roles = ["Admin", "Member"]
        visibility = ["Full", "Limited", "Restricted"]
        for i in range(5):
            user = rc(users)
            fake_name = fake.unique.last_name()
            
            group = Group(
                is_family = True,
                name = fake_name,
                role = rc(roles),
                visibility_status = rc(visibility),
                user_id =  user.id
            )

            db.session.add(group)
            db.session.commit()
            groups.append(group)

        #Creates fake goals
        goals = []
        print("    Seeding Goals...")
        emojis = ["U+1F600", "U+1F607", "U+1F911", "U+1F62C", "U+1F634"]
        for group in groups:
            image = rc(emojis)
            start = fake.past_date()
            end = fake.future_date()

            goal = Goal(
                name = fake_name,
                saving_target = randint(100, 500),
                start_timeframe = start,
                end_timeframe= end,
                emoji =  image,
                group_id = group.id
            )

            db.session.add(goal)
            db.session.commit()
            goals.append(goals)

        #Creates fake accounts
        accounts = []
        print("    Seeding Accounts...")
        acc_types = ["Savings", "Checking"]
        for user in users:
            fake_name = fake.unique.company()
            types = rc(acc_types)
            acc_bal = randint(400, 1500)

            account = Account(
                name = fake_name,
                type = types,
                balance = acc_bal,
                user_id = user.id,
            )

            db.session.add(account)
            db.session.commit()
            groups.append(group)