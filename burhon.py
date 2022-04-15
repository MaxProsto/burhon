from random import randint
from time import sleep
from tkinter import *


root = Tk()
root.geometry('250x350')
root.title('Поле чудес')

latter: str = ""
def input_enter():
  global latter
  latter = nema.get()
  

question = Label(root, text = "Падают капли, но это не дождь", fg = 'orange') #вопрос
question.pack()
word_root = Label(root, text = '--', fg = 'red') #слово
word_root.pack()
price_root = Label(root, text = '--', fg = 'black') #барабан
price_root.pack()
price_root2 = Label(root, text = '--', fg = 'black') #действие
price_root2.pack()
nema = StringVar()
enter = Entry(textvariable = nema) #ввод
enter.pack()
entry = Button(root, text = 'enter', command=input_enter)
entry.pack()

# sleep(3)
# word_root.pack_forget()
# sleep(3)
# word_root.pack()
data = {}
word_copy = []
word = list( "водопад" )
prices = [ "автомобиль", "ничего", "100000", "кефир", "дом", "жена", "смерть", "лук", ]
circle = [ 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, "2x", "3x", "+", "?", -1 ]
 
for i in word:
    word_copy.append( "_" )

for i in range( 3 ):
    # price_root2.config(text = "Введите имя " + str( i + 1 ) + " игрока: ")
    data[ input( "Введите имя " + str( i + 1 ) + " игрока: " ).capitalize() ] = 0

def write( number: int, text: str):
  if number == 1:
    price_root.config( text = text )
  elif number == 2:
    price_root2.config( text = text )
 
print( str( len( word ) ) + " букв" )

i = 0
count = 0
while True:
  name = list( data.keys() )[i]

  choice = str(input(name + ", хотите назвать слово: "))

  if choice == "да":
    l2 = input("Введите слово: ")
    if list(l2) == word:
      print("Поздравляю, вы угадали слово")
      data[name] += 1000
      print(data)

    else: 
      print("Вы не угадали")
      del data[name]
      if i < 2: i += 1
      else: i = 0

  word_root.config( text = word_copy )
  price = circle[ randint(0, len(circle)-4)]

  # if price == "?":#черный ящик
  #   price = prices[ randint( 0, len( prices ) - 1 ) ]
  #   price_root.config( text = "Чёрный ящик" )
  #   if price == "смерть": del data[ list( data.keys() )[i] ]
  #   else:
  #     k = 0
  #     print( "Вау, у тебя есть черный ящик" )
  #     letter = ""
  #     while k < 6:
  #       k += 1
  #       if letter == "да": break
  #       print( "Я предлагаю " + str( randint( 1000, 1000000 ) ) )
  #       letter = input( "Вы согласны взять наличные? ? " )

  #     print( "так что ты решил взять подарок " + price )
  # elif price == "+":
  #   price_root.config( text = "Вы можете открыть одну букву")
  #   k = int( input("Введите индекс буквы: "))
  #   m = k + 1
  #   word_copy[k] = word[k]
  #   word[k] = "_"
  # elif price == -1: 
  #   price_root.config( text = "Вы пропускаете ход")
  #   i +=1
  if price == 1: pass
  else:
    price_root.config( text = str(price) + " очков" )
    
    # letter = input( name + " введите букву: " )
    write( 2, name + " введите букву: ")
    sleep(10)
    letter = latter

    countl = word.count( letter )
    if letter == "0": break
    if word.count("_") < (len( word ) - 1):
      if countl > 0:
          points = 1
          if price == "2x": points = 2
          elif price == "3x": points = 3
          print( "Поздравляю, вы угадали букву !!!!" )
          for k in word:
              if k == letter:
                  count += 1
                  wi = word.index( letter )
                  data[name] = points * 100 * (1 + wi) + data[name]
                  word_copy[ wi ] = letter
                  word[wi] = "_"
                  if not price == "2x":
                    if not price == "3x":
                      data[name] += price
          print("У вас " +  str(data[name]) + " баллов")
          if count > 2:
            print( "теперь ты можешь получить сюрприз с двумя коробками, и тебе нужно выбрать одну из них " )
            letter = randint( 1, 3 )
            choice = int( input( "Выбери шкатулку: " ) )
            if choice == letter: 
              print( "Вау, ты выиграл 500 баллов" )
              data[name] += 500
            else: print("Эта шкатулка пуста")
      else:
        if i < 2: i += 1
        else: i = 0
        print( "вы не угадали букву" )
        print( "следующий ход игрока " + list(data.keys())[i])

    else: 
      print( word_copy )
      print("Победил " + str(i + 1) + " игрок")
      print( data )
      break
