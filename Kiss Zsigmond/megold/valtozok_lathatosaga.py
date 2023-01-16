import random
def tipp_bekero():
    print("Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!")
    tipp = int(input("Tippelj! "))
    return tipp
def eltalalta(tipp, kitalalando):
    if tipp == kitalalando:
        return True
    else:
        return False

def main():
    kitalalando = random.randint(1,10)
    print(kitalalando)
    tipp = tipp_bekero()

    talalat = False

    while not talalat:
        db = 0

        if eltalalta(tipp, kitalalando):
            talalat = True
            print("Gratulálok eltaláltad {} próbálkozásból!", db + 1)
        else:
            db = db + 1
            talalat = False

    print("Vége!")
main()