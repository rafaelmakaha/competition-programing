def main():
  M, H = input().split()

  if int(H) % int(M) == 0:
    return print("Yes")
  print("No")

main()