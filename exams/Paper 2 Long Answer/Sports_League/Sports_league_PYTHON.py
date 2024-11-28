# March 2023 Paper 22 Long Answer question

for TeamCount in range (0, LeagueSize):
    TotalPoints[TeamCount] = 0		# Reset to zero the totals for each club’s result details
    AwayWins = 0
    HomeWins = 0
    Draws = 0
    Losses = 0
    for MatchCount in range (0, MatchNo):
        TotalPoints[TeamCount] = TotalPoints[TeamCount] + TeamPoints[TeamCount][MatchCount]
        if TeamPoints[TeamCount][MatchCount] == 3:
            AwayWins = AwayWins + 1
        elif TeamPoints[TeamCount][MatchCount] == 2:
            HomeWins = HomeWins + 1
        elif TeamPoints[TeamCount][MatchCount] == 1:
            Draws = Draws + 1
        else:
            Losses = Losses + 1
    # Output details of each team’s results
    print("\nTeam:", TeamName[TeamCount])
    print("Total points:", TotalPoints[TeamCount])
    print("Away wins:", AwayWins)
    print("Home wins:", HomeWins)
    print("Draws:", Draws)
    print("Losses:", Losses)
    # Check for highest and lowest results
    if TeamCount == 0:
        HighestResult = TotalPoints[TeamCount]
        LowestResult = TotalPoints[TeamCount]
    if TotalPoints[TeamCount] > HighestResult:
        HighestResult = TotalPoints[TeamCount]
        TopTeam = TeamCount
    if TotalPoints[TeamCount] < LowestResult:
        LowestResult = TotalPoints[TeamCount]
        BottomTeam = TeamCount
# Output names of the teams with the highest and lowest number of points
print("Top Team:", TeamName[TopTeam])
print("Bottom Team:", TeamName[BottomTeam])