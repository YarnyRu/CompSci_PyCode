// Contacts PSEUDOCODE with procedures

CarryOn <- TRUE
WHILE CarryOn DO		// Allows program to continue indefinitely 
    OUTPUT "Please choose one of the following:"	// Display menu
    OUTPUT "1: Enter new contacts"
    OUTPUT "2: Display your contacts"
    OUTPUT "3: Delete all contacts"
    INPUT Choice
    WHILE Choice < 1 OR Choice > 3 DO				// Validate choice as 1, 2 or 3
        OUTPUT "Incorrect entry – please enter 1, 2, or 3"
        INPUT Choice
    ENDWHILE
    CASE OF Choice
        1: Enter_Contacts() 	// enter new contacts
        2: Display_Contacts()	// display all contacts
        3: Delete_Contacts()	// delete all contacts
    ENDCASE 
ENDWHILE

PROCEDURE Enter_Contacts()
    IF CurrentSize = 100 THEN	// Check if contacts are full
        OUTPUT "Your contacts are full"
    ELSE
        OUTPUT "Number of new contacts to enter (maximum of 5): "
        INPUT NewContacts
        WHILE NewContacts < 1 OR NewContacts > 5 DO
            OUTPUT "You may only enter between 1 and 5 contacts. Please try again"
            INPUT NewContacts
        ENDWHILE
        WHILE CurrentSize + NewContacts > 100  // checks the maximum size is not exceeded
            OUTPUT "Not enough space in your contacts"
            OUTPUT "The maximum number you may input is ", 100 – CurrentSize
            INPUT NewContacts
        ENDWHILE
        FOR Count <- CurrentSize + 1 TO CurrentSize + NewContacts		// Store new contacts in Contacts[] array
            OUTPUT "Enter the contact name as last name, first name"
            INPUT Contacts[Count, 1]
            OUTPUT "Enter the telephone number"
            INPUT Contacts[Count, 2]
        NEXT Count
        CurrentSize <- CurrentSize + NewContacts
        IF CurrentSize >= 2 THEN		// bubble sort to sort array if it contains 2 or more contacts
            REPEAT
                Flag <- FALSE
                FOR Count <- 1 TO CurrentSize-1
                    IF Contacts[Count + 1, 1] < Contacts[Count, 1] THEN
                        Flag <- TRUE
                        Temp1 <- Contacts[Count, 1]
                        Temp2 <- Contacts[Count, 2]
                        Contacts[Count, 1] <- Contacts[Count + 1, 1]
                        Contacts[Count, 2] <- Contacts[Count + 1, 2]
                        Contacts[Count + 1, 1] <- Temp1
                        Contacts[Count + 1, 2] <- Temp2
                    ENDIF
                NEXT Count
            UNTIL NOT Flag
        ENDIF
    ENDIF
ENDPROCEDURE

PROCEDURE Display_Contacts()
    IF CurrentSize > 0 THEN
        OUTPUT "Name and Telephone Number"
        FOR Count <- 1 TO CurrentSize
            OUTPUT Contacts[Count, 1], " ", Contacts[Count, 2]
        NEXT Count
    ENDIF
ENDPROCEDURE

PROCEDURE Delete_Contacts()
    FOR Count <- 1 TO 100
        FOR Count2 <- 1 TO 2
            Contacts[Count, Count2] <- ""
        NEXT Count2
    NEXT Count
ENDPROCEDURE