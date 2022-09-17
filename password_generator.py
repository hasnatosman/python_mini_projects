import random
upper = "ABCDE"
lower = "xyz"
numbers = "0123456789"
symbols = " *&^%$#@(){}[]|\/><?':"
all = upper + lower + numbers + symbols
length = 10


password = "".join(random.sample(all, length))

print(password)
