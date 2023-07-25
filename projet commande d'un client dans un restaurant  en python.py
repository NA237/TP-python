
#image du programme
print("\t\t\t\t\t\t\t\t ~~~~~~~~~~~~~~~~~~~~")
print("\t\t\t\t\t\t\t\t|tasty food of nagato|")
print("\t\t\t\t\t\t\t\t| ------------------ |")
print("\t\t\t\t\t\t\t\t|     version 2.0    |")
print("\t\t\t\t\t\t\t\t|____________________|")
print("\n\t\t\t\t\t\t\t BONJOUR, BIENVENUE  AU RESTAURANT DE NAGATO.")
#identification des  clients
print("svp, Qeul est votre nom??\n ")
nom = input("veuiller entrer votre nom: ")
serveur = "bienvenue au  Restaurant  nagato."
print("\n\t\t\tbonjour, Mr", nom, serveur)
# presentation du menu
print("\n\tSvp veuillez choisir votre plat parmir le Menu suivant: ")
print("\n comme Menu nous avons:\n")
#declation des prix des menu,complement,et jus
prix_menu=0
#liste des denu du restaurant
menu_du_restaurant = ["le pain", "(450 FCFA),\t","le riz","(500 FCFA),\t"]       
#affiche la liste des menu au client
print("\t", menu_du_restaurant[0], menu_du_restaurant[1], menu_du_restaurant[2], menu_du_restaurant[3])
#le client entre dans la machine sa commande 
choix_du_menu = input(" \n\t\tveuillez entrer votre choix: \n\n ",)

if choix_du_menu in menu_du_restaurant:
    #declaration des prix des menus du restaurant (M1:represente le 1er menu)
    M1="le pain"
    M2="le riz"
    while choix_du_menu==M1:
        prix_menu=450
        print("\n\t\t\t\t\t\tle prix du menu est de:",prix_menu,"FCFA")
        break
    while choix_du_menu==M2:
        prix_menu=500
        print("\n\t\t\t\t\t\tle prix du menu est de:",prix_menu,"FCFA")
        break
    
  


# ici c'est quand l'utilisateur faire un choix qui n'est pas dans le menu  du restaurant (c'est a dire le pain)
if choix_du_menu not in menu_du_restaurant:
    print(choix_du_menu, "\n\n Ce choix ne fait pas partir des plats de la maison, Veuillez ressayer  ")
    exit()
elif choix_du_menu in menu_du_restaurant:
    # deuxiemme choix pour charger son pain
    reponses = {}
    terminer = True
    complement = ["le chocolat",'(25 FCFA),\t'  "le beurre","(25 FCFA),\t"  "la sardine","(300 FCFA)\t" "la mayonnaise","(50 FCFA),\t"   "le piment","(25 FCFA),\t\n\n\n"   "l'oeuf","(100 FCFA),\t" "l'avocat","(500 FCFA),\t" "la sauce tomate","(300 FCFA),\t" "la sauce blanche","(250 FCFA),"]
    while terminer:
        print("\n\t\t\tveuillez choisir  un complément ou un chargement de votre choix \n\n")
        print(complement[0],complement[1],complement[2],complement[3],complement[4],complement[5],complement[6],complement[7],complement[8],complement[9])
        #le choix1 c est le choix pour le complement 
        choix1 = input("\n je veux choisir: ")
        print("\n")

        repeter = input("voulez-vous tourjours choisir un complement (oui/non) ")
        terminer = True if repeter == "oui" else False
    



#ici la je liste les jus que dispose la maison
listejus= ["pamplemouse","(650 FCFA),\t"   "orange","(1000 FCFA),\t"   "ananas","(550 FCFA),\t"    "mange","(1850 FCFA),\t"   "pomme","(800 FCFA),\t"]
print("\n voici la liste des jus que dispose le maison \n")
print(listejus[0],listejus[1],listejus[2],listejus[3],listejus[4],listejus[5])

mon_jus= input("\n svp veuillez entrer le nom de votre jus préférer: ")


#ici c'est le choix du jus  du client
if mon_jus not in listejus: 
    reponses_du_jus ={}
    livraison=True

    while livraison:

        choix3= mon_jus
        print("\n")

        repeter_jus=input("\n voulez-vous tourjours choisir un jus sur notre liste (oui/non) ")
        livraison =True if repeter_jus == "oui" else False


# ici la j'affiche la commande du client pour son chargemment avec le pain
if choix1 == complement:
    print(choix1, "\n Ce choix ne fait pas partir du complement de la maison, Veuillez ressayer  ")
else:
    # ici la je vais liste tout ce que le client a choisir
    print("\n vous venez de commander", choix_du_menu, "avec", choix1,"avec une top", choix3)

''
# ici la j'affiche la commande du client pour son chargemment avec plusieur element  le pain avec l'oeuf et le pimment
if choix1 == complement and choix1<=7:
    n=0
    for n in choix1:
        print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t vous venez de commander", choix_du_menu, "avec", choix1,n, "avec une top", choix3,)

print("\n\n\t\t\t\t\t\t\t Merci",nom ," D'etre tourjour fidèle au restaurant de nagato ")


#voici la fin du programme du restaurant de nagato

print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t NB: ce programme  à été coder par nagato le 25/07/2023")

print("\n\n\t\t\t\t\t\t\t\t\t FIN DU PROGRAMME...")n

exit() 





