import hashlib

failinimi = input("Sisesta failinimi: ")
with open(failinimi, "rb") as f:
    sisu = f.read()
    sha256 = hashlib.sha256(sisu).hexdigest()
    print("Faili SHA256:", sha256)
