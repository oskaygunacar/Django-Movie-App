from django import forms
from movie_app.models import Comments, Profile
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user', 'comment',]

class UserSignUpForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), validators=[MinLengthValidator(5, 'Please use at least 5 character long password')])

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password","email"]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileUpdateForm(forms.ModelForm):
    instagram = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please write your instagram username'}),required=False)
    twitter = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please write your twitter username'}),required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'info', 'instagram', 'twitter',]

class ChangeUserPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), validators=[MinLengthValidator(5, 'Please use at least 5 character long password')])
    old_password_again = forms.CharField(widget=forms.PasswordInput(), validators=[MinLengthValidator(5, 'Please use at least 5 character long password')])
    new_password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(5, 'Please use at least 5 character long password')])

    def clean(self):
        password1 = self.cleaned_data.get('old_password')
        password2 = self.cleaned_data.get('old_password_again')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords are not identical! Please check and try again.')
        
        return self.cleaned_data
    

class DeleteAccountForm(forms.Form):
    number = forms.IntegerField()
    confirm_number = forms.IntegerField()

    def clean(self):
        number = self.cleaned_data.get('number')
        number2 = self.cleaned_data.get('confirm_number')

        if number and number2 and number != number2:
            raise ValidationError('Validation numbers are not identical')
        
        return self.cleaned_data