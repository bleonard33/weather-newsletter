from django.forms import ModelForm
from models import Account


class SignupForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email_address', 'location']
