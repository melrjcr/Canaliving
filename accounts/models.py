from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from website.models import Products

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50),
    last_name = models.CharField(max_length=50),
    email = models.EmailField(max_length=200),
    phonenumber = PhoneNumberField(blank=True),
    adresses = models.ManyToManyField (
                                        'Address',
                                        through='AddressInfo',
                                        # through_fields=('address','profile')
                                        )
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user

# def post_save_profile_create(sender, instance, created, *args, **kwargs):
#     if created:
#         Profile.objects.get_or_create(user=instance)
#
#     user_profile, created = Profile.objects.get_or_create(user=instance)
#
#     if user_profile.stripe_id is None or user_profile.stripe_id == '':
#         new_stripe_id = stripe.Customer.create(email=instance.email)
#         user_profile.stripe_id = new_stripe_id['id']
#         user_profile.save()
#     post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

class Address(models.Model):

    address = models.CharField(max_length=100),
    Address2 = models.CharField(max_length=100),
    City = models.CharField(max_length=70),
    State = models.CharField(max_length=50),
    PostCode = models.CharField(max_length=7),
    Country = models.CharField(max_length=50),

    def __str__(self):
        return self.address

class AddressInfo(models.Model):

    HOME_ADDRESS = 1
    SHIPPING_ADDRESS = 2

    TYPE_ADDRESS_CHOICES = (
        (HOME_ADDRESS, "Home address"),
        (SHIPPING_ADDRESS, "Shipping address"),
    )
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    # This is the field you would use for know the type of address.
    address_type = models.PositiveIntegerField(choices=TYPE_ADDRESS_CHOICES)