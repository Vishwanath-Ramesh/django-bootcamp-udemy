import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_2.settings')

import django
django.setup()

from faker import Faker
fake = Faker()

from app_1.models import User

def populate(num=5):
    for itr in range(num):
        # fake user field data
        fake_fname = fake.unique.first_name()
        fake_lname = fake.unique.last_name()
        fake_email = fake.unique.email()

        user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]
        user.save()

if __name__ == '__main__':
    print('Populating fake data...')
    populate(20)
    print('Population complete')
