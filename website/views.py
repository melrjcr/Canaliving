from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from shopping_cart.models import Order

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .Forms import ContactForm

# Create your views here.
from .models import Products

@login_required
def product_list(request):
    object_list = Products.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "products/product_list.html", context)


def template(request):
    return render(request, 'website/template.html')

def home_page(request):

    products = Products.objects.all()

    return render(request, 'website/index.html', {'products':products})


def catalogue(request):
    products = Products.objects.all()

    return render(request, 'website/catalogue.html',{'products':products})

def about_page(request):
    return render(request, 'website/about.html')


# <!--Contact Page-->
def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['melreyesj@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            content = {
                'title': 'You email has been Successfully Sent',
                'message': 'We will reply to your email as soon as possible'
            }
            return render(request, "website/contact.html", {'content': content})

    else:
        form = ContactForm()
        content = {
            'title': 'Leave Message',
            'message': 'Feel free to contact us here'
        }

    return render(request, "website/contact.html",{'form': form},{'content':content})

def fqas(request):
    return render(request, 'website/FQAs.html')
