from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Info
from django.views.generic import ListView

# Create your views here.

class PostList(ListView):
   model = Info
   ordering = '-pk'
   paginate_by = 1


def calc_time(ms):
   second = int(int(ms) / 1000)
   ms = int((int(ms) % 1000) / 100)
   minute = int(second / 60)
   second %= 60
   hour = int(minute / 60)
   minute %= 60

   result = ""
   if hour > 0:
      result += str(hour) + '시간 '
   if minute > 0:
      result += str(minute) + '분 '
   if second > 0:
      if ms > 0 :
         result += str(second) + '.' + str(ms) + '초 '
      else :
         result += str(second) + '초 '
   return result


def createform(request):
   std = Info()
   std.battery = request.GET['battery']
   std.color = request.GET['color']
   std.runtime = request.GET['runtime']
   std.runtime = calc_time(std.runtime)
   std.save()






   return redirect('http://127.0.0.1:8000#about')


def signin(request):
    if request.method == "GET":
        return redirect('webapp:index')

    elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('webapp:index')
            else:
                return redirect('webapp:index')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('webapp:index')

