print('BMI Calculator and Health Assessment \n')

weight = float(input('Please Enter Your Weight(kg): '))
height = float(input('Please Enter Your Height(m): '))

while weight <= 0 or height <= 0 : 
  print('\nYou can not enter negatif or zero values \n')
  weight = float(input('Please Enter Your Weight again: '))
  height = float(input('Please Enter Your Height again: '))

bmi =float(weight/(height*height))

if bmi < 18.5 :
  print(f'Your BMI is {bmi:.2f}. You are underweight')
elif bmi >= 18.5 and bmi <= 24.9 :
  print(f'Your BMI is {bmi:.2f}. You have a normal weight')
elif bmi >= 25 and bmi <= 29.9 :
  print(f'Your BMI is {bmi:.2f}. You are overweight.')
elif bmi >= 30 :
  print(f'Your BMI is {bmi:.2f}. You have obesity.')
else:
  print('Unspported.....')
