Correct <- False
Count <- 0
WHILE Correct = False AND Count < 3 DO
    INPUT Password
    IF Password = "Secret" THEN
        Correct <- True
    ELSE
        OUTPUT "Incorrect password"
        Count <- Count + 1
    ENDIF
IF Correct = True THEN
    OUTPUT "Password accepted"
ELSE
    OUTPUT "You have reached the maximum number of tries"
ENDIF
