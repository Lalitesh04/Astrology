import json
import random

# import matplotlib
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import register, Feedback, Admin
# import pandas as pd
# import matplotlib.pyplot as plt
# #import mpld3


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def registration(request):
    return render(request, "register.html", )


def checklogin(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        user = register.objects.filter(Q(username=uname, password=pwd)).first()
        admin = Admin.objects.filter(Q(username=uname) & Q(password=pwd)).first()

        if user:
            request.session["user_name"] = user.name
            return render(request, "userhome.html", {"uname": user})
        if admin:
            request.session["admin_name"] = uname
            ucount = register.objects.count()
            fcount = Feedback.objects.count()
            return render(request, "adminhome.html", {"admin": admin, "ucount": ucount, "fcount": fcount})
        else:
            messages.error(request, "invalid Login")
            return redirect('login')
    else:
        messages.error(request, "invalid Login")
        return redirect('login')


def adminhome(request):
    return render(request, "adminhome.html")


def login(request):
    return render(request, "userlogin.html")


def feedback_form(request):
    return render(request, 'feedbackform.html')


def submit_feedback(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('phoneno')
        feedback_text = request.POST.get('feedback')
        is_happy = 'happy' in request.POST
        feedback = Feedback(
            customer_name=customer_name,
            email=email,
            contact=contact,
            feedback=feedback_text,
            happy=is_happy
        )
        feedback.save()
        messages.info(request, "FeedBack Submitted Successfully")
        return redirect(feedback_form)


def userhome_render(request):
    uname = request.session["user_name"]
    return render(request, "userhome.html", {"uname": uname})


def checksign(request):
    return render(request, "checksign.html")


zodiac_horoscopes = {
    "Capricorn": "Hello, dear Capricorn. Pay attention, because you're going to like what you read. After the "
                 "hellscape that was 2020, this year puts your career and money center stage. In particular, "
                 "you will benefit from leaning into what you love and whatever it is that brings you the most "
                 "satisfaction. While we all must take what we can get in this economy, this year asks you to take "
                 "risks and reap the financial rewards.",
    "Aquarius": "You care about your community, Aquarius, and the events of 2020 gave you plenty of chances to keep "
                "busy by lending a hand. Whether you became your family's point person and organizer of Zoom holidays "
                "or dove into activism, you likely stayed so busy tending to others that you forgot about your own "
                "needs. Now, 2021 shines a spotlight on you, precious water bearer, and it's time to step into it.",
    "Pisces": "Your psychic and empathic abilities are what make you so magical, Pisces, but the weight of the world "
              "in 2020 became too much for you. As a result, you probably used stay-at-home orders to retreat a "
              "little bit too much. This year asks you to come out of your fishbowl and grace us with your humor and "
              "pretty face. Expect major changes in your friend group that overlap with your love life. Are you "
              "secretly in love with your best friend?",
    "Aries": "2021 is major for your love life Aries, but only if you drop the drama. As the world starts to heal "
             "from the pains of 2020, you need to let go of any habits that may have developed while isolating that "
             "no longer serve you. This year brings opportunities for magnificent love, as long as you don't ruin it "
             "with an infamous Aries temper tantrum.",
    "Taurus": "Last year left you with plenty of time to think, Taurus, and 2021 wants you to act on your desires "
              "because you are worth it. This will likely manifest most obviously in your professional life, "
              "so don't be surprised if you leave one job for something bigger and better that fills your soul. "
              "Practice self-care and don't for a second forget your worth, or else you could risk missing out on an "
              "opportunity made for you.",
    "Gemini": "Have you ever been so busy that you wished you could clone yourself just to get everything done? "
              "That’s the Gemini experience in a nutshell. Appropriately symbolized by the celestial twins, "
              "this air sign was interested in so many pursuits that it had to double itself.",
    "Cancer": "2020 kept you so busy that you started crab-walking in circles, Cancer. You're an expert when it comes "
              "to taking care of other people, but 2021 asks you to let other people take care of you. This may be "
              "hard to do, as it can be difficult to admit when you're vulnerable, but I pinkie promise that it's for "
              "your own health and happiness.",
    "Leo": "You are ruled by the sun, Leo, so you were actually born to be in the spotlight. Social distancing was "
           "hard for everyone, but it's possible it affected your sign the most, leaving you to get creative. As the "
           "world starts to heal in 2021, you'll feel like a lion trapped in a cage bursting to get out. When you do, "
           "you'll want to say yes to every date and every opportunity, but beware of short-term thinking, "
           "Leo. Your 2021 mission is to practice patience and be discerning.",
    "Virgo": "As the healer of the zodiac, 2020 kept you busy, Virgo. When you weren't out there giving out masks and "
             "delivering meals you became an emotional net for friends and family, and it's likely you over-extended "
             "yourself. This year, it may be helpful to work through the trauma you've experienced, either by getting "
             "a therapist, meditating, or simply making more time for long walks. Doing things that make you feel "
             "calm and balanced may just help you erect boundaries to bring in healthier relationships.",
    "Libra": "As the sign of partnerships and balance, 2020 did a number on you. Not only was the world total chaos, "
             "but you had to primarily switch to flirting via sext, which while fun, is not the same as batting your "
             "eyelashes in real life. However, you still managed to get your fair share of attention. This year "
             "offers a chance at healthy, stable, and long-term love, you just need to keep your eyes and heart open.",
    "Scorpio": "As the sign of partnerships and balance, 2020 did a number on you. Not only was the world total "
               "chaos, but you had to primarily switch to flirting via sext, which while fun, is not the same as "
               "batting your eyelashes in real life. However, you still managed to get your fair share of attention. "
               "This year offers a chance at healthy, stable, and long-term love, you just need to keep your eyes and "
               "heart open.",
    "Sagittarius": "Last year was rough on everyone, Sagittarius, but you felt it super hard. As a fire sign who "
                   "loves to be the life of the party, when parties were canceled, you may have wondered what the "
                   "point of it all was — and given into doom-scrolling as a substitute. This year, you'll find "
                   "purpose again. 2021 asks you to prioritize your health, both mental and emotional. You'll feel "
                   "much better when you start listening and tending to your needs."
}


def horoscope(request):
    return render(request, "horoscope.html")


def checkhoroscope(request):
    date = int(request.POST["date"])
    month = int(request.POST["month"])
    zodiacsign = get_zodiac_sign(month, date)
    prediction = zodiac_horoscopes[zodiacsign]
    print(date, month, zodiacsign)
    return render(request, "horoscope.html", {"prediction": prediction, "zodiac": zodiacsign})


def get_zodiac_sign(month, date):
    if (month == 3 and date >= 21) or (month == 4 and date <= 19):
        return "Aries"
    elif (month == 4 and date >= 20) or (month == 5 and date <= 20):
        return "Taurus"
    elif (month == 5 and date >= 21) or (month == 6 and date <= 20):
        return "Gemini"
    elif (month == 6 and date >= 21) or (month == 7 and date <= 22):
        return "Cancer"
    elif (month == 7 and date >= 23) or (month == 8 and date <= 22):
        return "Leo"
    elif (month == 8 and date >= 23) or (month == 9 and date <= 22):
        return "Virgo"
    elif (month == 9 and date >= 23) or (month == 10 and date <= 22):
        return "Libra"
    elif (month == 10 and date >= 23) or (month == 11 and date <= 21):
        return "Scorpio"
    elif (month == 11 and date >= 22) or (month == 12 and date <= 21):
        return "Sagittarius"
    elif (month == 12 and date >= 22) or (month == 1 and date <= 19):
        return "Capricorn"
    elif (month == 1 and date >= 20) or (month == 2 and date <= 18):
        return "Aquarius"
    else:
        return "Pisces"


def contactus(request):
    return render(request, "contactus.html")


def userchangepwd(request):
    uname = request.session["user_name"]
    return render(request, "userchangepwd.html", {"uname": uname})


@login_required
def userupdatepwd(request):
    uname = request.session["user_name"]
    print(uname)
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    flag = register.objects.filter(Q(name=uname) & Q(password=opwd))
    if flag:
        register.objects.filter(name=uname).update(password=npwd)
        msg = "Password Updated Successfully"
    else:
        msg = "Old Password is Incorrect"
    return render(request, "userchangepwd.html", {"uname": uname, "message": msg})


# def feedback_report(request):
#     # Query the database for feedback data
#     feedback_data = Feedback.objects.all()
#     matplotlib.use('agg')
#     # Convert data to a Pandas DataFrame
#     feedback_df = pd.DataFrame(list(feedback_data.values()))

#     # Create a Matplotlib chart
#     plt.figure(figsize=(10, 5))
#     feedback_df['happy'].value_counts().plot(kind='bar')
#     plt.title('Satisfaction Level')
#     plt.xlabel('Satisfaction')
#     plt.ylabel('Count')

#     # Convert the Matplotlib chart to an interactive HTML format
#     chart_html = mpld3.fig_to_html(plt.gcf())

#     context = {
#         'chart_html': chart_html,
#         'summary_stats': feedback_df.describe().to_html(),
#     }

#     return render(request, 'report.html', context)


def logout_view(request):
    response = HttpResponse()
    response['Cache-Control'] = 'no-store'
    return redirect('login')


def viewuser(request):
    usersdata = register.objects.all()
    count = register.objects.count()
    return render(request, "viewuser.html", {"userdata": usersdata, "count": count})


def checkregistion(request):
    if request.method == "POST":
        name = request.POST["name"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        phoneno = request.POST["phoneno"]

        new_register = register(name=name, gender=gender, email=email, username=username, password=password,
                                contact=phoneno)
        new_register.save()
        messages.info(request, " Registered inserted SuccessFully")
        return render(request, "adduser.html")


def deleteuser(request):
    usersdata = register.objects.all()
    count = register.objects.count()
    return render(request, "deleteuser.html", {"userdata": usersdata, "count": count})


def deleteuserid(request, uid):
    register.objects.filter(id=uid).delete()
    return redirect("deleteuser")


def viewfeedback(request):
    count = Feedback.objects.count()
    feedback = Feedback.objects.all()
    return render(request, "viewfeedback.html", {"count": count, "data": feedback})


def userregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        phoneno = request.POST["phoneno"]

        new_register = register(name=name, gender=gender, email=email, username=username, password=password,
                                contact=phoneno)
        new_register.save()
        messages.info(request, " Data inserted SuccessFully")
        return render(request, "userlogin.html")
    return redirect(register)


def adminhome(request):
    admin = request.session["admin_name"]
    count = register.objects.count()
    fd = Feedback.objects.count()
    return render(request, "adminhome.html", {"admin": admin, "count": count, "fd": fd})


def rasi(request):
    if request.method == "POST":
        svg_data = None
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        date = int(request.POST.get('date'))
        hours = int(request.POST.get('hours'))
        minutes = int(request.POST.get('minutes'))
        url = "https://json.freeastrologyapi.com/horoscope-chart-svg-code"
        payload = json.dumps({
            "year": year,
            "month": month,
            "date": date,
            "hours": hours,
            "minutes": minutes,
            "seconds": 0,
            "latitude": 17.38333,
            "longitude": 78.4666,
            "timezone": 5.5,
            "config": {
                "observation_point": "topocentric",
                "ayanamsha": "lahiri"
            }
        })

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'sVhJNyXEho1paRvj6HgqK61jX3Xfef1xaGkD982m'
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            # Parse the JSON response
            response_json = response.json()
            # Extract SVG data from the response
            svg_data = response_json.get("output", "")

            if svg_data:
                # Pass SVG data to the template
                return render(request, "checksign.html", {"svg_data": svg_data})

        return render(request, "checksign.html", {"svg_data": None})


def chart(request):
    return render(request, "chart.html")


def marriage(request):
    return render(request, "marriage.html")


def ForgetPassword(request):
    return render(request, "forgetpassword.html")


def generate_otp():
    otp = ""
    for _ in range(4):
        otp += str(random.randint(0, 9))
    return otp


def checkforgot(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        try:
            value = register.objects.get(email=email)
            # print(value)
            if value:
                otp = generate_otp()
                request.session["otp"] = otp
                subject = 'Your OTP for the change Password'
                message = "otp:" + otp
                request.session['femail'] = email
                send_mail(subject, message, 'lalitesh.mupparaju04@gmail.com', [email], fail_silently=False)
                return render(request, "otpverify.html")
        except register.DoesNotExist:
            messages.info(request, "Email not registered")
            return render(request, "register.html")
        except Exception as e:
            print(e)  # Print the actual exception for debugging purposes
            return HttpResponse("An error occurred")


def checkotp(request):
    if request.method == "POST":
        userotp = request.POST["userotp"]
        otp = request.session["otp"]

        print(otp, userotp)
        if userotp == otp:
            return render(request, 'changepass.html')
        else:
            messages.info(request, "Otp MisMatch")
            return render(request, "otpverify.html")


def changepass(request):
    if request.method == "POST":
        newpassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')
        femail = request.session['femail']
        print(newpassword, confirmPassword)
        if newpassword == confirmPassword:
            user = register.objects.get(email=femail)
            user.password = newpassword
            user.save()
            return render(request, 'userlogin.html')
        else:
            messages.info(request, "Password MisMatch")
            return render(request, "changepass.html")
