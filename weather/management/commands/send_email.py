from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from signup.models import Account
import requests
import os


class Command(BaseCommand):

    # Base wunderground URL
    WUNDERGROUND_URL = ('http://api.wunderground.com/api/{key}/'
                        '{api}/q/{state}/{city}.json')

    # Get API key from system variable
    WUNDERGROUND_KEY = os.environ['WUNDERGROUND_KEY']

    # Base email message string
    # TODO: the language from wunderground is a bit awkward here sometimes
    MSG_STRING = (u'Right now in {city}, current conditions are: {current} '
                    u'with a temperature of {curr_temp}\u00B0F.\n\n'
                    u'Enjoy a discount of 20%% off any item with code {code}!')

    def handle(self, *args, **options):

        for loc in Account.objects.distinct('location'):

            # Retrieve city/state from location FK object
            city = loc.location.city
            state = loc.location.state

            # Build wunderground URL for city
            # Leave api field to fill in for the two needed below
            url = self.WUNDERGROUND_URL.format(
                key=self.WUNDERGROUND_KEY,
                api='{api}',
                state=state,
                city=city
            )

            # Get current conditions for location
            conditions = (requests.get(url.format(api='conditions')).json()
                .get('current_observation'))

            curr_temp = conditions.get('temp_f')
            precip = conditions.get('precip_1hr_in')
            current = conditions.get('weather').lower()

            # Get average temperature for location
            avg_temp = float(requests.get(url.format(api='almanac')).json()
                .get('almanac').get('temp_high').get('normal').get('F'))

            # Determine if weather is good or bad
            if curr_temp < avg_temp - 5 or float(precip) > 0:
                subj = 'Not so nice out? That\'s okay, enjoy a discount on us.'
                code = 'SUNSHINE20'
            elif curr_temp > avg_temp + 5 or 'sun' in current:
                subj = 'It\'s nice out! Enjoy a discount on us.'
                code = 'BEAUTIFULDAY20'
            else:
                subj = 'Enjoy a discount on us.'
                code = 'SAVE20'

            # Format message string with real values
            message = self.MSG_STRING.format(city=city, current=current,
                curr_temp=curr_temp, code=code)

            # Use city ID to find all emails associated with current city
            city_emails = [x.email_address for x
                    in Account.objects.filter(location_id=loc.location_id)]

            send_mail(subj, message, 'bmleonard33+weather@gmail.com',
                city_emails, fail_silently=False)
