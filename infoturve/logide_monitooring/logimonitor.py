with open("server.log", "r") as logifail:
    read = logifail.readlines()
    for rida in read[-50:]:
        if "error" in rida.lower():
            print(rida.strip())
