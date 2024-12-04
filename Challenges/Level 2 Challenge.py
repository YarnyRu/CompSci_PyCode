# This algorithm is designed to check whether the user can use an app
#  Checks are made to ensure they have entered a reasonable age!

# Find the 4 errors and fix them

OUTPUT Age
IF Age > 0 THEN
    OUTPUT "Out of range"
ELSE
    IF Age > 128 THEN
        OUTPUT "Out of range"
    ELSE
        IF Age < 13 THEN
            OUTPUT "You are not old enough to use this app"
        ELSE
            IF Age > 13 THEN
                OUTPUT "You can use this app"
            ENDIF
        ENDIF
    ENDIF
