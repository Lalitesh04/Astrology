from django.shortcuts import render

from payment_app.models import Payment


def adminchangepwd(request):
    adminname = request.session["admin_name"]
    return render(request, "userchangepwd.html", {"admin": adminname})


def adminhome(request):
    return render(request, "adminhome.html")


def viewfeedback(request):
    return render(request, "viewfeedback.html")


def users(request):
    return render(request, "users.html")


def adduser(request):
    return render(request, "adduser.html")


from django.db.models import Sum


def viewdonations(request):
    count = Payment.objects.count()
    payments = Payment.objects.all()

    # Calculate the total amount
    total_amount = Payment.objects.aggregate(Sum('amount'))['amount__sum']

    return render(request, "viewdonations.html", {"count": count, "payments": payments, "total_amount": total_amount})
