parool = input("Sisesta parool: ")

if len(parool) < 12:
    print("Parool on liiga lühike.")
elif parool.islower() or parool.isupper():
    print("Parool peaks sisaldama nii suuri kui väikseid tähti.")
elif parool.isalpha():
    print("Parool peaks sisaldama ka numbreid või sümboleid.")
else:
    print("Parool tundub tugev.")
