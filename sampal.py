pp = input().upper()
dr = input().upper()

def winner(ppmove, drmove):
    ppdr = {
        "ROCK": {"SCISSORS", "SLAP"},
        "PAPER": {"ROCK", "SLAP"},
        "SCISSORS": {"PAPER", "SLAP"},
        "GUN": {"SCISSORS", "ROCK", "PAPER"},
        "SLAP": {"GUN"},
    }

    if pp == dr:
        return "TIE"

    if ppmove in ppdr and drmove in ppdr[ppmove]:
        return "PLATYPUS"
    elif drmove in ppdr and ppmove in ppdr[drmove]:
        return "OOF"

result = winner(pp, dr)
print(result)
