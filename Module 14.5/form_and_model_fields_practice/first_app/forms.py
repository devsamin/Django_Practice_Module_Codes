from django import forms
import datetime

class ContactForm1(forms.Form):
    name = forms.CharField(max_length=20, initial='Your name')
    comment = forms.CharField(widget=forms.Textarea(attrs={'row' : 3}))
    email = forms.EmailField(required=False, label="Please enter your email address.")
    roll = forms.IntegerField(help_text="Enter 6 digit roll")
    file = forms.FileField(required=False)
    agree = forms.BooleanField(initial=True)
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    Birth_year_choice = ['2000', '2002', '2004']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years = Birth_year_choice))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    Favorite_color_choice = [
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('white', 'White')

    ]
    color_choice = forms.ChoiceField(choices=Favorite_color_choice)
