from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json
from django.core.management import call_command

class Command(BaseCommand):
    """Загружает данные из фикстур в базу данных"""
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'category_data.json')
        call_command('loaddata', 'product_data.json')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
