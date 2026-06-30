import random
def gamewin():
    if you==computer:
        print("you guess it right!!")
    else:
        if you>computer:
            print("choose the lesser number")
        elif you<computer:
            print("choose the greater number")
score=30           
computer=0
you=0
a = random.randint(1, 100)
computer = a
i=0

print("🙏welcome to the game🙏",'\n')
while computer!= you :
    you = int(input("enter the number:"))
    gamewin()
    i+=1


print(f"you have guess it in {i} times ")






