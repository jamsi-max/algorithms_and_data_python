# Задание № 2
# Закодируйте любую строку по алгоритму Хаффмана.

# УФФФФ! Просто жара! Писал сам пользовался только теорией! И вот что вышло! Остался только вопрос для раскодировки
# придется сохранять где-то номера индексов символов что бы потом можно было по метсам их расставить! Ведь при
# использовании аже хэш функции я так понимаю сумма не изменится от перемены мест символов и поэтому
# получится абракадабра из символов при декодировке?
from collections import Counter

class Node:
    def __init__(self, value, frequency, left=None, right=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value} {self.frequency} L={self.left} R={self.right}'

def decoder(data):
    # Функция обхода всего дереваи наполняющая словарь
    def dec_obj(obj, code=''):
        if obj.left is None and obj.right is None:
            res_dic[obj.value] = code
            return 1
        dec_obj(obj.left, code=f'{code}0')
        dec_obj(obj.right, code=f'{code}1')
        return 1

    print('Двоичное представление символов: ', list(bin(ord(i)) for i in data))
    root_dic_buf = {}
    res_dic = {}
    while len(data) != 1:
        buf = Counter()
        a = ()
        for i in reversed(data.most_common()):
            if not a:
                a = i
                continue
            if len(buf) < 1:
                buf[a[0] + i[0]] = a[1] + i[1]
                if a[0] in root_dic_buf and i[0] in root_dic_buf:
                    root_dic_buf[a[0] + i[0]] = (Node(a[0] + i[0], a[1] + i[1], root_dic_buf[a[0]], root_dic_buf[i[0]]))
                elif a[0] in root_dic_buf and i[0] not in root_dic_buf:
                    root_dic_buf[a[0] + i[0]] = (Node(a[0] + i[0], a[1] + i[1], root_dic_buf[a[0]], Node(i[0], i[1])))
                elif a[0] not in root_dic_buf and i[0] in root_dic_buf:
                    root_dic_buf[a[0] + i[0]] = (Node(a[0] + i[0], a[1] + i[1], Node(a[0], i[1]), root_dic_buf[i[0]]))
                else:
                    root_dic_buf[a[0] + i[0]] = (Node(a[0] + i[0], a[1] + i[1], Node(a[0], a[1]), Node(i[0], i[1])))
            else:
                buf[i[0]] = i[1]
        data = buf

    dec_obj(root_dic_buf[a[0] + i[0]])
    print('Таблица кодировки: ', res_dic)
    print('Архивная строка: ', end='')

    for i in res_dic.values():
        print(f'{i} ', end='')

    return res_dic

data_str = Counter(input('Введите строку: '))
decoder(data_str)