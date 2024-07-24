import turtle

def drawStar(myTurtle, numberOfSides, lengthOfSides) :
# Following 3 'if' statements are guard statements, which filters out situations when user inputs the number 
# of sides as an even number or smaller than 1 and when user inputs the length of the sides equal or smaller
# than 0 
    if numberOfSides % 2 == 0:
        print("Number of sides must be an odd number.")
        return
    if numberOfSides <= 1:
        print("Number of sides should be a positive odd number, which is bigger than 1.")
        return
    if lengthOfSides <= 0:
        print("Length of the sides can't be equal or smaller than 0.")
        return
    # Draws a 3-pointed star
    wn = turtle.Screen()
    if numberOfSides == 3:
        myTurtle.forward(lengthOfSides * 3 / 4)
        for n in range(numberOfSides + 1):
            if n % 2 == 0:
                myTurtle.left(30)
                myTurtle.forward(lengthOfSides / 2)
            else:
                myTurtle.right(150)
                myTurtle.forward(lengthOfSides / 2)
        myTurtle.left(40)
        myTurtle.forward(lengthOfSides * 3 / 4)
        wn.exitonclick()
        return
    # Draws a star with as many tips as user decides
    turnAngle = 180 - ((360 / numberOfSides) / 2)
    for i in range (numberOfSides):
        myTurtle.forward(lengthOfSides)
        myTurtle.right(turnAngle)
    wn.exitonclick()

t = turtle.Turtle()
drawStar(t, 9, 150)