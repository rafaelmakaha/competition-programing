def main():
  n = int(input())

  if n <= 1000:
    return print(0)
  if n % 1000 == 0:
    return print(n//1000)
  ans = n//1000 + n % 1000
  return print(ans)
  
main()