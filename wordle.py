'''wordleテスト'''
from random import choice
import cgi

#単語リスト(開始時にこの中からランダムに選ぶ)
words = ["above", "adult", "adapt", "brave", "build",
         "crime", "drive", "entry", "empty", "giant",
         "point", "snake", "unity", "slime", "false",
         "earth", "mouse", "horse", "smart", "clean",
         "shift", "space", "enter", "sweat", "berry",
         "print", "movie", "break", "lemon", "smile",
         "paint", "order", "click", "shoes", "shirt",
         "field", "apple", "grape", "sweet", "water"]
form = cgi.FieldStorage()
get = list(form.getfirst('input'))

def check(ans) -> bool:
    '''入力が答えと合っているか判定'''
    li_ans = list(ans)
    checking = [' '] * 5
    correct = 0

    #異常な入力が入った場合は再入力
    if len(get) != 5:
        print("もう一度入力してください")
        return

    #判定処理
    for i in range(5):
        if get[i] in ans:
            if get[i] == li_ans[i]:
                correct += 1
                checking[i] = 'o'
            else:
                checking[i] = '△'

    #合っていたらクリア
    if correct == 5:
        print("Clear!!")
        return True

    #合っていなかったら現状を出力
    print(checking)
    return False

if __name__ == '__main__':
    answer = choice(words)

    while True:
        check(answer)
