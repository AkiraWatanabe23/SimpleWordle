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
    if "tasks" not in request.session:
        request.session["tasks"] = []

    li_ans = list(NewTaskForm(request.POST))
    checking = [' '] * 5
    correct = 0

    get = list(input("5字の英単語を入力してください"))
    #異常な入力が入った場合は再入力
    if len(get) != 5:
        print("もう一度入力してください")
        return

    #判定処理
    for i in range(5):
        if get[i] in li_ans:
            if get[i] == li_ans[i]:
                correct += 1
                checking[i] = 'o'
            else:
                checking[i] = '△'

    #合っていたらクリア
    if correct == 5:
        print("Clear!!")

    #合っていなかったら現状を出力
    print(checking)

    return render(request, "game/game.html", {
        "tasks": request.session["tasks"]
    })
