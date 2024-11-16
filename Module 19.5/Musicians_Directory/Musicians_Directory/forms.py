from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    comfirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = None

# class UserloginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username','password']
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'
#             self.fields[field].help_text = None

