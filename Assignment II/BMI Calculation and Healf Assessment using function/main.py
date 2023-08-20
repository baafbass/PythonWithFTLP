print('BMI Calculator and Health Assessment \n')

def calculate_bmi(weight_in_Pounds,height_in_Inches):  
  weight = weight_in_Pounds/2.20462
  height = height_in_Inches/39.3701
  bmi = float(weight/(height*height))
  return round(bmi,2)
  
weightPound = float(input('Please Enter Your Weight(Pound): '))
heightInch = float(input('Please Enter Your Height(inch): '))

while weightPound <= 0 or heightInch <= 0 : 
  print('\nYou can not enter negatif or zero values \n')
  weightPound = float(input('Please Enter Your Weight again: '))
  heightInch = float(input('Please Enter Your Height again: '))

bmi = calculate_bmi(weightPound,heightInch)

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