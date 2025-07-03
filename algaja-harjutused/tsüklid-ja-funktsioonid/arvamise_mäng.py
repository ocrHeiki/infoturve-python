import random

# Arvuti valib juhusliku numbri 1 kuni 10
õige = random.randint(1, 10)

# Kasutaja proovib ära arvata
while True:
    pakkumine = int(input("Arva number (1-10): "))
    if pakkumine == õige:
        print("Õige! Tubli!")
        break
    else:
        print("Vale, proovi uuesti.")
