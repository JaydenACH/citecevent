from django.shortcuts import render
from .models import Emails
from datetime import datetime


def index(request):
    return render(request, "countdown_website/homepage.html")


def recordemail(request):
    email = request.POST["email"]
    reg_name = request.POST["reg_name"]
    reg_com = request.POST["reg_com"]
    today = datetime.today()
    today = today.strftime("%Y/%m/%d %H:%M:%S")
    email_log = Emails(
        email=email,
        reg_time = today,
        reg_name=reg_name,
        reg_com=reg_com,
    )
    email_log.save()
    return render(request, "countdown_website/homepage.html")