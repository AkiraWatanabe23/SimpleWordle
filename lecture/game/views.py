'''実行する内容'''
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    '入力内容の追加、反映'
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    '''Listの表示'''
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "game/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    '''Listに要素を追加する'''
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("game:index"))
        else:
            return render(request, "game/add.html", {
                "form": form
            })

    return render(request, "game/add.html", {
        "form": NewTaskForm()
    })

def check(request):
    '''判定用の関数'''
    return render(request, "game/index.html")
