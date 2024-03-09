from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from payment_app.models import Payment
from django.db.models import Sum


# from astro.user.models import Feedback


def adminchangepwd(request):
    adminname = request.session["admin_name"]
    return render(request, "adminchangepwd.html", {"admin": adminname})


def users(request):
    return render(request, "users.html")


def adduser(request):
    return render(request, "adduser.html")
def viewdonations(request):
    count = Payment.objects.count()
    payments = Payment.objects.all()

    # Calculate the total amount
    total_amount = Payment.objects.aggregate(Sum('amount'))['amount__sum']

    return render(request, "viewdonations.html", {"count": count, "payments": payments, "total_amount": total_amount})

