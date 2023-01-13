#list of vowels
vowel = [
  "a",
  "e",
  "i",
  "o",
  "u",
]

letter = input("Enter a letter: ")

#errors

if len(letter)!= 1:
  print("You must enter a single letter")
  exit()

#lower cases the letter
letter = letter.str.lower()

#vowel check
if letter in vowel:
  print(f'{letter} is a vowel')
elif letter == 'y':
  print(f'{letter} is sometimes a vowel')
else:
  print(f'{letter} is a consonant')


