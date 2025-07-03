import random
import string

pikkus = 16
märgid = string.ascii_letters + string.digits + string.punctuation
parool = ''.join(random.choice(märgid) for i in range(pikkus))
print("Genereeritud parool:", parool)
