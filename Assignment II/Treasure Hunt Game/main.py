import random

print('Welcome to The Treasure Hunt Game \n')

n = int(input('Enter the number of rows for the game board: '))
m = int(input('Enter the number of columns for the board: '))

treasureRow = int(input(f'Choose a row to hide the treasure (1-{n}): '))
treasureColumn = int(input(f'Choose a column to hide the treasure (1-{m}): '))

while treasureRow > n or treasureColumn > m:
  if treasureRow > n:
    treasureRow = int(input(f'The row must be between (1-{n}): '))
  if treasureColumn >m:
    treasureColumn = int(input(f'The column must be between (1-{m}): '))

print('\nHere is your game board : \n')

trapRow = random.randint(1,n)
trapColumn = random.randint(1,m)

rowController=1
columnController=1

while rowController <= n:
  while columnController <= m:
    if treasureRow == rowController and treasureColumn==columnController:
      print(' T ',end="")
      columnController+=1
    elif  trapRow == rowController and trapColumn == columnController:
      if trapRow == treasureRow and trapColumn == treasureColumn:
        print(' T ',end="")
        trapRow = random.randint(1,n)
        trapColumn = random.randint(1,m)
        columnController+=1
      else:
        print('(X)',end="")
        columnController+=1
    else:
      print(' * ',end="")
      columnController= columnController+1
  rowController=rowController+1
  columnController=1
  print('\n')

print('Can You Guess The Treasure Location ?\n')

guessRow = int(input(f'What do you think the treasure Row is? (1-{n}):'))
guessColumn = int(input(f'What do you think the treasure Column is? (1-{m}):'))
    
while True :
  if guessRow == treasureRow and guessColumn==treasureColumn:
    print('You successfully found the Treasure :)')
    break
  elif guessRow == trapRow and guessColumn == trapColumn:
    print('You unfortunatly land on the Trap :(')
    break
  else:
    print('\nNot found try again\n')
    guessRow = int(input(f'What do you think the treasure Row is? (1-{n}):'))
    guessColumn = int(input(f'What do you think the treasure Column is? (1-{m}):'))
  