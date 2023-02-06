kutya = {}

kutya["név"] = input("Kérlek, add meg a kutya nevét: ")
kutya["életkor"] = int(input("Kérlek, add meg a kutya életkorát: "))
kutya["fajta"] = input("Kérlek, add meg a kutya fajtáját: ")
oltas = input("Rendelkezik érvényes oltással veszettség ellen? (igen/nem): ")
if oltas == "igen":
  kutya["oltás"] = True
else:
  kutya["oltás"] = False

print("A kutya adatai:")
print(kutya)