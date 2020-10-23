import pandas as pd 
import numpy
import csv
import matplotlib.pyplot as plt


# creation de dataframes
def createdataframes(season) :
    file = 'players_'+str(season)+'_test.csv'
    df = pd.read_csv(file)
    df = pd.DataFrame(df)
    df = df[["short_name","pace","shooting","passing","dribbling","defending","physic"]]
    return df

# top 10 joueurs en fonction d'une qualité
def topSkills(season, skill):
    df = createdataframes(season)
    df = df.sort_values(by = str(skill),ascending = False).head(10)
    return df[["short_name",skill]]

# filter par note attribuée à un skill en particulier
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

    return df

# filterBySkillDF = filterByskill(20, 'potential', 90, '>')
# print (filterBySkillDF)

##### GRAPHIQUES #####

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
    # plt.show()
    return plt

evolutionRashford = playerevolutionbar(20, "M. Rashford", "shooting")
evolutionRashford.savefig("rashford.jpg")

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
    # plt.show()

    return plt

evolutionAouar = playerevolutioncurve(20, "H. Aouar", "passing")
evolutionAouar.savefig("aouar.jpg")

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
    plt.plot(x,ypace, label="pace")
    plt.plot(x,yshoot, label="shooting")
    plt.plot(x,ypass, label="passing")
    plt.plot(x,ydribl, label="dribbling")
    plt.plot(x,ydefend, label="defending")
    plt.plot(x,yphys, label="physics")
    plt.title(player+' skills Evolution')
    plt.legend()
    plt.grid(True)
    # plt.show()  

    return plt

evolutionMbappe = playerevolutionAllcurve(20, "K. Mbappé")
evolutionMbappe.savefig("mbappe.jpg")
