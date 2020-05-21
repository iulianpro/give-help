from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from accounts.models import Donor


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True)
    last_name = forms.CharField(
        max_length=30,
        required=True)
    password1 = forms.CharField(
        min_length=6,
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Retype Password",
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(
                u'An account with this email already exists')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Fill in the same password in both fields")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            "phone_number",
            "postcode",
            "town_city",
            "street_address1",
            "street_address2",
            "county",
        ]
