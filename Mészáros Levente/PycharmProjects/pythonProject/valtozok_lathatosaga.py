import random

MIN = 1
MAX = 10

def main():
    kitalalando = random.randint(MIN, MAX)
    print(kitalalando)
    def tipp_bekero():
        print(f"Gondoltam egy számra {MIN} és {MAX} között! Próbáld meg kitalálni!")
        tipp = None
        talalat = 0
        while tipp != kitalalando:
            tipp = int(input('Tippelj!'))
            if tipp != kitalalando:
                talalat += 1
                print(f'Nem találtad el. Ez volt a {talalat}. próbálkozásod.')
            if tipp == kitalalando:
                talalat += 1

                print(f'Gratulálok eltaláltad {talalat} próbálkozásból!')

        def eltalalta(tipp, kitalalando):
            if tipp == kitalalando:
                return True
            else:
                return False

        print(eltalalta(tipp, kitalalando))
    tipp_bekero()

main()

