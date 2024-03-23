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
        Insight.query.delete()
        Personal_goal.query.delete()
        Action.query.delete()
        # Creates Family group and users
        # roles = ["Admin", "Member", "Viewer"]
        # visibility = ["Full", "Limited", "Restricted"]
        groups = []
        print("    Seeding Family Group...")
            
        family_group = Group(
            name = "The Craft Family",
        )

        db.session.add(family_group)
        db.session.commit()
        groups.append(family_group)
        print("    Seeding Family Users...")
        users = []
        dad = User(
            first_name = "Steve",
            last_name = "Craft",
            email = f"SteveCraft123@gmail.com",
            phone = fake.msisdn(),
            admin = True,
            visibility_status = "Full",
            rent = randint(1000, 1500),
            income = randint(2500, 4000),
            group_id = family_group.id,
            _access_token = "access-sandbox-371d3141-3c75-469b-978d-adc90f60abfc"
        )
        dad.password_hash = dad.email

        db.session.add(dad)
        db.session.commit()
        users.append(dad)

        mom = User(
            first_name = "Alex",
            last_name = "Craft",
            email = f"AlexCraft123@gmail.com",
            phone = fake.msisdn(),
            admin = True,
            visibility_status = "Full",
            rent = randint(1000, 1500),
            income = randint(2500, 4000),
            group_id = family_group.id, 
            _access_token = "access-sandbox-12a993e3-e0ce-4e17-b14c-3340096978a5"
        )
        mom.password_hash = mom.email

        db.session.add(mom)
        db.session.commit()
        users.append(mom)

        family_group.total_income = mom.income + dad.income
        family_group._access_token = f"{dad._access_token}%%{mom._access_token}"

        child = User(
            first_name = "Steelix",
            last_name = "Craft",
            email = f"SteelixCraft123@gmail.com",
            phone = fake.msisdn(),
            admin = True,
            visibility_status = "Restricted",
            rent = randint(1000, 1500),
            income = randint(2500, 4000),
            group_id = family_group.id  
        )
        child.password_hash = child.email

        db.session.add(child)
        db.session.commit()
        users.append(child)

        print("    Seeding Family Group Goals...")
        goals = []
        emojis = ["U+1F600", "U+1F607", "U+1F911", "U+1F62C", "U+1F634"]
        goal_names = ["Save up for a cruise", "Save up for a vacation", "Have an emergency cushion", "Save for a large purchase", "Build a nest egg", "Create a unique goal"]
        for i in range(randint(2, 4)):
            goal = Goal(
                name = rc(goal_names),
                saving_target = randint(100, 500),
                start_timeframe = fake.past_date(),
                end_timeframe= fake.future_date(),
                emoji = rc(emojis),
                group_id = family_group.id
            )

            db.session.add(goal)
            db.session.commit()
            goals.append(goal)
        
        print("    Seeding Single User...")
        single_user = User(
            first_name = "Single",
            last_name = "User",
            email = f"SingleUser123@gmail.com",
            phone = fake.msisdn(),
            admin = True,
            visibility_status = "Full",
            rent = randint(1000, 1500),
            income = randint(2500, 4000),
        )
        single_user.password_hash = single_user.email

        db.session.add(single_user)
        db.session.commit()
        users.append(single_user)

        print("    Seeding personal goals...")
        personal_goals = []
        for user in users:
            for i in range(randint(1, 3)):
                pg = Personal_goal(
                    name = rc(goal_names),
                    saving_target = randint(100, 500),
                    start_timeframe = fake.past_date(),
                    end_timeframe= fake.future_date(),
                    emoji = rc(emojis),
                    user_id = user.id
                )
                db.session.add(pg)
                db.session.commit()
                personal_goals.append(pg)

        print("    Seeding insights...")
        insights = []
        actions = []
        for goal in goals:
            insight = Insight(
                    savings_monthly = randint(100, 500),
                    savings_needed = randint(100, 500),
                    strategy = fake.paragraph(nb_sentences=5),
                    goal_id = goal.id
            )
            db.session.add(insight)
            db.session.commit()
            insights.append(insight)

        for personal_goal in personal_goals:
            insight = Insight(
                savings_monthly = randint(100, 500),
                savings_needed = randint(100, 500),
                strategy = fake.paragraph(nb_sentences=5),
                personal_goal_id = personal_goal.id
            )
            db.session.add(insight)
            db.session.commit()
            insights.append(insight)
        
        for insight in insights:
            for i in range(5):
                action = Action(
                    text = fake.sentence(),
                    insight_id = insight.id
                )
                db.session.add(action)
                db.session.commit()
                actions.append(action)

    print("Seed complete!")