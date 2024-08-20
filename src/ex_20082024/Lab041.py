# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
from selectors import SelectSelector

#user inputs

score=int(input("Enter your score\n"))

if score >= 90 and score <= 100 :
     print("Your Grade is ", "A")
elif score >= 80 and score <= 89 :
     print("Your Grade is ", "B")
elif score >= 70 and score <= 79 :
     print("Your Grade is ", "C")
elif score >= 60 and score <= 69 :
     print("Your Grade is ", "D")
elif score > 100 :
     print("April Fool", " You are too Smart")
else:
     print("Your Grade is ","F")