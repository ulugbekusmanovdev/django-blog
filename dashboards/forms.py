from django import forms
from home.models import Category, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ('slug', 'author', ) #slud author dan boshqasi


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions',)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions',)