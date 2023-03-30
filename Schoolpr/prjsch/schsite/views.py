from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Students,Teachers,Items,kolUrok, Klass,Password1
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate
from  django.contrib.auth import login
from  django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import get_user
from django.contrib.auth.models import AbstractBaseUser



# Create your views here.
class GenreView:
    def getGenres(self):
        return Students.objects.all()
    def getGenr(self):
        return User.objects.all()
def logout_view(request):
    logout(request)
    return redirect("profile")
class login_view(View):
    """Отзывы"""
    def post(self, request):
        user = authenticate(request, username=self.request.POST.get("name"), password=self.request.POST.get("password"))
        if user is not None:
            login(request, user)
        else:
            HttpResponse("У вас тут пусто")
        return redirect('profile') 
def main(request):
    return render(request, 'schsite/main.html')
def err404(request, exception):
    return render(request, 'schsite/err404.html')
def logView(request):
    return render(request, 'schsite/login.html')

class regStud(GenreView ,ListView):
    model = Students
    queryset = Students.objects.all()
    template_name = "schsite/students.html"
    context_object_name = 'users'
class AddReview(View):
    """Отзывы"""
    def post(self, request):
        stud = User(username=self.request.POST.get("name"))
        stud.set_password(self.request.POST.get("password")) 
        stud.is_active = False
        stud.save()
        login(request, stud, backend='django.contrib.auth.backends.ModelBackend')
        item1 = Items.objects.all()
        stud2 = Klass.objects.get(klass=self.request.POST.get("klas"))
        stud1 = Students(image=self.request.FILES.get("img"), author=stud, klas=stud2) 
        stud1.save()
        for itm in item1:
            stud1.item.add(itm)
        stud1.save()
        return redirect('/')
class UrokAdd(View):
    """Отзывы"""
    def post(self, request):
        tud2 = Items.objects.get(title=self.request.POST.get("predmet[]"))
        stu = kolUrok.objects.create(title=self.request.POST.get("tema"), data=self.request.POST.get("date"), sdacha=self.request.POST.get("date1"), homework=self.request.POST.get("dom"), item=tud2, nomer=self.request.POST.get("nomer"))   
        a = self.request.POST.getlist("man[]")
        for t in a:
            print(t)
        try:
            for t in a:
                tud3 = Students.objects.get(id=t)
                stu.genres.add(tud3)
        except:
            tud3 = Students.objects.get(id=self.request.POST.getlist("man[]"))
            stu.genres.add(tud3)
        return redirect('/')
class AddPassword(View):
    """Отзывы"""
    def get(self, request):
        a = self.request.GET.get("pas")
        s = Password1.objects.get(0)
        print(s)
        if str(s) == a: 
            return redirect('/')
        else:
            return redirect("/profile")
class Profile(GenreView,View):
    def get(self, request):
        queryset = User.objects.all()
        return render(request, 'schsite/profile.html',{'student': queryset})
class Urok(GenreView,View):
    def get(self, request, slug):
        kalm = Items.objects.get(url=slug)
        return render(request, 'schsite/urok.html', {'urok': kalm})
class DetaUrok(GenreView,View):
    def get(self,request, slug, pk):
        klm = Items.objects.get(url=slug)
        kalm = kolUrok.objects.get(id=pk)
        return render(request, 'schsite/detaurok.html', {'urok': kalm})
def password(request):
    return render(request, "schsite/password.html")
class AddUrok(GenreView ,ListView):
    model = Teachers
    queryset = User.objects.all()
    template_name = "schsite/addUrok.html"
    context_object_name = 'users'

    
