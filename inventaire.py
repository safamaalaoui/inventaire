# nom d'utilisateur et mot de passe désigné en dur (En dur: veut dire que la valeur est la meme pour tout le monde)
from unicodedata import name


username = 'mohamed'
password = 'azerty'

# initialisation 
usernameInput = ''
passwordInput = ''


usernameInput = input ('username \n')
passwordInput=input ('password \n')
while (usernameInput != username and passwordInput!= password):
    print('Identifiants incorrectes \n')
    usernameInput = input ('username \n')
    passwordInput=input ('password \n')


print(f'bienvenu {username}') # formatage de chaine de caractère 

print ('0_ajouter produit \n 1_supprimer produit \n 2_modifier produit \n 3-lister produit \n -1_quiter\n')
options =[0,1,2,3,-1]
numero= 5
try:
    numero=int(input ('entrer une option'))
except:
        print('la valeur doit être numérique')

while (numero not in options):
    try:
        print ('option incorrecte \n')
        numero=int(input ('entrer une option '))
    except:
        print('la valeur doit être numérique')