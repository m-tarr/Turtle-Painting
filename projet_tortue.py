import turtle
import random

# Customizable settings

Time_Set = 20 # 24 hours

Number_of_stars = 75 # Only works from 20 - 5.99
Number_of_trees = 4
Number_of_clouds = 6
Number_of_flowers = 15

Grass_Color = "darkgreen"
Tree_Leaves_Color = "green"

Flower_Size = 20
Cloud_Radius = 27.5
Pool_Length = 200
Pool_Radius = 70

# Drawing settings - DO NOT TOUCH

Tree_Length = 100
Tree_Width = 20

House_Height = 300
House_Width = 200
House_Base = 20

cloud_positions = []

# Create a Turtle screen/window

screen = turtle.Screen()
screen.title("House Maker Canevas")
screen.bgcolor("white")
WIDTH = 1200
HEIGHT = 800
screen.setup(width=WIDTH, height=HEIGHT)

# Create a Turtle object

brush = turtle.Turtle()
brush.shape("turtle")
brush.color("red")
brush.pencolor("")
brush.pensize(5)
brush.speed(60)




# BACKGROUND SECTION - GRASS, SKY, STARS, SUN & CLOUDS

def draw_grass():
    brush.fillcolor(Grass_Color)
    brush.penup()
    brush.goto(-WIDTH/2,-HEIGHT/2)
    brush.pendown()
    brush.begin_fill()

    for _ in range(2):
        brush.forward(WIDTH)
        brush.left(90)
        brush.forward(HEIGHT//3)
        brush.left(90)

    brush.end_fill()

def draw_sky():
    turtle.colormode(255)

    # Define color gradient for the transition
    day_color = (173, 216, 230)  # Light blue during the day
    night_color = (0, 0, 0)  # Black at night

    if 6 <= Time_Set < 20:
        # Daytime: Transition from light blue to darker blue (Day from 6 - 19.99)
        factor = (Time_Set - 6) / 14.0
        red = int(day_color[0] + (0 - day_color[0]) * factor)
        green = int(day_color[1] + (48 - day_color[1]) * factor)
        blue = int(day_color[2] + (82 - day_color[2]) * factor)
    else:
        # Nighttime: Transition from darker blue to black (Night from 20 - 5.99)
        red = 0
        green = 0
        blue = 0

    brush.pencolor(red, green, blue)
    brush.penup()
    brush.goto(-WIDTH / 2, -HEIGHT / 6)
    brush.pendown()
    brush.fillcolor((red, green, blue))
    brush.begin_fill()

    for _ in range(2):
        brush.forward(WIDTH)
        brush.left(90)
        brush.forward(HEIGHT * 2 / 3)
        brush.left(90)

    brush.end_fill()
    brush.setheading(90)

def draw_stars():
    if 20 <= Time_Set <= 24 or 0 <= Time_Set < 6:
        for _ in range(Number_of_stars):
            x = random.randint(-WIDTH / 2, WIDTH / 2)
            y = random.randint(0, HEIGHT // 2)
            size = random.randint(1, 4)
            brush.penup()
            brush.goto(x, y)
            brush.pendown()
            brush.pencolor("white")
            brush.dot(size)

def draw_sun_or_moon():
    brush.penup()
    brush.goto(WIDTH * 1 / 3 + 50, HEIGHT / 3)
    brush.pendown()
    brush.begin_fill()

    if 6 <= Time_Set < 20:
        # Daytime: Draw the sun
        brush.pencolor("Yellow")
        brush.fillcolor("Yellow")
        brush.circle(radius=50, extent=360)
        brush.end_fill()

        for _ in range(8):
            brush.penup()
            brush.goto(WIDTH * 1 / 3, HEIGHT / 3)
            brush.pencolor("Yellow")
            brush.setheading(45 * _)
            brush.pendown()
            brush.forward(100)
    else:
        # Nighttime: Draw the moon
        brush.fillcolor("silver")
        brush.circle(radius=50, extent=360)
        brush.end_fill()

    brush.setheading(90)

def draw_cloud(x, y, Cloud_Radius):
    brush.right(90)
    brush.pensize(5)
    brush.penup()
    brush.goto(x, y)
    brush.pendown()
    brush.pencolor("White")
    brush.fillcolor("White")

    for _ in range(3):
        brush.begin_fill()
        if _ == 1:  # Check if it's the middle semi-circle
            brush.circle(1.35 * Cloud_Radius, 180)
        else:
            brush.circle(Cloud_Radius, 180)
        brush.end_fill()
        brush.left(90)
        brush.forward(2 * Cloud_Radius)
        brush.penup()
        brush.forward(2 * Cloud_Radius)
        brush.pendown()
        brush.left(90)
    brush.setheading(0)
    brush.left(180)

def draw_randclouds():
    for _ in range(Number_of_clouds):
        while True:
            x = random.randint(-550, 300)
            y = random.randint(180, 350)
            is_overlapping = False

            for (cx, cy) in cloud_positions:
                distance = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
                if distance < 4 * Cloud_Radius:
                    is_overlapping = True
                    break

            if not is_overlapping:
                break

        cloud_positions.append((x, y))

        draw_cloud(x, y, Cloud_Radius)




# DESSIN DE LA RANGÉE D'ARBRES

def draw_tree(hauteur, largeur, x):
    brush.penup()
    brush.goto(x, -150)
    brush.pendown()
    brush.pencolor("saddlebrown")
    brush.fillcolor("saddlebrown")
    brush.begin_fill()

    # Tronc de l'arbre
    for _ in range(2):
        brush.forward(hauteur)
        brush.right(90)
        brush.forward(largeur)
        brush.right(90)
    brush.end_fill()

    # Ajustement pour centrer le triangle et ajouter les feuilles
    brush.forward(hauteur)
    brush.left(90)
    d = 80 / largeur
    brush.backward((80 - largeur) - 10)
    brush.pencolor(Tree_Leaves_Color)
    brush.fillcolor(Tree_Leaves_Color)
    brush.begin_fill()
    for _ in range(3):
        brush.forward(80)
        brush.right(120)
    brush.end_fill()
    brush.penup()
    brush.goto(x, -150)
    brush.right(90)

def draw_trees(hauteur, largeur, nb_arbre):
    x = 100
    for _ in range(nb_arbre):
        draw_tree(hauteur, largeur, x)
        x += 100  # Move to the next tree position




# DESSIN DES RANGÉES DE FLEURS DE COULEUR ALÉATOIRE

def draw_flower(grandeur, couleur): # Pour une seule fleur
    for _ in range(5):
        brush.begin_fill()
        brush.fillcolor(couleur)
        brush.pencolor(couleur)
        brush.forward(grandeur)
        brush.right(144)
        brush.end_fill()

def draw_flower_row(x, y, num_flowers, grandeur): # Pour rangées de fleurs
    brush.penup()
    brush.goto(x, y)
    brush.pendown()
    couleurs = ["white", "black", "red", "blue", "yellow", "orange", "purple", "pink", "gray",
                "brown", "cyan", "magenta", "turquoise", "gold", "silver"]

    for _ in range(num_flowers):
        couleur_choisi = random.choice(couleurs)
        draw_flower(grandeur, couleur_choisi)
        brush.penup()
        brush.right(90)
        brush.forward(50)
        brush.left(90)
        brush.pendown()

def draw_flowers(grandeur):
    y = -210
    brush.penup()
    brush.goto(-200, y)
    brush.pendown()

    num_flowers = Number_of_flowers
    while num_flowers > 0:
        num_in_row = min(num_flowers, 5) # Choisi le minimum entre le nombre de fleurs et 5 (le nombre max par rang)
        draw_flower_row(-200, y, num_in_row, grandeur)
        y -= 50
        num_flowers -= num_in_row



# DESSIN DE LA PISCINE

def draw_pool(longeur, rayon):
    brush.penup()
    brush.goto(200, -200)
    brush.pendown()
    brush.pencolor("navy")
    brush.fillcolor("blue")
    brush.begin_fill()
    brush.left(90)
    for _ in range(2):
        brush.circle(rayon, 180)
        brush.forward(longeur)
    brush.end_fill()




# DESSIN DE LA MAISON ET DE SES COMPOSANTES

def draw_chimney():
    brush.penup()
    brush.goto(-480, 30)
    brush.pendown()
    brush.pencolor("dimgray")
    brush.fillcolor("sienna")
    brush.begin_fill()
    for _ in range(2):
        brush.forward(100)
        brush.right(90)
        brush.forward(40)
        brush.right(90)
    brush.end_fill()
    brush.forward(100)
    brush.right(90)
    brush.forward(20)
    brush.left(90)
    brush.forward(15)
    brush.right(45)
    brush.forward(5)
    brush.left(45)

def draw_rectangle(hauteur, largeur):
    brush.penup()
    brush.goto(-500, -300)
    brush.pendown()
    brush.pencolor("mistyrose")
    brush.fillcolor("mistyrose")
    brush.begin_fill()
    for _ in range(3):
        brush.forward(hauteur)
        brush.right(90)
        brush.forward(largeur)
        brush.right(90)
    brush.end_fill()

def draw_roof(largeur):
    brush.left(270)
    brush.pencolor("dimgray")
    brush.fillcolor("sienna")
    brush.begin_fill()
    for _ in range(3):
        brush.forward(largeur)
        brush.right(120)
    brush.end_fill()

def draw_windows():
    draw_window(-425, -50)
    draw_window(-330, -50)
    draw_window(-425, -150)
    draw_window(-330, -150)

def draw_window(x, y):
    brush.penup()
    brush.goto(x, y)
    brush.pendown()
    brush.pencolor("gray")
    brush.fillcolor("white")
    brush.begin_fill()
    for _ in range(2):
        for _ in range(2):
            for _ in range(4):
                brush.forward(20)
                brush.left(90)
            brush.forward(20)
        brush.right(180)
    brush.end_fill()

def draw_door():
    brush.penup()
    brush.goto(-420, -220)
    brush.pendown()
    brush.pencolor("black")
    brush.fillcolor("red")
    brush.begin_fill()
    for _ in range(2):
        brush.left(90)
        brush.forward(80)
        brush.left(90)
        brush.forward(40)
    brush.end_fill()
    brush.penup()
    brush.goto(-390, -260)
    brush.pendown()
    brush.pencolor("black")
    brush.fillcolor("black")
    brush.begin_fill()
    rayon = 2
    brush.circle(rayon)
    brush.end_fill()

def draw_bush(x, y):
    brush.penup()
    brush.goto(x, y)
    brush.pendown()
    brush.pencolor("chartreuse4")
    brush.fillcolor("chartreuse4")
    brush.begin_fill()
    for _ in range(2):
        brush.forward(80)
        brush.left(90)
        brush.forward(40)
        brush.left(90)
    brush.end_fill()

def draw_path():
    brush.penup()
    brush.goto(-420, -220)
    brush.right(270)
    brush.forward(80)
    brush.pendown()
    brush.pencolor("black")
    brush.fillcolor("grey")
    brush.begin_fill()
    for _ in range(2):
        brush.forward(100)
        brush.left(90)
        brush.forward(40)
        brush.left(90)
    brush.end_fill()

def draw_house(hauteur, largeur, base):
    draw_chimney()
    draw_rectangle(hauteur, largeur)
    draw_roof(largeur)
    draw_windows()
    draw_door()
    draw_bush(-290, -260)
    draw_bush(-430, -260)
    draw_path()
    brush.left(180)

#---------------------------------------------------------------------------------------------------------------------#

# Programme principal #

#---------------------------------------------------------------------------------------------------------------------#

def main():
    draw_grass()
    draw_sky()
    draw_stars()
    draw_sun_or_moon()
    draw_trees(Tree_Length, Tree_Width,Number_of_trees)
    draw_house(House_Height, House_Width, House_Base)
    draw_flowers(Flower_Size)
    draw_pool(Pool_Length, Pool_Radius)
    draw_randclouds()


main()
screen.exitonclick()


