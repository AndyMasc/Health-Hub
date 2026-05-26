from authenticate.models import Account
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.user.account.role == "Patient":
            return redirect("workspace:dashboard")
        elif request.user.account.role == "Doctor":
            return redirect("workspace:dashboard")
    return render(request, "home/index.html")
