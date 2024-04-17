def fonction_logique(a,b,c):
     return  (a and b) or (not b and c) or (a and not c)

print ("f(a,b,c) = (a and b) or (not b and c) or (a and not c)")

print("\nTable de vérité de f(a,b,c)")

# création d'une table de vérité
#  les en-têtes de tableau
def table_v () :
    variable = ("1","0")
    print("a\tb\tc\tf(a,b,c)")
    print ("----------------------------")
 # les combinaison des variables
    for a in variable:
        for b in variable:
             for c in variable:
                resultat =fonction_logique(int (a),int(b), int(c)) 
                print(f"{a} | {b} | {c} | {int (resultat)}")
table_v()  
  # fin du tableau

# maintenat,on va voir les forme canonique
print("forme canonique de la fonction f: ")
 
print("\nposons f1 : première forme canonique de la fonction")
def permiere_forme_canonique () :
   premiere_canonique= "f1=(a and not b and c) or (not b and not c)"
   return premiere_canonique
print("\n Alors on a " , permiere_forme_canonique() )

print("\nposons f2 : second forme canonique de la fonction")
def second_forme_canonique () :
    second_canonique = "f2 = (a or b or c) and (not a or not b or not c)"
    return second_canonique
print("\n Alors on a " , second_forme_canonique () )
