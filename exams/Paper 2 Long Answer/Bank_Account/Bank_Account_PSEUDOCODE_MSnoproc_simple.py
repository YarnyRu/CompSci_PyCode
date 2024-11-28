// Paper June 23/22 Simplified Partial Answer

REPEAT
    OUTPUT "Please enter your account number: "
    INPUT AccID
UNTIL AccID > 0 AND AccID < Size
CarryOn <- TRUE
OUTPUT “Please enter name: “
INPUT Name
OUTPUT “Please enter password: “
INPUT Password
IF Name <> Account[AccID, 1] THEN
    OUTPUT “Invalid name”
    CarryOn <- FALSE
ENDIF
IF Password <> Account[AccID, 2] THEN
    OUTPUT “Invalid password”
    CarryOn <- FALSE
ENDIF

WHILE CarryOn = TRUE DO
    OUTPUT "Menu"
    OUTPUT "1. Display balance"
    OUTPUT "2. Withdraw money"
    OUTPUT "3. Deposit money"
    OUTPUT "4. Exit"
    OUTPUT "Please choose 1, 2, 3 or 4: "
    INPUT Choice
    CASE OF Choice
        1 : OUTPUT “Your balance is”, AccDetails[AccID, 1]
        2 : OUTPUT "Please enter amount to withdraw: "
            INPUT Amount
            IF Amount > AccDetails[AccID,3] THEN
                OUTPUT "Amount greater than withdrawal limit."
            ENDIF
            IF Amount > AccDetails[AccID,2] + AccDetails[AccID,1] THEN
                OUTPUT "Amount greater than cash available."
            ENDIF
            // Only withdraw the amount if the criteria have been met
            IF Amount <= AccDetails[AccID,3] AND Amount <= AccDetails[AccID,2] + AccDetails[AccID,1] THEN
                    AccDetails[AccID,1] <- AccDetails[AccID,1] - Amount
            ENDIF
        3 : OUTPUT "Please enter a positive amount to deposit: "
            INPUT Amount
            AccDetails[AccID,1] <- AccDetails[AccID,1] + Amount
        4 : CarryOn <- FALSE
        OTHERWISE OUTPUT "Invalid choice"
    ENDCASE
ENDWHILE