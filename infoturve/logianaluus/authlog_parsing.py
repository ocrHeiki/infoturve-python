with open("fake_auth.log") as fail:
    for rida in fail:
        if "Failed password" in rida:
            print(rida.strip())
