a=float(input('Enter a number:'))
b=float(input('Enter another number:'))
operator=input('Enter a operator(*,/,+,-):')
if operator=='+':
  print(f'Summation of {a} + {b} is = {a+b}')
elif operator=='-':
  print(f'Subtraction of {a} - {b} is = {a-b}')
elif operator=='*':
  print(f'Multiplication of {a} x {b} is = {a*b}')
elif operator=='/':
  if b==0:
    print('Error: Division by zero is not allowed')
  else: 
    print(f'Division of {a} and {b} is = {a/b}')
else:
  print('Error:Invalid operator')
        
  
