data = {
    "1": {"name": "Alex", "last_name": "Loo", "email": "alexlo0@gmail.com", "telephote": "+111222"},
    "2": {"name": "Flex", "last_name": "Tex", "email": "", "telephote": "+444444"},
    "3": {"name": "Hex", "last_name": "Fex", "email": "hex228@gmail.com", "telephote": "+555555"},
    "4": {"name": "Meks", "last_name": "Geks", "email": None, "telephote": "+343454652"}
}

print(data.items())
def email(data):
    flist = []
    for id, user_info in data.items():
        if user_info["email"] is None or user_info["email"] == "":
            flist += [user_info["name"] + " is empty"]
    return flist


print(email(data))
