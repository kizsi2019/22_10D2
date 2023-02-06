dog = {}
dog_name = input("Kérlek, adja meg a kutya nevét: ")
dog_age = input("Kérlek, adja meg a kutya életkorát: ")
dog_breed = input("Kérlek, adja meg a kutya fajtáját: ")
dog_vaccination = input("Rendelkezik-e érvényes oltással veszettség ellen (igen/nem): ")

dog["név"] = dog_name
dog["életkor"] = dog_age
dog["fajta"] = dog_breed
dog["oltás"] = dog_vaccination

print("A kutya adatai:")
for key, value in dog.items():
    print(f"{key}: {value}")