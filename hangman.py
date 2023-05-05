import random

word_list = ['человек', 'муравей', 'олово', 'медведь', 'психопад', 'желтуха', 'программа', 'солнышко', 'свитер', 'самурай', 'палочка', 'гарнитура',
             'звук', 'ноутбук', 'отвертка', 'шестигранник', 'бумага', 'линейка', 'фломастер', 'ножницы', 'дырокол', 'степлер', 'ластик', 'резинка',
             'голова', 'пачка']

def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # голова, торс, обе руки, одна нога
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # голова, торс, обе руки
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # голова, торс и одна рука
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # голова и торс
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # голова
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # начальное состояние
                    '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
        ]
    return stages[tries]

def play(word):
    while True:
        word_completion = '_' * len(word)
        word_completion1 = list(word_completion)
        guessed = False                    # сигнальная метка
        guessed_letters = []               # список уже названных букв
        guessed_words = []                 # список уже названных слов
        tries = 6
        counter = 0
        print('Давайте играть в угадайку слов!')
        print(display_hangman(tries))
        print(*word_completion1)

        while tries > 0:
            print('Введите букву или слово целиком: ')
            letter = input()
            counter = 0
            if letter.isalpha() != True:
                print('Введите, пожалуйста, букву!')
            if letter.isalpha() == True:        
                if len(letter) == 1:              
                    for i in range(len(word)):
                        if word[i] in letter.upper():
                            counter += 1
                            del word_completion1[i]
                            word_completion1.insert(i, letter.upper())
                    print(*word_completion1)                
                    if letter in guessed_letters:
                        print('Вы уже вводили эту букву, попробуйте другую!')            
                    if counter == 0 and letter not in guessed_letters:
                        tries -= 1
                        print(display_hangman(tries))
                        guessed_letters.append(letter)
                    if counter > 0:
                        guessed_letters.append(letter)
                    if word_completion1 == list(word):
                        print('Поздравляем, вы угадали слово! Вы победили!')
                        break                    
                if len(letter) == len(word):
                    if letter.upper() == word.upper():
                        print('Поздравляем, вы угадали слово! Вы победили!')
                        break
                    elif letter.upper() != word.upper():
                        if letter in guessed_words:
                            print('Вы уже называли это слово, попробуйте другое!')                    
                        if letter not in guessed_words:
                            print('Неверно, попробуйте ещё раз!')
                            tries -= 1
                            print(display_hangman(tries))
                            guessed_words.append(letter)
                if 1 < len(letter) < len(word):
                    print('Введите только одну букву либо слово целиком!')
                    continue

        if tries == 0:
            print('Вы проиграли... Загаданное слово: ', word)
        print('Хотите сыграть ещё раз? (да или нет)')

        ask = input()
        if ask.lower() != 'да':
            print('До новых встреч!')
            break
        
word = get_word()
play(word)
