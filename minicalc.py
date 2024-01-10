# MiniCalc by swmwy

minicalc = True

while minicalc = True:

  operation = input("Choose an operation: a for addition, s for subtraction, m for multiplication, and d for division.\n")

  if operation == 'd':
    operation = 'division'

  elif operation == 'a':
    operation = 'division'

  elif operation == 's':
    operation = 'subtraction'

  elif operation == 'm':
    operation = 'multiplication'

  else:
    print("Error: could not detect operation. (Hint: Make sure the letter is lowercase.)")

  num1 = input("Enter the first number:")

  num2 = input("Enter the second number:")

  int(num1)
  int(num2)

  if operation == 'division':
    if num1 == 0:
      print("Divide by 0 error.")
    elif num2 == 0:
      print("Divide by 0 error.")
    else:
      solution = num1 / num2

  if operation == 'subtraction':
    solution = num1 - num2

  if operation == 'addition':
    solution = num1 + num2

  if operation == 'multiplication':
    solution = num1 * num2

  print(solution)
