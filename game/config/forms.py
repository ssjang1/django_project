from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):  # UserCreationForm : username, password1, password2
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)  # 아직 transaction을 하지 않음
        if commit:
            user.save()  # 실제 추가 commit
        return user