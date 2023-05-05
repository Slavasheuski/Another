import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
neod = 'il1Lo0O'
chars = ''
m = []

n = int(input('Укажите количество паролей для генерации: '))
lenght_password = int(input('Укажите длину одного пароля: '))
digit = input('Включать ли цифры 0123456789? ')
upp_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
low_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
punct = input('Включать ли символы !#$%&*+-=?@^_? ')
symbol = input('Исключать ли неоднозначные символы il1Lo0O? ')

if digit.lower() == 'да':
  chars += digits
if low_letters.lower() == 'да':
  chars += lowercase_letters
if upp_letters.lower() == 'да':
  chars += uppercase_letters
if punct.lower() == 'да':
  chars += punctuation
if symbol.lower() == 'да':
  for i in chars:
    if i not in neod:
      m.append(i)
if symbol.lower() != 'да':
  m.append(chars)
chars = ''.join(m)

def generate_password(num):
  l = []
  for i in range(num):
    l.append(''.join(random.sample(chars, lenght_password)))
  print('Варианты паролей: ', *l, sep='\n')
  
generate_password(n)
