import os

kaust = input("Sisesta kausta tee: ")

for juur, kaustad, failid in os.walk(kaust):
    for fail in failid:
        if fail.endswith(".log"):
            print("Leitud logifail:", os.path.join(juur, fail))
