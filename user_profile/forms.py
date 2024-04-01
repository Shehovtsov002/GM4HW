from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserProfileForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False, widget=forms.FileInput())
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')))
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    biography = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    social = forms.URLField(required=False)
    country = forms.CharField(max_length=100, required=False)

    class Meta:
        model = models.UserProfile
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'date_birth',
            'gender',
            'avatar',
            'biography',
            'social',
            'country'
        )

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user
