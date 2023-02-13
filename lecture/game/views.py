'''実行する内容'''
from random import choice
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#単語リスト(開始時にこの中からランダムに選ぶ)
words = ["above", "adult", "adapt", "brave", "build",
         "crime", "drive", "entry", "empty", "giant",
         "point", "snake", "unity", "slime", "false",
         "earth", "mouse", "horse", "smart", "clean",
         "shift", "space", "enter", "sweat", "berry",
         "print", "movie", "break", "lemon", "smile",
         "paint", "order", "click", "shoes", "shirt",
         "field", "apple", "grape", "sweet", "water"]

answer = choice(words)

class NewTaskForm(forms.Form):
    '入力内容の追加、反映'
    task = forms.CharField(label="5字の英単語を入力してください")

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

def check(get):
    '''判定用の関数'''
    li_ans = list(answer)
    checking = [' '] * 5
    correct = 0

    get_value = list(get)
    #↓これはbytesを入力された文字列に変更
    aaa = get_value[0][90:len(str(get_value[0]))-1].decode('utf-8')
    #異常な入力が入った場合は再入力
    # if len(get) != 5:
    #     return render(request, "game/play.html")

    #判定処理
    for i in range(5):
        if aaa[i] in li_ans:
            if aaa[i] == li_ans[i]:
                correct += 1
                checking[i] = 'o'
            else:
                checking[i] = '△'
        else:
            checking[i] = 'x'

    #合っていたらクリア
    if correct == 5:
        return True, "Clear!"

    #合っていなかったら現状を出力
    return False, checking

def play(request):
    '''テスト'''
    if request.method == "POST":
        #form = NewTaskForm(request.POST)
        form = NewTaskForm()
        if form.is_valid():
            #form.cleaned_dataがDictだったため、taskは指定部分のvalueであると予想している
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            #↓ここの条件文を修正
            if check(str(task)):
                return HttpResponseRedirect(reverse("game:check"))
            else:
                return HttpResponseRedirect(reverse("game:play"))
        else:
            return render(request, "game/play.html", {
                "form": form
            })

    return render(request, "game/play.html", {
        "form": NewTaskForm()
    })
