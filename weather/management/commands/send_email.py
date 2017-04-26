from django.core.management.base import BaseCommand, CommandError
from signup.models import Account
import requests
import os


class Command(BaseCommand):

    WUNDERGROUND_URL = ('http://api.wunderground.com/api/{key}/'
                        '{api}/q/{state}/{city}.json')

    WUNDERGROUND_KEY = os.environ['WUNDERGROUND_KEY']

    # API_ENDPOINTS = ['conditions', 'almanac']

    def handle(self, *args, **options):

        for loc in Account.objects.distinct('location'):

            loc = loc.location

            # Get current conditions for location
            r = requests.get(
                self.WUNDERGROUND_URL.format(
                    key=self.WUNDERGROUND_KEY,
                    api='conditions',
                    state=loc.state,
                    city=loc.city
                )
            )

            curr_temp = r.json().get('current_observation').get('temp_f')

            r = requests.get(
                self.WUNDERGROUND_URL.format(
                    key=self.WUNDERGROUND_KEY,
                    api='almanac',
                    state=loc.state,
                    city=loc.city
                )
            )

            avg_temp = (r.json().get('almanac').get('temp_high')
                        .get('normal').get('F'))

            print curr_temp, avg_temp

        # print [x.location.city for x in Account.objects.distinct('location')]
