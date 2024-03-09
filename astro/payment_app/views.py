# payment_app/views.py

from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from .models import Payment
from django.db import transaction
import razorpay
from django.conf import settings


class PaymentForm(forms.Form):
    name = forms.CharField()
    amount = forms.IntegerField(min_value=1)


def initiate_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
            payment_data = {
                "amount": amount,
                "currency": "INR",
                "receipt": "order_receipt",
                "notes": {
                    "email": "user_email@example.com",
                },
            }

            try:
                order = client.order.create(data=payment_data)
            except razorpay.errors.RazorpayError as e:
                return JsonResponse({"error": str(e)})

            response_data = {
                "id": order["id"],
                "amount": order["amount"],
                "currency": order["currency"],
                "key": settings.RAZORPAY_API_KEY,
                "name": "AstroPrediction",
                "description": "Payment for Your Product",
                "image": static("images/logo.png"),
            }

            # Save payment details in the database within a transaction
            with transaction.atomic():
                new_payment = Payment(name=name, amount=amount, orderid=order["id"])
                new_payment.save()

            # Return JSON response with payment details
            return JsonResponse(response_data)
        else:
            # Return JSON response for invalid form data
            return JsonResponse({"error": "Invalid form data"})

    # Render the payment.html template for GET requests
    return render(request, "payment.html")


def payment_success(request):
    # Render the payment_success.html template
    return render(request, "payment_success.html")


def payment_failed(request):
    # Render the payment_failed.html template
    return render(request, "payment_failed.html")
