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
        request.session['guess'] = guess
        #answer = None
        answer = random.choice(words.Words)

    if request.method == 'POST':
        letter_guess = request.POST.get('letter_guess', '')
        if letter_guess:
            letter_guess = letter_guess.lower()
            #str.isalpha()...文字列内の文字が全英字で、かつ1字以上のときTrue
            if letter_guess.isalpha():
                if guess:
                    guess += letter_guess
                else:
                    guess = letter_guess
                request.session['guess'] = guess

    if guess:
        #この内包表記の動きが分からない
        letters = [letter if letter in guess else '_' for letter in answer]
        game_clear = '_' not in letters
        print("aaa", answer)
    else:
        letters = None
        game_clear = False
        print("bbb", answer)

    return render(request, 'game/play.html', {
        'letters': letters,
        'game_clear': game_clear,
        'guess': guess
    })

def reset(request):
    '''リセット'''
    request.session.flush()
    return HttpResponseRedirect('/')
