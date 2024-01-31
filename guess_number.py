from random import randint

random = randint(1,100)
print('Угадайте число от 1 до 100')

while True:
      guess = int(input('Введите число: '))

      if guess < random:
            print('Ваше число меньше загаданного')

      elif guess > random:
            print('Ваше число больше загаданного')

      else:
            break
      
print('Вы угадали число')
