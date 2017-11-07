import logging

from django.core.management import BaseCommand

logger = logging.getLogger('django')

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("begin clean")
        logger.info("clean orders")