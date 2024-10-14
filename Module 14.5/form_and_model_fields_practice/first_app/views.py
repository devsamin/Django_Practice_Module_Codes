from django.shortcuts import render,redirect
from .forms import ContactForm1
from .models import ModelForm
# Create your views here.



def contact1(request):
    if request.method == 'POST':
        form = ContactForm1(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                f = form.cleaned_data['file'] # Access upload file
                with open('first_app/upload/' + f.name, 'wb+') as destination:  # Save the file
                    for chunk in f.chunks():
                        destination.write(chunk)

            print(form.cleaned_data)
            return redirect('contact1page')
    else:
        form = ContactForm1()

    return render(request, 'contact1.html', {'Form' : form})

def contact2(request):
    form = ModelForm.objects.all()

    return render(request, 'contact2.html', {'data' : form})