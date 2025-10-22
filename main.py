quiestion1=input("1. Quien fue el primer hombre en la luna?")
answer1="neil armstrong"
score=0
user_answer1=(quiestion1).lower()
if user_answer1==answer1:
    print("corecto!")
    score+=1 

else:
    print("No!")

quiestion2=input("2. Cual es el mejor amigo del hombre?")
answer2="perro"
user_answer2=(quiestion2).lower()
if user_answer2==answer2:
    print("corecto!")
    score+=1

else:
    print("No!")

quiestion3=input("3. Cuando empezo la segunda guerra mundial?")
answer3="1939"
user_answer3=(quiestion3).lower()
if user_answer3==answer3:
    print("corecto!")
    score+=1
    print("Total puntos 0-3:",score)

else:
    print("No!")
    print("Total puntos 0-3:",score)
