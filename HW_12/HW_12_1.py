# Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое
# и последнее вхождение буквы h, а также все символы, находящиеся между ними.

string = "А huge hungry honeyeater lives in a small apartment overlooking the river"
First_i = None
Last_i = None
char = len(string)
for i in range(char):
    if string[i] == 'h':
        First_i = i
        break
for j in range(char-1, 0, -1):
    if string[j] == 'h':
        Last_i = j
        break
if First_i:
    string_new = string[:First_i] + string[Last_i+1:]
    print(string_new)
else:
    print('Буквы h нет')
