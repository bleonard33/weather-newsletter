from django.core.management.base import BaseCommand
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from signup.models import Account
import requests
import time
import os


class Command(BaseCommand):

    # Base wunderground URL
    WUNDERGROUND_URL = ('http://api.wunderground.com/api/{key}/'
                        '{api}/q/{state}/{city}.json')

    # Get API key from system variable
    WUNDERGROUND_KEY = os.environ['WUNDERGROUND_KEY']

    FROM_EMAIL = 'bmleonard33+weather@gmail.com'

    wunderground_api_calls = 0

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

            # Throttle wunderground API calls to 10/min for free plan
            # TODO: Upgrade API plan and remove entirely
            if self.wunderground_api_calls >= 10:
                time.sleep(60)

            # Get current conditions for location
            conditions = (requests.get(url.format(api='conditions')).json()
                .get('current_observation'))

            curr_temp = conditions.get('temp_f')
            precip = conditions.get('precip_1hr_in')
            current = conditions.get('weather').lower()

            # Get average temperature for location
            avg_temp = float(requests.get(url.format(api='almanac')).json()
                .get('almanac').get('temp_high').get('normal').get('F'))

            print city, curr_temp, avg_temp, precip, current

            self.wunderground_api_calls += 2

            # Determine if weather is good or bad
            # TODO: Dynamically generate coupon code and store in DB
            if curr_temp < avg_temp - 5 or float(precip) > 0:
                subj = 'Not so nice out? That\'s okay, enjoy a discount on us.'
                if curr_temp < avg_temp - 5:
                    code = 'COLD20'
                else:
                    code = 'SOGGY20'
            elif curr_temp > avg_temp + 5 or 'sun' in current:
                subj = 'It\'s nice out! Enjoy a discount on us.'
                code = 'BEAUTIFULDAY20'
            else:
                subj = 'Enjoy a discount on us.'
                code = 'SAVE20'

            # Use city ID to find all emails associated with current city
            city_emails = [x.email_address for x
                    in Account.objects.filter(location_id=loc.location_id)]

            context = {
                        'city': city,
                        'curr_temp': curr_temp,
                        'current': current,
                        'code': code
            }

            # Render plaintext and html emails with context
            plaintext = get_template('email.txt').render(context)
            html = get_template('email.html').render(context)

            # Send the message!
            message = EmailMultiAlternatives(subj, plaintext, self.FROM_EMAIL, city_emails)
            message.attach_alternative(html, "text/html")
            message.send()
