# Demo of ordered dict object

from collections import OrderedDict

def main():
    # lsit of sport teams with win and loss
    sport_teams = [("Barca", (8,2)),("Real",(7,0)),
                   ("Bayern", (8,2)),("Real_Betis",(7,0)),
                   ("Chelsea", (6,0)),("ManCity",(7,0))
                   ]
    # Sort by num of goal scored
    sorted_team = sorted(sport_teams, key = lambda t: t[1][0], reverse = True)
    print(sorted_team)
    
    teams = OrderedDict(sorted_team)
    print("\n sort",teams)
if __name__ == "__main__":
    main()
    