from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time
from faker import Faker
from core.models import Product
from random import randrange

class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        
        for _ in range(30):
            Product.objects.create(
                title=faker.name(),
                description=faker.text(100),
                image=faker.image_url(),
                price=randrange(10,100)
            )
