import turtle # turtle é uma biblioteca
import random
import time

tela = turtle.Screen()
tela.title("Jogo da Cobrinha Nokia3310")

pontos = 0 

tela.bgcolor("black") #A cor de fundo da tela é definida como preta
tela.setup(width=600, height=600)

tela.tracer(0)

#nasce uma serpente simpatica
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square") #square=quadrado
cobra.color("blue")
cobra.penup() # movimento
cobra.goto(0,0) #para onde é o movimento vai para... "go to"
cobra.direction = 'stop' #para onde ela vai

# comer para ficar forte e poder crescer!
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle") 
comida.color("red")
comida.penup() # movimento
comida.goto(0, 100) #para onde é o movimento vai para... "go to"

# ensinar os seus primeiros passos
def vai_pra_cima():
    cobra.direction = 'up'
def vai_pra_baixo():
    cobra.direction = 'down'
def vai_pra_direita():
    cobra.direction = 'right'
def vai_pra_esquerda():
    cobra.direction = 'left'

# fazer a cobra me obedecer
tela.listen()
tela.onkeypress(vai_pra_cima, "Up") # maiuscula por causa da biblioteca turtle
tela.onkeypress(vai_pra_baixo, "Down")
tela.onkeypress(vai_pra_direita, "Right")
tela.onkeypress(vai_pra_esquerda, "Left")

# o coração do aplicativo ta aqui

while True: 
        tela.update()
        if cobra.distance(comida) < 20:
             x = random.randint(-290,290)
             y = random.randint(-290,290)
             comida.goto(x,y)
             pontos += 10
             tela.title(f"Pontos: {pontos}")
        time.sleep(0.1) #sleep controla a execução do codigo
        if cobra.direction == "right": 
            x= cobra.xcor() #xcor cordenada do eixo x
            cobra.setx(x + 20)
        elif cobra.direction == "left": 
            x= cobra.xcor() 
            cobra.setx(x - 20)
        elif cobra.direction == "up": 
            y= cobra.ycor() 
            cobra.sety(y + 20)
        elif cobra.direction == "down": 
            y= cobra.ycor() 
            cobra.sety(y - 20)
        if cobra.xcor() > 290 or cobra.xcor() < -290 or cobra.ycor() > 290 or cobra.ycor() < -290:
            tela.title(f"GAME OVER! Pontuação final: {pontos}")
            cobra.goto(0,0)
            cobra.direction = "stop"
            break 



# até aqui!!!!
tela.mainloop()

