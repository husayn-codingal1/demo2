def decimal_to_binary(n):
  if n > 1:
    decimal_to_binary(n // 2)
  print(n % 2, end='')

number = int(input("Enter a decimal number: "))

decimal_to_binary(number)
