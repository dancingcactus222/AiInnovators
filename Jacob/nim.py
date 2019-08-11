#nim
dots = 9

while not dots == 0:
    print("\n" + dots)
    move = int(input("How many dots do you take (1,2,3)\n"))
    dots = dots - move
    
    
print("You lose")