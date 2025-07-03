email = input("Sisesta e-posti aadress: ")

if "@gmail.com" in email or "@yahoo.com" in email or "@outlook.com" in email:
    print("Tundub olevat tavakasutaja e-post.")
else:
    print("Võib olla ettevõtte või kohandatud domeen.")
