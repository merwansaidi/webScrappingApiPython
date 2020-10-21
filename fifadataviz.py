import pandas as pd 
import numpy
import csv
from IPython.display import display, HTML
# from tabulate import tabulate
import matplotlib.pyplot as plt



vartest = 'test..test'



# comment envoyer ces valeur à la fontion !!!
# commment afficher le retour de fontion !!!

# "long_name", "age", "dob",	"height_cm", "weight_kg", 
# create dataframes 
def createdataframes(season) :
    # header_list = ["short_name", "nationality", "club", "overall", "potential", "player_positions", "preferred_foot", "skill_moves", "work_rate", "player_tags", "pace", "shooting", "passing", "dribbling", "defending", "physic", "player_traits"]
    file = 'players_'+str(season)+'_test.csv'
    df = pd.read_csv(file)
    df = pd.DataFrame(df)
    return df
    



#    top x joueurs skill
def topskill(season, skill, top):
    df = createdataframes(season)
    df = df.sort_values(by = skill,ascending = False).head(top)
    print(df)


# topskill(20, 'shooting', 5)

#    > filtre skill, formule 3 champs de saisi ( liste des skill, opération, valeur )
def filterByskill(saison, skill, val, op):

    file = 'players_'+str(saison)+'.csv'
    df = pd.read_csv(file)
    if op == '>' :
        df_mask = df[skill]>val
        print(df[df_mask])
    elif op == '<' :
        df_mask = df[skill]<val
        print(df[df_mask])
    elif op == '=' :
        df_mask = df[skill]=val
        print(df[df_mask])
    else :
        print('no player for this condition')


# filterByskill(20, 'potential', 90, '>')

# best players by skill
def bestPskill(season, skill):
    # skill = str(skill)
    df = createdataframes(season)
    maxs = df[skill].max()
    df_mask = df[str(skill)]=maxs
    print(df_mask)


bestPskill(20, 'physic')

def describe_player(season):
    df = createdataframes(season)
    df.describe()


# bestPskill(20, 'power_jumping')

# createdataframes(20)

# championnat : liste des rencontres 
#       > classement 
#       > meilleur attaque 
#       > meilleur defence 
#       > lequipe gagner le plus / perdu le plus 




# championnat : liste des rencontres 
#       > classement 
#       > meilleur attaque 
#       > meilleur defence 
#       > lequipe gagner le plus / perdu le plus 