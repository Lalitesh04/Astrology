from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from payment_app.models import Payment
from django.db.models import Sum, Q

from user.models import Admin


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


def changepassword(request):
    if "admin_name" in request.session:
        adminname = request.session["admin_name"]
    else:
        return redirect("login")

    if request.method == "POST":
        opwd = request.POST.get("opwd")
        npwd = request.POST.get("npwd")
        admin = Admin.objects.filter(Q(name=adminname) & Q(password=opwd)).first()

        if admin:
            if opwd == npwd:
                message = "New password cannot be the same as the old password."
            else:
                admin.password = npwd
                admin.save()
                message = "Password changed successfully."

            return render(request, "adminchangepwd.html", {"admin": adminname, "message": message})
        else:
            message = "Incorrect old password. Please try again."
            return render(request, "adminchangepwd.html", {"admin": adminname, "message": message})

    return render(request, "adminchangepwd.html", {"admin": adminname})
