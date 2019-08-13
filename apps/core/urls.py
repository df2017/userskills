from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import LoginView, LogoutView, HomeView, TestList, SolutionCreate

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', login_required(HomeView.as_view()), name='home'),
    path('test/', login_required(TestList.as_view()), name='tests'),
    path('create/', login_required(SolutionCreate.as_view()), name='create'),
]
