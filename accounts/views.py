from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django import views
from .forms import SignUpForm
from .models import User
from snippets.models import Snippet
# Create your views here.

class SignUpView(views.View):
    def get(self,request):
        form = SignUpForm()
        return render(request,"accounts/signup.html",{"form":form})
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request,"accounts/signup.html",{"form":form})

class ProfileView(LoginRequiredMixin,views.generic.DetailView):
    template_name = 'accounts/base_profile.html'
    context_object_name = 'user'
    model = User
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return User.objects.filter(pk=pk)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user == self.object:
            context['snippets'] = self.request.user.snippets.all()
            return context
        context['snippets'] = self.object.snippets.filter(private=False)[:5]
        return context

class MainView(LoginRequiredMixin,views.View):
    def get(self,request):
        return render(request,"accounts/main.html")

class SearchView(LoginRequiredMixin,views.View):
    def get(self,request):
        slug = request.GET.get("search")
        users = None
        if slug:
            users = User.objects.filter(Q(username__icontains=slug)|Q(email__icontains=slug))
        return render(request,"accounts/search.html",{"users":users})

class UpdateProfileView(LoginRequiredMixin,views.generic.UpdateView):
    context_object_name = "user"
    model = User
    fields = ['first_name',"last_name","email"]
    template_name = "accounts/update.html"
    def get_success_url(self):
        return reverse("main")
        
    def get_object(self, *args, **kwargs):
        user = super(UpdateProfileView, self).get_object(*args, **kwargs)
        if user != self.request.user:
            raise PermissionDenied() #or Http404
        return user
