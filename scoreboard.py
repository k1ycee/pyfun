def scoreboard():
    team1 = (input("Home team score: "))
    team2 = (input("Away team score: "))
    if team1 > team2:
        print("Home team won by "+team1+" - "+team2)

    elif team1 == team2:
        print("Both teams draw "+team1+" - "+team2)

    else:
        print("Home team lost by "+team1+" - "+team2)










scoreboard()