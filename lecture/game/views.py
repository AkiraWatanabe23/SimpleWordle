'''実行する内容'''
import random
from game import words
# from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.urls import reverse

#この変数が、毎回変化している可能性アリ(それは困る)
#answer = random.choice(words.Words)

# Create your views here.
def home(request):
    '''最初の入力かどうか、入力の判定'''
    if 'guess' in request.session:
        guess = request.session['guess']
        answer = random.choice(words.Words)
    else:
        guess = None
        answer = None

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
        letters = [letter if letter in guess else '_' for letter in answer]
        game_over = '_' not in letters
    else:
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
