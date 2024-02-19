
tableau = ["" for x in range(0,9)]
print(len(tableau))
joueurs = ["X", "O"]
x = 0

def affiche_tableau():
    print(f"{tableau[0]:2}|{tableau[1]:2}|{tableau[2]:2}")
    print(f"{tableau[3]:2}|{tableau[4]:2}|{tableau[5]:2}")
    print(f"{tableau[6]:2}|{tableau[7]:2}|{tableau[8]:2}")

fini = False
affiche_tableau()
while not fini:
    joueur = joueurs[x%2]
    print(f"joueur :{joueur}")
    x+=1
    if(x > 10):
        break

    commande_valide = False 
    commande = -1
    while (commande_valide != True):  
        try:
            commande = int(input("entrez la case à jouer: "))
            
        except ValueError:
            print("commande invalide, il faut un chiffre") 
        print(f"commande demandé = {commande}")
        if(int(commande) >9):
            print("pas possible hors tableau")
        elif(int(commande) <0):
            print("pas possible hors tableau")
        elif(tableau[int(commande)] =="X" or tableau[int(commande)] =="O" ):
            print("case deja pris")
            print(f"joueur {joueur} doit entrer une nouvelle case")
            
        else:
            tableau[int(commande)]=joueur
            commande_valide = True
    affiche_tableau()

    if(tableau[0]==tableau[1] and tableau[1] == tableau[2] and tableau[0] != "" and tableau[1] != "" and tableau[2] != ""):
        print(f"le joueur {joueur} a gagné")
        fini = True
    elif(tableau[3]==tableau[4] and tableau[4] == tableau[5] and tableau[3] != "" and tableau[4] != "" and tableau[5] != ""):
        print(f"le joueur {joueur} a gagné")
        fini = True
    elif(tableau[6]==tableau[7] and tableau[7] == tableau[8] and tableau[6] != "" and tableau[7] != "" and tableau[8] != ""):
        print(f"le joueur {joueur} a gagné")
        fini = True

    elif(tableau[0]==tableau[3] and tableau[3] == tableau[6] and tableau[0] != "" and tableau[3] != "" and tableau[6] != ""):
        print(f"le joueur {joueur} a gagné")
        fini = True
    elif(tableau[1]==tableau[4] and tableau[4] == tableau[7] and tableau[1] != "" and tableau[4] != "" and tableau[7] != ""):
        print(f"le joueur {joueur} a gagné")
        fini = True
    elif(tableau[2]==tableau[5] and tableau[5] == tableau[8] and tableau[2] != "" and tableau[5] != "" and tableau[8] != ""):
        print(f"le joueur {joueur} a gagné")
        fini = True
    
    elif(tableau[0]==tableau[4] and tableau[4] == tableau[8] and tableau[0] != "" and tableau[4] != "" and tableau[8] != ""):
        print(f"le joueur {joueur} a gagné")
        fini = True
    elif(tableau[2]==tableau[4] and tableau[4] == tableau[6] and tableau[2] != "" and tableau[4] != "" and tableau[6] != ""):
        print(f"le joueur {joueur} a gagné")       
        fini = True
    
    