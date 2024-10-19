import random
#affichons des questions a choix multiples sous forme de dictionnaire
question= {
"what are the countries of africa?":["A.zambie","B.australie","C.ghana","D.fidji"],
       "what is 4**2?" :["A.8","B.16","C.32", "D.64"] 
}
  # FONCTION POUR VALIER LE QUIZ
def quiz(question):
  score=0
  #melanger l'ordre des questions
question=list(question.keys())
random.shuffle(question)

  #parcourir les question
for question in question:
  print(question)
  answer=question[0:3]
  for answer in answer:
    print(answer)
  
  #la reponse de l'utilisateur
user_answer=input("your answer(A,B,C,D):").upper()

#Verifier le reopnse de l'utilisateur
if user_answer==answer:
  print("correct answer")
  score += 1
else:
  print("wrong answer")

#afficher le score final
print("your score is {score}/{len(question)}.")

#executer le quiz
quiz(question)
