from django.shortcuts import render
from find.views import find_detail_view
from .models import StripeCustomer
import stripe

def checkout(request):
    stripe.api_key = "sk_test_6YKv6Lyvteom4I7tWq8ebkY3"
    if request.method=="POST":
        print(request.POST)
        token = request.POST['stripeToken']
        email = request.POST['stripeEmail']

        # create stripe customer
        customer = stripe.Customer.create(
            email = email,
            source = token
        )

        customer_id = customer['id']

        # subscribe the customer
        stripe.Subscription.create(
            customer = customer_id,
            items = [
                {
                    'plan': 'weekly'
                }
            ]
        )

        # add customer to the database
        StripeCustomer.objects.create(
            customer_id=customer_id,
            customer_email=email
        )



    return render(request, 'payment/finish.html')
