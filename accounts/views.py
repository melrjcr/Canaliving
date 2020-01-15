from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from shopping_cart.models import Order
from .forms import AddressForm, RegistrationForm
from .models import Profile, AddressInfo


def profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_addresses = AddressInfo.objects.filter(owner=my_user_profile)
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_addresses': my_addresses,
        'my_orders': my_orders
    }

    return render(request, "profile.html", context)

class registration(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/profile'

class Address(CreateView):
    form_class = AddressForm
    template_name = 'register.html'
    success_url = '/profile'


