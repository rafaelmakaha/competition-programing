import math

def main():
  x = input()
  if x.find('.') > 0:
    return print(x.split('.')[0])
  return print(x)

main()