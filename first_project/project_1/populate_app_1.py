import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_1.settings')

django.setup()

from app_1.models import Topic, Webpage, AccessRecord

fake = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    topic = Topic.objects.get_or_create(top_name=random.choice(topics))[0] # returns created topic instance
    topic.save()

    return topic

def populate(num=5):
    for entry in range(num):
        # creating new topic
        topic = add_topic()

        # fake fields 
        name = fake.company()
        url = fake.url()
        date = fake.date()

        # creating webpage entry
        webpage = Webpage.objects.get_or_create(topic=topic, name=name, url=url)[0]

        # creating access record
        accessRecord = AccessRecord.objects.get_or_create(name=webpage, date=date) 


if __name__ == '__main__':
    print('Populating fake data...')
    populate(20)
    print('Population complete')

