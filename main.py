# №25 Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

print(text := 'a d f g s a s s s d f g a')
text_list = text.split()
dict_count = dict()

for i in range(len(text_list)):
    if len(dict_count) == 0:
        dict_count[text_list[i]] = 0
    else:
        if text_list[i] in dict_count:
            dict_count[text_list[i]] += 1
            text_list[i] = text_list[i] + "_" + str(dict_count[text_list[i]])
        else:
            dict_count[text_list[i]] = 0

print(*text_list)
