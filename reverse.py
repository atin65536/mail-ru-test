#HR мне сказала, что требуется python3.
#Однако, в тексте задании упоминается функция `xrange`, что наводит некую смуту.
#На всякий случай, предоставляю оба варианта.

#python2
def reverse(lst):
    for i in xrange(len(lst) / 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

#python3
def reverse(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst
