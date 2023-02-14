'''実行する内容'''
import random
# from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.urls import reverse

#単語リスト(開始時にこの中からランダムに選ぶ)
words = ["above", "adult", "adapt", "brave", "build",
         "crime", "drive", "entry", "empty", "giant",
         "point", "snake", "unity", "slime", "false",
         "earth", "mouse", "horse", "smart", "clean",
         "shift", "space", "enter", "sweat", "berry",
         "print", "movie", "break", "lemon", "smile",
         "paint", "order", "click", "shoes", "shirt",
         "field", "apple", "grape", "sweet", "water"]

#この変数が、毎回変化している可能性アリ(それは困る)
answer = random.choice(words)

# class NewTaskForm(forms.Form):
#     '入力内容の追加、反映'
#     task = forms.CharField(label="5字の英単語を入力してください")

# Create your views here.
def home(request):
    '''最初の入力かどうか、入力の判定'''
    if 'guess' in request.session:
        guess = request.session['guess']
    else:
        guess = None

    if request.method == 'POST':
        letter_guess = request.POST.get('letter_guess', '')
        if letter_guess:
            letter_guess = letter_guess.lower()
            if len(letter_guess) == 1 and letter_guess.isalpha():
                if guess:
                    guess += letter_guess
                else:
                    guess = letter_guess
                request.session['guess'] = guess

    if guess:
        #answer = random.choice(words)
        letters = [letter if letter in guess else '_' for letter in answer]
        game_over = '_' not in letters
    else:
        #answer = None
        letters = None
        game_over = False

    return render(request, 'game/play.html', {
        'letters': letters,
        'game_over': game_over,
        'guess': guess
    })

def reset(request):
    '''リセット'''
    request.session.flush()
    return HttpResponseRedirect('/')

# def check(get):
#     '''判定用の関数'''
#     li_ans = list(answer)
#     checking = [' '] * 5
#     correct = 0

#     get_value = list(get)
#     values = get_value[0][90:len(str(get_value[0]))].decode('utf-8')
#     #異常な入力が入った場合は再入力
#     # if len(get) != 5:
#     #     return render(request, "game/play.html")

#     #判定処理
#     for i in range(5):
#         if values[i] in li_ans:
#             if values[i] == li_ans[i]:
#                 correct += 1
#                 checking[i] = 'o'
#             else:
#                 checking[i] = '△'

#     #合っていたらクリア
#     if correct == 5:
#         view_result(True, "Clear!")

#     #合っていなかったら現状を出力
#     view_result(False, checking)

# def view_result(request, result: bool):
#     '''判定結果を返す関数(ここでは、renderを返したい)'''
#     if "results" not in request.session:
#         request.session["results"] = []

#     if result:
#         return render(request, "game/clear.html", {
#             "results": request.session["results"]
#         })
#     else:
#         return render(request, "game/retry.html", {
#             "results": request.session["results"]
#         })


# def play(request):
#     '''テスト'''
#     if request.method == "POST":
#         #form = NewTaskForm(request.POST)
#         form = NewTaskForm()
#         if form.is_valid():
#             #form.cleaned_dataがDictだったため、taskは指定部分のvalueであると予想している
#             result = form.cleaned_data["result"]
#             request.session["results"] += [result]
#             #↓ここの条件文を修正
#             if check(str(result)):
#                 return HttpResponseRedirect(reverse("result"))
#             else:
#                 return HttpResponseRedirect(reverse("play"))
#         else:
#             return render(request, "game/play.html", {
#                 "form": form
#             })

#     return render(request, "game/play.html", {
#         "form": NewTaskForm()
#     })
