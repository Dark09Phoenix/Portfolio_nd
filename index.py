# ==============================
# APPLICATION DE GESTION DES EMPRUNTS
# ==============================

# ---- Identifiants administrateur (préenregistrés) ----
User=[("Py_user", 123), ("Al_user",563)]


# ---- Variables statistiques ----
total_emprunts = 0
recette_totale = 0
nb_etudiants = 0
nb_adultes = 0
nb_seniors = 0

PRIX_JOUR = 3.5


# ==============================
# AUTHENTIFICATION
# ==============================
def authentification():
    tentatives = 3

    while tentatives > 0:
        identifiant = input("Identifiant : ")
        mot_de_passe = input("Mot de passe : ")

        if identifiant == User.index and mot_de_passe == MOT_DE_PASSE:
            print("Connexion réussie.\n")
            return True
        else:
            tentatives -= 1
            print(f"Erreur ! Tentatives restantes : {tentatives}")

    print("3 échecs. L'application se ferme.")
    return False


# ==============================
# ENREGISTREMENT EMPRUNT
# ==============================
def enregistrer_emprunt():
    global total_emprunts, recette_totale
    global nb_etudiants, nb_adultes, nb_seniors

    nom = input("Nom de l'emprunteur : ")

    # ---- Contrôle du nombre de jours ----
    tentatives_jours = 5
    while tentatives_jours > 0:
        try:
            jours = int(input("Nombre de jours d'emprunt (1-30) : "))
            if 1 <= jours <= 30:
                break
            else:
                tentatives_jours -= 1
                print(f"Nombre invalide. Tentatives restantes : {tentatives_jours}")
        except:
            tentatives_jours -= 1
            print(f"Entrée invalide. Tentatives restantes : {tentatives_jours}")

    if tentatives_jours == 0:
        print("Retour au menu principal.\n")
        return

    # ---- Catégorie ----
    print("Catégorie :")
    print("1 - Étudiant")
    print("2 - Adulte")
    print("3 - Senior")

    categorie = input("Choix : ")

    reduction = 0
    categorie_nom = ""

    if categorie == "1":
        reduction = 0.5
        categorie_nom = "Étudiant"
        nb_etudiants += 1
    elif categorie == "2":
        reduction = 0
        categorie_nom = "Adulte"
        nb_adultes += 1
    elif categorie == "3":
        reduction = 0.3
        categorie_nom = "Senior"
        nb_seniors += 1
    else:
        print("Catégorie invalide. Retour menu.\n")
        return

    # ---- Calcul du prix ----
    prix_sans_reduction = jours * PRIX_JOUR

    # Majoration si plus de 14 jours (uniquement jours au-delà de 14)
    majoration = 0
    if jours > 14:
        jours_majores = jours - 14
        majoration = jours_majores * PRIX_JOUR * 0.2

    prix_apres_reduction = prix_sans_reduction * (1 - reduction)
    prix_final = prix_apres_reduction + majoration

    # ---- Mise à jour statistiques ----
    total_emprunts += 1
    recette_totale += prix_final

    # ---- Affichage reçu ----
    print("\n===== REÇU =====")
    print("Nom :", nom)
    print("Nombre de jours :", jours)
    print("Catégorie :", categorie_nom)
    print("Prix sans réduction :", round(prix_sans_reduction, 2), "€")
    print("Prix final :", round(prix_final, 2), "€")
    print("================\n")


# ==============================
# STATISTIQUES
# ==============================
def afficher_statistiques():
    print("\n===== STATISTIQUES =====")
    print("Nombre total d'emprunts :", total_emprunts)
    print("Recette totale :", round(recette_totale, 2), "€")
    print("Nombre d'étudiants :", nb_etudiants)
    print("Nombre d'adultes :", nb_adultes)
    print("Nombre de seniors :", nb_seniors)
    print("========================\n")


# ==============================
# MENU PRINCIPAL
# ==============================
def menu():
    while True:
        print("1 - Enregistrer un nouvel emprunt")
        print("2 - Afficher les statistiques")
        print("3 - Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            enregistrer_emprunt()
        elif choix == "2":
            afficher_statistiques()
        elif choix == "3":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.\n")


# ==============================
# PROGRAMME PRINCIPAL
# ==============================
if authentification():
    menu()