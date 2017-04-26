from django.core.management.base import BaseCommand, CommandError
from signup.models import Account


class Command(BaseCommand):

    WUNDERGROUND_URL = ('http://api.wunderground.com/api/{key}/'
                        '{api}/q/{state}/{city}.json')

    API_ENDPOINTS = ['conditions', 'almanac']

    def handle(self, *args, **options):

        print [x.location.city for x in Account.objects.distinct('location')]
