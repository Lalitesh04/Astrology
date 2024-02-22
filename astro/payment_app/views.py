# payment_app/views.py

import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from .models import Payment
from django.db import transaction


def initiate_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST["amount"]) * 100
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data = {
            "amount": amount,
            "currency": "INR",
            "receipt": "order_receipt",
            "notes": {
                "email": "user_email@example.com",
            },
        }

        order = client.order.create(data=payment_data)

        # Include key, name, description, and image in the JSON response
        response_data = {
            "id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": settings.RAZORPAY_API_KEY,
            "name": "AstroPrediction",
            "description": "Payment for Your Product",
            "image": static("images/logo.png"),
        }

        # Save the payment record within a transaction block
        # new_payment = Payment(name=name, amount=amount, orderid=order["id"])
        # new_payment.save()

        return JsonResponse(response_data)

    return render(request, "payment.html")


def payment_success(request):
    name = request.POST.get('name')
    amount = int(request.POST["amount"]) * 100
    order_id = request.POST.get('order_id')
    new_payment = Payment(name=name, amount=amount, orderid=order_id)
    new_payment.save()
    return render(request, "payment_success.html")


def payment_failed(request):
    return render(request, "payment_failed.html")
