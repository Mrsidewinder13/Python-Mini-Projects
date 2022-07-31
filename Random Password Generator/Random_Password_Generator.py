import random

passlen = int(input('Enter The Length Of Password: '))
S = 'abcdefghijklmopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
P = ''.join(random.sample(S,passlen ))
print(P) # Length limit is 73