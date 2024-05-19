from django.shortcuts import render
from sampleapp.models import Book
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def base(request):
	data=Book.objects.all()
	return render(request,'base.html',{'b':data})
def index(request):
	return render(request,'index.html')
class SignUp(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'
def logout(request):
	return render(request,'logout.html')
class BooksDetailView(DetailView):
    model = Book
    template_name = 'details.html'
class BookCheckOutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'
# Create your views here.
