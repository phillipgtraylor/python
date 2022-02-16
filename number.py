import random
while True :
    throw_1 = random.randint(1,6)
    throw_2 = random.randint(1,6)
    throw_3 = random.randint(1,6)
    total = throw_1 + throw_2 + throw_3
    print(total)
    if throw_1 == 6 and throw_2 == 6 and throw_3 == 6:
        break
print('six six six has been thrown')