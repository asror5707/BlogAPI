from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import request
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .forms import MaqolaForm
from .models import Maqola,Rasm
from .serializers import MaqolaSerializer


def home(request):
    return render(request,'home.html')
class BlogAPIView(ListCreateAPIView):

    serializer_class = MaqolaSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        if request.user.is_authenticated:
            plans = Maqola.objects.filter(user=self.request.user)
            return plans
        else:
            return redirect('/login')
    def perform_create(self, serializer):
        if request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            return redirect('/login')

# class BlogView(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             m = Maqola.objects.filter(user=request.user)
#             forma = MaqolaForm()
#             return render(request, 'blog.html',{'maqola':m, "form":forma})
#         else:
#             return redirect('/login')
#
#     def post(self,request):
#         if request.user.is_authenticated:
#             forma = MaqolaForm(request.POST)
#             if forma.is_valid():
#                 forma.save()
#             return redirect('/blog')
#         else:
#             return redirect('/login')
def maqola1(request,son):
    if request.user.is_authenticated:
        maqola = Maqola.objects.get(id=son)
        rasm = Rasm.objects.filter(maqola=maqola)
        return render(request, 'maqola.html', {'m': maqola, 'r': rasm})
    else:
        return redirect('/login')

def maqola(request):
    return render(request,'maqola.html')
def about(request):
    return render(request,'about.html')
class LoginView(View):
    def get(self, request):
        return render(request,'login.html')
    def post(self,request):
        l = request.POST['login']
        parol = request.POST['parol']
        user = authenticate(request, username=l, password=parol)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('blog')

class ReqisterView(View):
    def get(self, request):
        return render(request,'register.html')
    def post(self,request):
        user = User.objects.create_user(
            username=request.POST['login'],
            password=request.POST.get('parol')
        )
        login(request, user)
        return redirect('login')
def Logout(request):
    logout(request)
    return redirect('login')

# Create your views here.
