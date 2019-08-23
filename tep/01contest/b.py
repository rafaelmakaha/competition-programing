def main():
	vogais = ["a", "e", "i", "o", "u", "y"]
	s = input()
	s = s.lower()

	for vogal in vogais:
		s = s.replace(vogal,'')
	novo = ''
	for letra in s:
		novo = novo + '.' + letra
	
	print(novo)
	
main()