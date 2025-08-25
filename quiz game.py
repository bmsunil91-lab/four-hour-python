question=("how many  word in alphabet?:",
          "how many bouns in human body?:",)

option=(("A.23","B.24","C.26","D.34"),
        ("A. 116","B.113","C.111","D.118"))

answer=("C","D")
guess=[]
score=0
question_num=0

for question in question:
 print("---------------------")
 print(question)
 for option in option [question_num]:
  print(option)

 guess=input("Enter(A,B,C):").upper()
if guess==answer[question_num]:
   score+=1
   print("CORRECT!")
else:
 print("in corret!")
 print(f"{answer[question_num]} is the is correct")
 question_num+=1
 