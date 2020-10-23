import pandas as pd 
import numpy
import csv
#from IPython.display import display, HTML
# from tabulate import tabulate
import matplotlib.pyplot as plt


# create dataframes 
def createdataframes(season) :
    # header_list = ["short_name", "nationality", "club", "overall", "potential", "player_positions", "preferred_foot", "skill_moves", "work_rate", "player_tags", "pace", "shooting", "passing", "dribbling", "defending", "physic", "player_traits"]
    file = 'players_'+str(season)+'_test.csv'
    df = pd.read_csv(file)
    df = pd.DataFrame(df)
    return df
    



#    top x joueurs skill
def topskill(season, skill):
    df = createdataframes(season)
    df = df.sort_values(by = str(skill),ascending = False).head(10)
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



# def describe_player(season):
#     df = createdataframes(season)
#     df.describe()



# graphs 

def playerevolutionbar(season, player, skill):
    df20 = createdataframes(season)
    df19 = createdataframes(season-1)
    df18 = createdataframes(season-2)
    listskilss = ["short_name","pace","shooting","passing","dribbling","defending","physic"]
    df20new = df20[listskilss]
    df19new = df19[listskilss]
    df18new = df18[listskilss]
    df18new.columns = ['short_name', 'pace18', 'shooting18', 'passing18', 'dribbling18', 'defending18','physic18']
    df19new.columns = ['short_name', 'pace19', 'shooting19', 'passing19', 'dribbling19', 'defending19','physic19']
    df20new.columns = ['short_name', 'pace20', 'shooting20', 'passing20', 'dribbling20', 'defending20','physic20']

    df_evolution = pd.merge(df18new, df19new, on='short_name').merge(df20new, on='short_name')
    df_reduit = df_evolution[df_evolution['short_name']== str(player)][[str(skill)+"18", str(skill)+"19", str(skill)+"20"]]
   
    x = [skill+" FIFA 18", skill+" FIFA 19", skill+" FIFA 20"]
    y = df_reduit.iloc[0].values
    plt.bar(x,y)
    plt.title(player+" "+skill+' Evolution')
    plt.show()


#playerevolutionbar(20, "L. Suárez", "passing")

def playerevolutioncurve(season, player, skill):
    df20 = createdataframes(season)
    df19 = createdataframes(season-1)
    df18 = createdataframes(season-2)
    listskilss = ["short_name","pace","shooting","passing","dribbling","defending","physic"]
    df20new = df20[listskilss]
    df19new = df19[listskilss]
    df18new = df18[listskilss]
    df18new.columns = ['short_name', 'pace18', 'shooting18', 'passing18', 'dribbling18', 'defending18','physic18']
    df19new.columns = ['short_name', 'pace19', 'shooting19', 'passing19', 'dribbling19', 'defending19','physic19']
    df20new.columns = ['short_name', 'pace20', 'shooting20', 'passing20', 'dribbling20', 'defending20','physic20']

    df_evolution = pd.merge(df18new, df19new, on='short_name').merge(df20new, on='short_name')
    df_reduit = df_evolution[df_evolution['short_name']== str(player)][[str(skill)+"18", str(skill)+"19", str(skill)+"20"]]

    x = [skill+" FIFA 18", skill+" FIFA 19", skill+" FIFA 20"]
    y = df_reduit.iloc[0].values

    plt.plot(x,y)
    plt.title(player+" "+skill+' Evolution')
    plt.show()





def playerevolutionAllcurve(season, player):
    df20 = createdataframes(season)
    df19 = createdataframes(season-1)
    df18 = createdataframes(season-2)
    listskilss = ["short_name","pace","shooting","passing","dribbling","defending","physic"]
    df20new = df20[listskilss]
    df19new = df19[listskilss]
    df18new = df18[listskilss]
    df18new.columns = ['short_name', 'pace18', 'shooting18', 'passing18', 'dribbling18', 'defending18','physic18']
    df19new.columns = ['short_name', 'pace19', 'shooting19', 'passing19', 'dribbling19', 'defending19','physic19']
    df20new.columns = ['short_name', 'pace20', 'shooting20', 'passing20', 'dribbling20', 'defending20','physic20']

    df_evolution = pd.merge(df18new, df19new, on='short_name').merge(df20new, on='short_name')
    df_reduit = df_evolution[df_evolution['short_name']== str(player)]
   
    x = ["FIFA 20", "FIFA 19", "FIFA 18"]
    ypace = df_reduit[["pace18", "pace19", "pace20"]].iloc[0].values
    yshoot = df_reduit[["shooting18", "shooting19", "shooting20"]].iloc[0].values 
    ypass = df_reduit[["passing18", "passing19", "passing20"]].iloc[0].values 
    ydribl = df_reduit[["dribbling18", "dribbling19", "dribbling20"]].iloc[0].values 
    ydefend = df_reduit[["defending18", "defending19", "defending20"]].iloc[0].values
    yphys = df_reduit[["physic18", "physic19", "physic20"]].iloc[0].values

    plt.plot(x,ypace)
    plt.plot(x,yshoot)
    plt.plot(x,ypass)
    plt.plot(x,ydribl)
    plt.plot(x,ydefend)
    plt.plot(x,yphys)
    plt.title(player+' skills Evolution')
    plt.grid(True)
    plt.show()


playerevolutionAllcurve(20, "P. Pogba")

# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
# ax.bar(langs,students)
# plt.show()





# "short_name","pace","shooting","passing","dribbling","defending","physic"
# # grand data 15 ( 5 colonnes depuis chaque df )
# df18_new = df18[["short_name","pace","shooting","passing","dribbling","defending","physic"]]
# df19_new = df19[["short_name","pace","shooting","passing","dribbling","defending","physic"]]
# df20_new = df20[["short_name","pace","shooting","passing","dribbling","defending","physic"]]



# def topclubByskill(skill, top):
#     df = createdataframes(20)
#     mask = ["FC Barcelona", "Juventus", "Paris Saint-Germain", "Atlético Madrid", "Real Madrid", "Manchester City", "Liverpool",
#             "Napoli", "Tottenham Hotspur", "Manchester United", "Chelsea", "FC Bayern München", "Inter", "Borussia Dortmund", "Arsenal",
#             "Valencia CF", "AS Monaco", "FC Girondins de Bordeaux", "SL Benfica", "Olympique de Marseille", "Lokomotiv Moscow",
#             "Galatasaray SK", "Sevilla FC", "Roma", "Sporting CP"]
    
#     df_mask = df["club"] in mask
#     df[df[df_mask]]
#     dfnew = df[["club", str(skill)]]

#     dfcalc = dfnew.groupby("club")[str(skill)].mean()
#     # dfcalc.rename[]
#     dfcalc = pd.DataFrame(dfcalc)<
#     # dfcalc.columns = ['National team', 'avg']
#     print(df_mask)
#     print(dfcalc.sort_values(str(skill), ascending=False).head(top))
#     #print(dfcalc)


# topclubByskill("physic", 10)

