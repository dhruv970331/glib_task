from django import forms
from .models import Snippet
from accounts.models import User
from pprint import pprint

class SnippetForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        if kwargs.get("owner"):
            self.owner = kwargs.pop("owner")
        super().__init__(*args,**kwargs)
    class Meta:
        model = Snippet
        fields = ('description', 'name', 'language',"indent_mode","indent_value", 'code', 'private')

    def clean(self):
        cleaned_data = super().clean()
        """ This is the form's clean method, not a particular field's clean method """
        if self.owner:
            user = self.owner
        name = cleaned_data.get("name")
        if (Snippet.objects.filter(owner=user, name=name).count()):
            self.add_error("name","File with same name already exists")
            raise forms.ValidationError("File with same name already exists")
        cleaned_data['owner'] = user
        return cleaned_data

class SnippetEditForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        if kwargs.get("owner"):
            self.owner = kwargs.pop("owner")
        super().__init__(*args,**kwargs)
    class Meta:
        model = Snippet
        fields = ('description', 'name', 'language',"indent_mode","indent_value", 'code', 'private')

    def clean(self):
        cleaned_data = super().clean()
        """ This is the form's clean method, not a particular field's clean method """
        if self.owner:
            user = self.owner
        name = cleaned_data.get("name")
        if (Snippet.objects.filter(owner=user, name=name).count()) and Snippet.objects.get(name=name,owner=user)!=self.instance:
            self.add_error("name","File with same name already exists")
            raise forms.ValidationError("File with same name already exists")
        cleaned_data['owner'] = user
        return cleaned_data

        
