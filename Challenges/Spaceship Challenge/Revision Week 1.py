crew = ["Arthur", "Zaphod", "Ford", "Marvin"]
crew_pwd = ["Towel", "Beeblebrox", "SoLong", "AllSpareParts"]
flag_continue = False
name = input("Please enter your first name: ")
for i in range (0, len(crew)):
    if crew[i] == name:
        pwd = input("Please enter your password: ")
        if crew_pwd[i] == pwd:
            flag_continue = True