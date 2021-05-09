from core.models import User
from django.core.management import BaseCommand
from django_redis import get_redis_connection

class Command(BaseCommand):
    def handle(self, *args, **options):
        conn = get_redis_connection("default")
        ambassadors = User.objects.filter(is_ambassador=True)
        
        for ambassador in ambassadors:
            conn.zadd("rankings", {ambassador.name: float(ambassador.revenue)})
            