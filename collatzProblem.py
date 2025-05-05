def Collatz(number):
  if number == 1:
    return
  elif number % 2 == 0:
    number = number // 2
    print(number, end=' ')
    return Collatz(number)
  else:
    number = 3 * number + 1
  print(number, end=' ')
  return Collatz(number)

while True:
  try:
    number = int(input('Enter a number: '))
    if number <= 0:
      print('Invalid input. Try again.')
      continue
  except ValueError:
    print('Invalid input. Try again.')
    continue
  else:
    break
print(f'Input: {number}')
print('Sequence: ', end='')
Collatz(number)
