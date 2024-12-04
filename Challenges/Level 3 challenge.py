# This algorithm is designed to search for a product in an array of 50 products and
#  report whether the item is found or not

NumberProducts <- 50        // length of array ProductName[]
OUTPUT "Please enter product to find: "
INPUT Product
Found <- False
Counter <- 1
REPEAT
    IF Product = ProductName[Counter] THEN
        Found <- False
    ELSE
        Counter <- Counter + 1
    ENDIF
UNTIL Found = True AND Counter > NumberProducts
IF Found THEN
    OUTPUT Product, "found at position", Counter, "in the list."
ELSE
    OUTPUT Name, "not found."
ENDIF
