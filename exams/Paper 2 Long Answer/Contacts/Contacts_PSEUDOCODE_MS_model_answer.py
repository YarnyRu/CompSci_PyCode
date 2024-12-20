// Contacts

DECLARE Contacts : ARRAY[1:100, 1:2] OF STRING
DECLARE CurrentSize : INTEGER
DECLARE Cont : BOOLEAN
DECLARE Choice : INTEGER
DECLARE NewContacts : INTEGER
DECLARE Count : INTEGER
DECLARE Count2 : INTEGER
DECLARE Flag : BOOLEAN
DECLARE Temp1 : STRING
DECLARE Temp2 : STRING

// the number of contacts in the array
CurrentSize <- 0

// to allow program to continue indefinitely
Cont <- TRUE
WHILE Cont DO
    // display menu
    OUTPUT "Please choose one of the following: "
    OUTPUT "Press 1 to enter new contacts "
    OUTPUT "Press 2 to display your contacts "
    OUTPUT "Press 3 to delete all contacts "
    INPUT Choice
    // validate choice as 1, 2 or 3
    WHILE Choice = 1 AND CurrentSize = 100 DO
        OUTPUT "Your contacts are full, please enter 2 or 3"
        INPUT Choice
    ENDWHILE
    WHILE Choice < 1 OR Choice > 3 DO
        OUTPUT "Incorrect entry – please enter 1, 2, or 3"
        INPUT Choice
    ENDWHILE
    // enter new contacts
    IF Choice = 1
    THEN
        OUTPUT "How many contacts (1 to 5 only)?"
        INPUT NewContacts
        // validates new contacts input
        WHILE NewContacts < 1 OR NewContacts > 5 DO
            OUTPUT "You may only enter between 1 and 5 contacts. Please try again"
            INPUT NewContacts
        ENDWHILE
        // checks the maximum size is not exceeded
        WHILE CurrentSize + NewContacts > 100
            OUTPUT "Not enough space in your contacts"
            OUTPUT "The maximum number you may input is ", 100 – CurrentSize
            INPUT NewContacts
        ENDWHILE
        FOR Count  CurrentSize + 1 TO CurrentSize + NewContacts
            OUTPUT "Enter the contact name as last name, first name"
            INPUT Contacts[Count, 1]
            OUTPUT "Enter the telephone number"
            INPUT Contacts[Count, 2]
        NEXT Count
        CurrentSize  CurrentSize + NewContacts
        // bubble sort to sort array if it contains 2 or more contacts
        IF CurrentSize >= 2
        THEN
            REPEAT
                Flag  FALSE
                FOR Count  1 TO CurrentSize-1
                    IF Contacts[Count + 1, 1] <
                        Contacts[Count, 1]
                    THEN
                        Flag  TRUE
                        Temp1  Contacts[Count, 1]
                        Temp2  Contacts[Count, 2]
                        Contacts[Count, 1]  Contacts[Count + 1, 1]
                        Contacts[Count, 2]  Contacts[Count + 1, 2]
                        Contacts[Count + 1, 1]  Temp1
                        Contacts[Count + 1, 2]  Temp2
                    ENDIF
                NEXT Count
            UNTIL NOT Flag
        ENDIF
    ENDIF
    // display all contacts
    IF Choice = 2
    THEN
        IF CurrentSize > 0
        THEN
            OUTPUT "Name and Telephone Number"
            FOR Count  1 TO CurrentSize
                OUTPUT Contacts[Count, 1], " ", Contacts[Count, 2]
            NEXT Count
        ENDIF
    ENDIF
    // delete all contacts
    IF Choice = 3
    THEN
        FOR Count  1 TO 100
            FOR Count2  1 TO 2
                Contacts[Count, Count2]  ""
            NEXT Count2
        NEXT Count
    ENDIF
ENDWHILE