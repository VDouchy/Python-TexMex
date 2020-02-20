#General

menu = {
    "Tapas" : "(Tomatoes, Olive, Ham)",
    "Fajitas" : "(Tortilla, Chicken, Onion, Pepper)",
}






#Code execute
print("Bienvenue chez PYTHON TexMex, voici notre menu ! :")
print("Nous vous proposons", menu)
choix = input("Dites-nous quel plat vous avez choisi ! ")

if choix not in menu:
    print("Nous n'avons pas ce plat ! Choissisez dans le menu")
else:
    print("vous avez choisi", choix,"Votre commande arrive !")
