'''実行する内容'''
from django import forms
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    '追加内容の追加、反映'
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    '''Listの表示'''
    return render(request, "game/index.html", {
        "tasks": tasks
    })

def add(request):
    '''Listに要素を追加する'''
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "game/add.html", {
                "form": form
            })

    return render(request, "game/add.html", {
        "form": NewTaskForm()
    })
    