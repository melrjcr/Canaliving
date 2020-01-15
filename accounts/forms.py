from django.forms import Form, CharField, EmailField, TextInput, PasswordInput, EmailInput, ModelForm, Select
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User

from accounts.models import Address


class RegistrationForm(Form):

    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control w-75',
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control w-75',
    }))
    phone_number = PhoneNumberField(label='Telephone'),
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-75',
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control w-75',
    }))

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'adress1': TextInput(attrs={'class': 'form-control w-75', }),
            'adress2': TextInput(attrs={'class': 'form-control w-75', }),
            'state': TextInput(attrs={'class': 'form-control w-75', }),
            'city': TextInput(attrs={'class': 'form-control w-75', }),
            'postcode': TextInput(attrs={'class': 'form-control w-75', }),
            'country': Select(attrs={'class': 'form-control w-75', }),
        }


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-50',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-50',
    }))