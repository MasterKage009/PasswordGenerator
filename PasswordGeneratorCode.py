import random, string, secrets

Digits = random.randint(10, 99)

#print(Digits)

#generates random number


letter1 = secrets.choice(string.ascii_lowercase)
letter3 = secrets.choice(string.ascii_lowercase)
letter2 = secrets.choice(string.ascii_uppercase)
letter4 = secrets.choice(string.ascii_uppercase)

#print(letter1 + letter2 + letter3 + letter4)

#generates random combo of uppercase/lowercase letters


special_characters = string.punctuation[2]
#print ( ''.join(random.choice(special_characters) for i in range(3)) )

#generates special characters

print(letter1 + letter2 + letter3 + letter4 + str(Digits) + str(special_characters))

#print random password





