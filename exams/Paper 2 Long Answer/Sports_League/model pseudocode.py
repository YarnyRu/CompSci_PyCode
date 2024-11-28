# March 2023 Paper 22 Long Answer question
# This first part you DO NOT NEED TO DO in the exam
LeagueSize <- 3
MatchNo = 4
TeamName = [""] * LeagueSize
TeamName = ["City", "Villa", "United"]
TeamPoints = [[0 for x in range(MatchNo)] for y in range(LeagueSize)]
TotalPoints = [0] * LeagueSize
HighestResult = 0
LowestResult = 999

# Open file
with open("match_scores.txt") as f:
 
# Read in one line at a time
    League = 0
    for line in f:
        line = line.strip()
        temp_input = line.split()
        for Count in range (0, MatchNo):
            TeamPoints[League][Count] = int(temp_input[Count])
        League += 1
# Start here to write the code to complete the program
# From here you need to comment your code

FOR TeamCounter <- 1 TO LeagueSize
    TotalPoints[TeamCounter] <- 0
    AwayWins <- 0
    HomeWins <- 0
    Draws <- 0
    Losses <- 0
    FOR MatchCounter <- 1 TO MatchNo
        TotalPoints[TeamCounter] <- TotalPoints[TeamCounter] + TeamPoints[TeamCounter][MatchCounter]
        CASE TeamPoints[TeamCounter][MatchCounter] OF
            3:	AwayWins = AwayWins + 1
            2:  HomeWins = HomeWins + 1
            1:  Draws = Draws + 1
            OTHERWISE: Losses = Losses + 1
        ENDCASE
    NEXT MatchCounter

    PRINT "Team:", TeamName[TeamCounter]
    PRINT "Total points:", TotalPoints[TeamCounter]
    PRINT "Away wins:", AwayWins
    PRINT "Home wins:", HomeWins
    PRINT "Draws:", Draws
    PRINT "Losses:", Losses

# Check for highest and lowest results
    IF TeamCounter = 1 THEN
        HighestResult <- TotalPoints[TeamCounter]
        LowestResult <- TotalPoints[TeamCounter]
    ENDIF
    IF TotalPoints[TeamCounter] > HighestResult THEN
        HighestResult <- TotalPoints[TeamCounter]
        TopTeam <- TeamCounter
    ELSE
        IF TotalPoints[TeamCounter] < LowestResult THEN
            LowestResult <- TotalPoints[TeamCounter]
            BottomTeam <- TeamCounter
        ENDIF
    ENDIF
NEXT TeamCounter

# Output names of the teams with the highest and lowest number of points
PRINT "Top Team:", TeamName[TopTeam]
PRINT "Bottom Team:", TeamName[BottomTeam]

