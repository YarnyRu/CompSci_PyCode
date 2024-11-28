// Paper June 23/22

PROCEDURE CheckDetails (AccID: INTEGER)
    DECLARE Name, Password : STRING 		// Local variables
    Valid <- FALSE
    IF AccID < 0 OR AccID > Size THEN
        OUTPUT “Invalid Account Number”
    ELSE
        OUTPUT “Please enter name: “
        INPUT Name
        OUTPUT “Please enter password: “
        INPUT Password
        IF Name <> Account[AccID, 1] OR Password <> Account[AccID, 2] THEN
            OUTPUT “Invalid name or password.”
        ELSE
            Valid <- TRUE
        ENDIF
    ENDIF
ENDPROCEDURE

PROCEDURE Balance(AccID: INTEGER)
    OUTPUT “Your balance is”, AccDetails[AccID, 1]
ENDPROCEDURE

PROCEDURE WithDrawal(AccID : INTEGER)
    DECLARE Amount : REAL // local variable
    REPEAT
        OUTPUT "Please enter amount to withdraw: "
        INPUT Amount
        IF Amount > AccDetails[AccID,3] THEN
            OUTPUT "Amount greater than withdrawal limit."
        ENDIF
        IF Amount > AccDetails[AccID,2] + AccDetails[AccID,1] THEN
            OUTPUT "Amount greater than cash available."
        ENDIF
        IF Amount <= AccDetails[AccID,3] AND Amount < AccDetails[AccID,2] + AccDetails[AccID,1] THEN
            AccDetails[AccID,1] <- AccDetails[AccID,1] - Amount
        ENDIF
    UNTIL Amount <= AccDetails[AccID,3] AND Amount <= AccDetails[AccID,2] + AccDetails[AccID,1] AND Amount > 0
ENDPROCEDURE

PROCEDURE Deposit(AccID : INTEGER)
    DECLARE Amount : REAL // local variable
    REPEAT
        OUTPUT "Please enter a positive amount to deposit: "
        INPUT Amount
    UNTIL Amount > 0
    AccDetails[AccID,1] <- AccDetails[AccID,1] + Amount
ENDPROCEDURE

// Declarations of global variables for information – not required in candidate responses
DECLARE AccountNumber, Choice : INTEGER
DECLARE Valid, Exit : BOOLEAN

OUTPUT "Please enter your account number: "
INPUT AccountNumber
CheckDetails(AccountNumber)
IF Valid = TRUE THEN
    REPEAT
        OUTPUT "Menu"
        OUTPUT "1. Display balance"
        OUTPUT "2. Withdraw money"
        OUTPUT "3. Deposit money"
        OUTPUT "4. Exit"
        OUTPUT "Please choose 1, 2, 3 or 4: "
        INPUT Choice
        CASE OF Choice
            1 : Balance(AccountNumber)
            2 : Withdrawal(AccountNumber)
            3 : Deposit(AccountNumber)
            4 : Exit <- TRUE
            OTHERWISE OUTPUT "Invalid choice"
        ENDCASE
    UNTIL Exit = TRUE
ELSE
    OUTPUT "Invalid account number."
ENDIF