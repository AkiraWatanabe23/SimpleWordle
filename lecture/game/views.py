'''実行する内容'''
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    '''Listの表示'''
    return render(request, "game/index.html", {
        "tasks": tasks
    })

def add(request):
    '''Listに要素を追加する'''
    return render(request, "game/add.html")
    