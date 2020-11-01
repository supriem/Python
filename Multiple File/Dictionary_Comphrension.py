# Demonstrate how to use dictionary comphrensions

def main():
    # define a list of temprature values
    ctemps = [0,12,34,100]
    
    # TODO: Use a comphrension to build a dictionary
    tempDict = {t: (t*9/5) + 32 for t in ctemps}
    print(tempDict)
    tempDict = {t: (t*9/5) + 32 for t in ctemps if t<100}
    print(tempDict)
    # TODO: Merge two dictionaries with a comphrension
    team1 = {"Jones": 24, "Jameson": 58, "Burns":7}
    team2 = {"White": 12, "Mscke": 88, "Perce": 4}
    
    new_team = {k:v for team in (team1,team2) for k,v in team.items()}
    print(new_team)
    
    
if __name__ == "__main__":
    main()
