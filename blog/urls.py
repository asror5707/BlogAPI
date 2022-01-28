from django.contrib import admin
from django.urls import path
from blog_app.views import about,BlogAPIView,home,maqola,maqola1,LoginView,ReqisterView,Logout
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/', obtain_auth_token),
    path('login/', LoginView.as_view(),name='login'),
    path('reg/',ReqisterView.as_view(),name='reg'),
    path('', home,name='home'),
    path('blog/', BlogAPIView.as_view() ,name='blog'),
    path('about/', about),
    path('maqola/', maqola,name='maqola'),
    path('maqola/<int:son>', maqola1,name="maqola1"),
    path('logout/', Logout, name='logout'),

]
