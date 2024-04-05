# MiniCalc by swmwy

from time import sleep

minicalc = True

while minicalc is True:

  error = True

  while error is True:
  
    operation = input("Choose an operation: a for addition, s for subtraction, etc.\n")

    if operation == 'd':
      operation = 'division'
      error = False
    elif operation == 'a':
      operation = 'addition'
      error = False
    elif operation == 's':
      operation = 'subtraction'
      error = False
    elif operation == 'm':
      operation = 'multiplication'
      error = False
    else:
      print("Error: could not detect operation.")
      error = True
      sleep(1)
  num1 = input("Enter the first number:")

  sleep(1)
  
  num2 = input("Enter the second number:")

  sleep(1)
  
  if operation == 'division':
    if num1 == 0 or num2 == 0:
      print("Divide by 0 error.")
      sleep(1)
    else:
      solution = int(num1) / int(num2)

  elif operation == 'subtraction':
    solution = int(num1) - int(num2)

  elif operation == 'addition':
    solution = int(num1) + int(num2)

  elif operation == 'multiplication':
    solution = int(num1) * int(num2)

  sleep(1)
  print(solution)
  sleep(1)
