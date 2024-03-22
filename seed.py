from random import randint, choice as rc

from faker import Faker

from config import db, app
from models.models import *

if __name__ == "__main__":
    fake = Faker()
    with app.app_context():
        print("Beginning Seed...")
        print("Deleting the database...")
        # deletes database
        User.query.delete()
        Group.query.delete()
        Goal.query.delete()

        #Creates fake groups
        groups = []
        print("    Seeding Groups...")
        for i in range(5):
            fake_name = fake.unique.last_name()
            
            group = Group(
                is_family = rc([True, False]),
                name = fake_name,
            )

            db.session.add(group)
            db.session.commit()
            groups.append(group)
        
        # Creates fake users
        users = []
        print("    Seeding Users...")
        roles = ["Admin", "Member"]
        visibility = ["Full", "Limited", "Restricted"]
        email_endpoints = ["@gmail.com", "@yahoo.com", "@outlook.com"]
        for group in groups:
            if group.is_family == False:
                email_endpoint = rc(email_endpoints)
                fake_first = fake.unique.first_name()
                fake_last = fake.unique.last_name()
                fake_number = fake.msisdn()
                user = User(
                    first_name = fake_first,
                    last_name = fake_last,
                    email = f"{fake_first}{fake_last}123{email_endpoint}",
                    phone = fake_number,
                    admin = True,
                    role = roles[0],
                    visibility_status = visibility[0],
                    rent = randint(1000, 1500),
                    income = randint(2500, 4000),
                    group_id = group.id
                )
                user.password_hash = user.email
                db.session.add(user)
                db.session.commit()

                users.append(user)
            else:
                email_endpoint = rc(email_endpoints)
                fake_first = fake.unique.first_name()
                fake_last = fake.unique.last_name()
                fake_number = fake.msisdn()

                user1 = User(
                    first_name = fake_first,
                    last_name = fake_last,
                    email = f"{fake_first}{fake_last}123{email_endpoint}",
                    phone = fake_number,
                    admin = True,
                    role = roles[0],
                    visibility_status = visibility[0],
                    rent = randint(1000, 1500),
                    income = randint(2500, 4000),
                    group_id = group.id
                )
                user1.password_hash = user1.email
                db.session.add(user1)
                db.session.commit()

                users.append(user1)

                random_range = randint(1, 3)
                for i in range(random_range):
                    email_endpoint = rc(email_endpoints)
                    fake_first = fake.unique.first_name()
                    fake_last = fake.unique.last_name()
                    fake_number = fake.msisdn()

                    user2 = User(
                        first_name = fake_first,
                        last_name = fake_last,
                        email = f"{fake_first}{fake_last}123{email_endpoint}",
                        phone = fake_number,
                        admin = False,
                        role = roles[1],
                        visibility_status = visibility[1],
                        rent = 0,
                        income = 0,
                        group_id = group.id
                    )
                    user2.password_hash = user2.email
                    db.session.add(user2)
                    db.session.commit()

                    users.append(user2)

        #Creates fake goals
        goals = []
        print("    Seeding Goals...")
        emojis = ["U+1F600", "U+1F607", "U+1F911", "U+1F62C", "U+1F634"]
        for group in groups:
            image = rc(emojis)

            goal = Goal(
                name = fake.unique.first_name(),
                saving_target = randint(100, 500),
                start_timeframe = fake.past_date(),
                end_timeframe= fake.future_date(),
                emoji =  image,
                group_id = group.id
            )

            db.session.add(goal)
            db.session.commit()
            goals.append(goal)

        #Creates fake accounts
        # accounts = []
        # print("    Seeding Accounts...")
        # acc_types = ["Savings", "Checking"]
        # for user in users:
        #     types = rc(acc_types)
        #     acc_bal = 0
        #     if user.admin == True:
        #         acc_bal = randint(400, 1500)

        #     account = Account(
        #         name = fake.unique.company(),
        #         type = types,
        #         balance = acc_bal,
        #         user_id = user.id,
        #     )

        #     db.session.add(account)
        #     db.session.commit()
        #     groups.append(group)

        print("Seed complete!")