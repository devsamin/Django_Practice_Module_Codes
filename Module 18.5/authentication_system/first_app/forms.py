from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldsname in self.fields:
            self.fields[fieldsname].help_text = None
            self.fields[fieldsname].widget.attrs.update({'class' : 'form-control'})
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for fieldsname in self.fields:
            self.fields[fieldsname].help_text = None
            self.fields[fieldsname].widget.attrs.update({'class' : 'form-control'})
    class Meta:
        model = User
        fields = ['username', 'password']

class CustomChangePassForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for fildename in self.fields:
            self.fields[fildename].help_text = None
            self.fields[fildename].widget.attrs.update({'class' : 'form-control'})
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']