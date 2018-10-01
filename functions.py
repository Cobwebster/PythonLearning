def beef():
    print("function ran")


def bitcoin_to_usd(btc):
    print("Value ", btc * 527)
    return btc


bitcoin_to_usd(100)

print(bitcoin_to_usd(1))


# default values for arguments

def get_gender(sex='unknown'):
    if sex is "m":
        sex = "male"
    elif sex is "f":
        sex = "female"
    print(sex)

get_gender()
get_gender("f")
get_gender("m")
