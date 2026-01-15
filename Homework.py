#dictionnaire donnant la force d'une lettre
POWER_LETTER={
    'a':1, 'à':1, 'â':1, 'ä':1, 'á':1, 'ã':1, 'å':1,
    'b':2,
    'c':3, 'ç':3,
    'd':4,
    'e':5, 'é':5, 'è':5, 'ê':5, 'ë':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9, 'í':9, 'ì':9, 'î':9, 'ï':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14, 'ñ':14,
    'o':15, 'ó':15, 'ò':15, 'ô':15, 'ö':15, 'õ':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21, 'ú':21, 'ù':21, 'û':21, 'ü':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25, 'ý':25, 'ÿ':25,
    'z':26
}

#cette fonction nous permet de calculer la force d'un mot entre sa i-eme et sa j-eme lettre
def force_du_mot(mot,i,j):
    #on mets tout en minuscule pour ne pas avoir des probleme avec le dictionnaire
    mot = mot.lower()
    
    #calcule de la force
    #definition de la variable qui va stoquer la force 
    force=0
    #on va parcourir notre mot de la i-eme lettre a la j-eme lettre
    #on verifie d'abord si notre mot a plus de j lettres
    if(len(mot)>=j): 
        #ok on peut parcourir le mot entre i et j , attention la i-eme lettre est a l'indice i-1 et de meme pour la j-ieme
        for position in range(i-1,j):
            #on recupere la lettre qui est a l'indice <<position>>
            letter=mot[position]
            #on ajoute sa force a notre variable force
            #mais d'abord on verifie si la lettre est dans le dictionnaire car ca peut etre un trait d'union ou un espace , on ne sait pas 
            if letter in POWER_LETTER:
                #ok c'est une lettre on peut avancer
                force+=POWER_LETTER[letter]
            #si c'est pas une lettre on ne fera donc rien
    else:
        #cas ou le mot a moins de j lettres,donc on va parcourir le mot de la i-eme lettre jusqu'a la fin
        for position in range(i-1,len(mot)):
            #la logique reste la meme que plus haut 
            letter=mot[position]
            if letter in POWER_LETTER:
                force+=POWER_LETTER[letter]
                
    #a ce stade on a deja la force du mot entre i et j on peut renvoyer sa valeur
    return force

#cette fonction nous permet de determiner le mot le plus court
def min_mot(liste_de_mots):
    #on affecte le mot le plus court au premier indice du tableau
    min_word=liste_de_mots[0]
    #on parcourt le tableau pour rechercher le min
    for mot in liste_de_mots:
        #si un mot est a une taille plus petite que min_word il devient min_word
        if( len(mot) < len(min_word) ):
            min_word=mot
    
    #on renvoie le mot de taille minimum
    return min_word

#cette fonction nous permet de determiner le mot le plus long
def max_mot(liste_de_mots):
    #on affecte le mot le plus court au premier indice du tableau
    max_word=liste_de_mots[0]
    #on parcourt le tableau pour rechercher le min
    for mot in liste_de_mots:
        #si un mot est a une taille plus grande que max_word il devient max_word
        if( len(mot) > len(max_word) ):
            max_word=mot
    
    #on renvoie le mot de taille minimum
    return max_word

#cette fonction va nous permettre de verifier si un utilisateur a bien entre une lettre
def verify_number(number):
    #on parcour les caracteres un par un et on regarde si ceux sont bien des chiffres
    for x in number:
        if( x not in "0123456789"):
            #le  caractere x n'est pas un chiffre
            return False
    #si on arrive ici c'est que tout c'est bien passe
    return True
    
#code principal

#liste de termes geologiques
mot_geol = ["granite", "basalte", "schiste", "calcaire", "grès", "argile", 
            "métamorphisme", "érosion fluviale", "dérive des continents", 
            "subduction", "rift continental", "pluton", "cratère volcanique", 
            "lave basaltique", "cycle sédimentaire", "faille normale", 
            "plaine alluviale", "roche magmatique", "strates géologiques", 
            "moraine glaciaire"]

#debut du programme
print("BIENVENUE A LA WWE DES MOTS  #QUI EST LE PLUS FORT\n")
print("Le mot le plus court de la liste est : "+min_mot(mot_geol)+"\n")
print("Le mot le plus long de la liste est : "+max_mot(mot_geol)+"\n\n")
print("A vous de fixer les regles du combat, veuillez entrer\n")


start=input("Entrez la position de lettre a partir de laquelle on parcourt les mots : ")
#on verifie si l'utilisateur a entre des bonne valeurs
#du moment que notre fonction de verification nous envoie faux on redemande la valeur
while not verify_number(start):
    start=input("Veuillez entrer un nombre : ")
    
end=input("Entrez la position de la lettre à laquelle on arrête de parcourir les mots : ")
#on verifie si l'utilisateur a entre des bonne valeurs
#du moment que notre fonction de verification nous envoie faux on redemande la valeur
while not verify_number(end):
    end=input("Veuillez entrer un nombre : ")
    
#on convertir les chaines en entier
start=int(start)
end=int(end)


print("\n-------La partie commence----------\n")

#on va parcourit notre liste pour derminer le mot le plus fort
#declaratioin de la variable
mot_le_plus_fort=mot_geol[0]
#on parcourt les mots de la liste
#avant ca on enleve le premier terme pour ne pas le comparer a lui meme
del mot_geol[0]
#maintenant on peut parcourir la liste
for mot in mot_geol:
    #si le mot est plus fort que le mot_le_plus_fort , on mets a jour le nouveau mot le plus fort
    if ( force_du_mot(mot,start,end) > force_du_mot(mot_le_plus_fort,start,end) ):
        print(" "+mot+" est plus fort que le mot "+mot_le_plus_fort+"\n")
        mot_le_plus_fort=mot
    else:
        #dans ce cas ci le mot_le_plus_fort est plus fort ou egale a mot 
        print(" "+mot_le_plus_fort+" est plus fort que le mot "+mot+"\n")
        
        
#resultat final
print(" Le mot le plus fort de la liste est : "+ mot_le_plus_fort +" \n")

input("Appuyez sur Entrée pour quitter l'arene de combat...")
