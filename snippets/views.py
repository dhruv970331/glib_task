from django.shortcuts import render,redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.core.exceptions import PermissionDenied
from .models import Snippet
from .forms import SnippetForm,SnippetEditForm
from django import views
from accounts.models import User
# Create your views here.

class SnippetCreateView(LoginRequiredMixin,views.View):
    def get(self,request):
        form = SnippetForm()
        return render(request,"snippets/create.html",{"form":form})
    @transaction.atomic
    def post(self,request):
        data = request.POST.copy()
        data['owner'] = request.user
        form = SnippetForm(request.POST,owner = request.user)
        if form.is_valid():
            print("valid")
            snippet = form.save(commit = False)
            snippet.owner = request.user
            snippet.save()
            
            return redirect(reverse("snippets:snippet-detail",kwargs={"pk":snippet.id}))
        return render(request,"snippets/create.html",{"form":form})

class SnippetDetailView(LoginRequiredMixin,views.generic.DetailView):
    template_name = 'snippets/detail.html'
    context_object_name = 'snippet'
    model = Snippet
    def get_object(self, queryset=None):
        obj = super(SnippetDetailView, self).get_object(queryset=queryset)
        if obj.owner == self.request.user or not obj.private:
            return obj
        raise PermissionDenied()
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Snippet.objects.filter(pk=pk)

class SnippetListView(LoginRequiredMixin,views.generic.ListView):
    model = Snippet
    context_object_name = 'snippets'
    template_name = 'snippets/list.html'

    def get_queryset(self):
        print(self.request.user,self.kwargs)
        owner = User.objects.get(pk=self.kwargs['pk'])
        if owner == self.request.user:
            return owner.snippets.all()
        return owner.snippets.filter(private=False)

class SnippetEditView(LoginRequiredMixin,views.generic.UpdateView):
    form_class = SnippetEditForm
    model = Snippet
    template_name = 'snippets/edit.html'

    def get_form_kwargs(self):
        kwargs = super(SnippetEditView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    def get_success_url(self):
        view_name = 'snippets:snippet-detail'
        # No need for reverse_lazy here, because it's called inside the method
        return reverse(view_name, kwargs={'pk': self.kwargs['pk']})

    def get_object(self,queryset=None):
        snippet = Snippet.objects.get(pk=self.kwargs['pk'])
        if snippet.owner == self.request.user:
            return snippet
        raise PermissionDenied()