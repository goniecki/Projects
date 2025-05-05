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


number = int(input('Enter a number: '))
print(f'Input: ', number)
print('Sequence: ', end='')
Collatz(number)
