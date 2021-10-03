from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
name = []
class NameForm(forms.Form):
    name = forms.CharField(label="User name")
def index(request):
    return render(request, "hellouser/index.html", {
        'name': name
    })

def write(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            nam = form.cleaned_data["name"]
            name.append(nam)
            return HttpResponseRedirect(reverse("hellouser:index"))
        
        else:
            return render(request, 'hellouser/write.html', {
                "form": form
            })


    return render(request, "hellouser/write.html", {
        "form": NameForm()
    })