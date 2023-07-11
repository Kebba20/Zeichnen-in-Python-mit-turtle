from turtle import*

#turtle.shape("turtle")#Schildkröte wird auf dem Bildschirm angezeigt

# Fenster Größe anpassen

height = 500 #
width = 1000
screen = Screen()
screen.setup(width, height)


leonardo = 	Turtle() #Name des Turtles
leonardo.speed(6) # Geschwindigkeit des Turtles
leonardo.color("green") # Farbe des Turtles
leonardo.shape("turtle")
bgcolor("black") # Hintergrundfarbe
leonardo.pensize(10) # Größer des Stiftes


#Buchstabe (A) wird gezeichnet.
leonardo.left(75)
leonardo.forward(207)
leonardo.right(150)
leonardo.forward(205)
leonardo.backward(80)
leonardo.left(255)
leonardo.forward(63)
leonardo.penup() # Zeichnung wird unsichtbar gestellt
leonardo.right(205)
leonardo.forward(170)
leonardo.left(25)



#Buchstabe (D) wird gezeichnet.
leonardo.pendown() # Zeichung wird wieder sichtbar gestellt.
leonardo.circle(100,180)
leonardo.left(90)
leonardo.forward(200)

leonardo.penup()
leonardo.right(270)
leonardo.forward(150)




#Buchstabe (A) wird gezeichnet.
leonardo.pendown()
leonardo.left(75)
leonardo.forward(207)
leonardo.right(150)
leonardo.forward(205)
leonardo.backward(80)
leonardo.left(255)
leonardo.forward(63)
leonardo.hideturtle() # Turtle verschwindet vom Bildschirm.