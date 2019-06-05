import string

def Forbidden(text):
    forbidden = ('!', '?', ',', ':', '*', '#', '@', '№', '%', "'", '/', ' ', '.')
    newText = ''
    for i in text:
        if i not in forbidden:
            newText += i
    return newText.lower()

def reverse(text):
    text = Forbidden(text)
    return text[::-1].lower()

def palindromee(text):
    text = Forbidden(text)
    return text == reverse(text)

something = input()

print('Вы набрали {}'.format(something))
print('С Forbidden и lower() читается так: {}'.format(Forbidden(something)))
print('Реверс сделал из него {}'.format(reverse(something)))
if palindromee(Forbidden(something)):
    print('Это палиндром')
else:
    print('Это не палиндром')
