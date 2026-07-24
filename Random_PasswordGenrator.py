import random
import string
char=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(12):
    password=password+random.choice(char)
print("your random genrated password is-",password)