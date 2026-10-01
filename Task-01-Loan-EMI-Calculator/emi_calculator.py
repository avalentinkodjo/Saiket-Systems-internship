def print_hi ():
    print(f'*** Bienvenue dans la calculatrice de paiement mensuel ***')

def func_emi(mtn_pret:float, taux_interet:float, duree_pret:int) -> float:
    #Conversion du taux annuel en taux mensuel
    r = taux_interet / (100*12)

    #Condition lorsque le taux mensuel est nul
    if r == 0:
        emi = mtn_pret / duree_pret
        return emi
    else:
        numerateur = mtn_pret * r * (1 + r) ** duree_pret
        denominateur = (1 + r) ** duree_pret - 1
        emi = numerateur / denominateur

        return emi

if __name__ == '__main__':
    print_hi()

    #Controle des valeurs de chaque variable et récupération
    unPret = float(input('\t -> Veuillez entrer le montant principale du prêt : '))
    while unPret <= 0 :
        unPret = float(input("\t -> Veuillez entrer un montant strictement supérieur à zéro : "))

    unTaux_interet = float(input("\t -> Veuillez entrer le taux d'intérêt du prêt en pourcentage : "))
    while unTaux_interet < 0:
        unTaux_interet = float(input("\t -> Veillez zntre un taux du prêt en pourcentage : "))

    uneDuree_pret = int(input("\t -> Entrez la durée du prêt en mois : "))
    while uneDuree_pret <= 0 :
        uneDuree_pret = int(input("\t -> Veilez entrer une durée de prêt strictement supérieure à zéro"))

    #Capital à payer par moi
    cap_emi = func_emi(unPret, unTaux_interet, uneDuree_pret)

    print("\n *** LES RESULTATS DE VOTRE PRET ***")
    print(f"\t -> Vous avez zu à faire un prêt de : {unPret:.2f}")
    print(f"\t -> Le taux de ce prêt est : {unTaux_interet:.2f}")
    print(f"\t -> La duree du prêt est : {uneDuree_pret} mois")
    print(f"\t -> Voici le montant à payer par mois : {cap_emi:.2f}")