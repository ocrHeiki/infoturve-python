# Küsi kasutajalt parooli
parool = input("Sisesta oma parool: ")

# Kontrollime parooli pikkust
if len(parool) >= 12:
    print("Hea parool!")
else:
    print("Parool võiks olla vähemalt 12 tähemärki.")
