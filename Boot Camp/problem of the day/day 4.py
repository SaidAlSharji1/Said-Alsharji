def check_gender(username):
    if username.endswith('s'):
        return "The user is Girl"
    else:
        return "The user is Boy"

us1=check_gender("chidy")
us2=check_gender("blacks")
print(us1)
print(us2)