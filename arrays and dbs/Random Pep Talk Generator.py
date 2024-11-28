# Pep talk generator
import random
SetA = ["Cracking", "Inventive", "Genius", "Nerdy", "Good Old Fashioned"]
print (random.choice(SetA), "Pep Talk Generator")
#random.shuffle(SetA)
SetB = ["Champ,", "Fact:", "Just saying -", "Know this:", "Experts agree:", "Hear ye, hear ye -"]
#print (random.choice(SetB))
SetC = ["the mere idea of you", "what you got going on", "everything you do", "your hair today", 
        "that sparkle in your eye", "the way you roll"]
#print (random.choice(SetC))
SetD = ["rains magic", "is the next big thing", "makes birds sing", "makes my world go round", "gets the party started", 
        "roars like a lion", "is made of diamonds", "has serious game"]
print (random.choice(SetB), random.choice(SetC), random.choice(SetD))
