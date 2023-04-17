import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image



# Create the main window
root = tk.Tk()
root.title("Market Calculator")


# Create tabs
tab_control = ttk.Notebook(root)

# Create the first tab and add widgets to it
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Main Market")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tropical Island Farm")

tab_control.pack(expand=1, fill='both')

# Load the image
wildflowers_image = Image.open("assets/wildflowers.png")
corn_image = Image.open("assets/corn.png")
cabbage_image = Image.open("assets/cabbage.png")
wheat_image = Image.open("assets/wheat.png")
dandelion_image = Image.open("assets/dandelion.png")
lambslettuce_image = Image.open("assets/lambslettuce.png")
carrots_image = Image.open("assets/carrots.png")
barley_image = Image.open("assets/barley.png")
daisies_image = Image.open("assets/daisies.png")
eggs_image = Image.open("assets/eggs.png")
pigs_image = Image.open("assets/pigs.png")
milk_image = Image.open("assets/milk.png")
goatscheese_image = Image.open("assets/goatscheese.png")
duckfeathers_image = Image.open("assets/duckfeathers.png")
sheepwool_image = Image.open("assets/sheepwool.png")
graywool_image = Image.open("assets/graywool.png")
whitewool_image = Image.open("assets/whitewool.png")
apples_image = Image.open("assets/apples.png")
cherries_image = Image.open("assets/cherries.png")
almonds_image = Image.open("assets/almonds.png")
peaches_image = Image.open("assets/peaches.png")
lavender_image = Image.open("assets/lavender.png")
aloevera_image = Image.open("assets/aloevera.png")
jasmine_image = Image.open("assets/jasmine.png")
vanilla_image = Image.open("assets/vanilla.png")
cocoa_image = Image.open("assets/cocoa.png")
olives_image = Image.open("assets/olives.png")
citrusfruits_image = Image.open("assets/citrusfruits.png")
essenceoflavender_image = Image.open("assets/essenceoflavender.png")
aloeveragel_image = Image.open("assets/aloeveragel.png")
essenceofjasmine_image = Image.open("assets/essenceofjasmine.png")
vanillaextract_image = Image.open("assets/vanillaextract.png")
cocoapowder_image = Image.open("assets/cocoapowder.png")
oliveoil_image = Image.open("assets/oliveoil.png")
citrusoil_image = Image.open("assets/citrusoil.png")
dough_image = Image.open("assets/dough.png")
bread_image = Image.open("assets/bread.png")
croissant_image = Image.open("assets/croissant.png")
applestrudel_image = Image.open("assets/applestrudel.png")
sachertorte_image = Image.open("assets/sachertorte.png")
carrotcake_image = Image.open("assets/carrotcake.png")
applejam_image = Image.open("assets/applejam.png")
berryjam_image = Image.open("assets/berryjam.png")
orangejam_image = Image.open("assets/orangejam.png")
cherryjam_image = Image.open("assets/cherryjam.png")
peachjam_image = Image.open("assets/peachjam.png")
butter_image = Image.open("assets/butter.png")
cherryyoghurt_image = Image.open("assets/cherryyoghurt.png")
cream_image = Image.open("assets/cream.png")
cheese_image = Image.open("assets/cheese.png")
foresthoney_image = Image.open("assets/foresthoney.png")
flowerhoney_image = Image.open("assets/flowerhoney.png")
oranges_image = Image.open("assets/oranges.png")
peanuts_image = Image.open("assets/peanuts.png")
grapes_image = Image.open("assets/grapes.png")
peacocks_image = Image.open("assets/peacocks.png")
lemurs_image = Image.open("assets/lemurs.png")
mangos_image = Image.open("assets/mangos.png")
coconuts_image = Image.open("assets/coconuts.png")
bananas_image = Image.open("assets/bananas.png")
orangefizz_image = Image.open("assets/orangefizz.png")
peanutsnack_image = Image.open("assets/peanutsnack.png")
summerslush_image = Image.open("assets/summerslush.png")
nutsandgrapes_image = Image.open("assets/nutsandgrapes.png")
fruityflip_image = Image.open("assets/fruityflip.png")
tropicstar_image = Image.open("assets/tropicstar.png")

# Create a dictionary to store the images
assets = {
    "Wildflowers": ImageTk.PhotoImage(wildflowers_image),
    "Corn": ImageTk.PhotoImage(corn_image),
    "Cabbage": ImageTk.PhotoImage(cabbage_image),
    "Wheat": ImageTk.PhotoImage(wheat_image),
    "Dandelion": ImageTk.PhotoImage(dandelion_image),
    "Lamb's Lettuce": ImageTk.PhotoImage(lambslettuce_image),
    "Carrots": ImageTk.PhotoImage(carrots_image),
    "Barley": ImageTk.PhotoImage(barley_image),
    "Daisies": ImageTk.PhotoImage(daisies_image),
    "Eggs": ImageTk.PhotoImage(eggs_image),
    "Pigs": ImageTk.PhotoImage(pigs_image),
    "Milk": ImageTk.PhotoImage(milk_image),
    "Goat's Cheese": ImageTk.PhotoImage(goatscheese_image),
    "Duck Feathers": ImageTk.PhotoImage(duckfeathers_image),
    "Sheep Wool": ImageTk.PhotoImage(sheepwool_image),
    "Gray Wool": ImageTk.PhotoImage(graywool_image),
    "White Wool": ImageTk.PhotoImage(whitewool_image),
    "Apples": ImageTk.PhotoImage(apples_image),
    "Cherries": ImageTk.PhotoImage(cherries_image),
    "Almonds": ImageTk.PhotoImage(almonds_image),
    "Peaches": ImageTk.PhotoImage(peaches_image),
    "Lavender": ImageTk.PhotoImage(lavender_image),
    "Aloe Vera": ImageTk.PhotoImage(aloevera_image),
    "Jasmine": ImageTk.PhotoImage(jasmine_image),
    "Vanilla": ImageTk.PhotoImage(vanilla_image),
    "Cocoa": ImageTk.PhotoImage(cocoa_image),
    "Olives": ImageTk.PhotoImage(olives_image),
    "Citrus Fruits": ImageTk.PhotoImage(citrusfruits_image),
    "Essence of Lavender": ImageTk.PhotoImage(essenceoflavender_image),
    "Aloe Vera Gel": ImageTk.PhotoImage(aloeveragel_image),
    "Essence of Jasmine": ImageTk.PhotoImage(essenceofjasmine_image),
    "Vanilla Extract": ImageTk.PhotoImage(vanillaextract_image),
    "Cocoa Powder": ImageTk.PhotoImage(cocoapowder_image),
    "Olive Oil": ImageTk.PhotoImage(oliveoil_image),
    "Citrus Oil": ImageTk.PhotoImage(citrusoil_image),
    "Dough": ImageTk.PhotoImage(dough_image),
    "Bread": ImageTk.PhotoImage(bread_image),
    "Croissant": ImageTk.PhotoImage(croissant_image),
    "Apple Strudel": ImageTk.PhotoImage(applestrudel_image),
    "Sachertorte": ImageTk.PhotoImage(sachertorte_image),
    "Carrot Cake": ImageTk.PhotoImage(carrotcake_image),
    "Apple Jam": ImageTk.PhotoImage(applejam_image),
    "Berry Jam": ImageTk.PhotoImage(berryjam_image),
    "Orange Jam": ImageTk.PhotoImage(orangejam_image),
    "Cherry Jam": ImageTk.PhotoImage(cherryjam_image),
    "Peach Jam": ImageTk.PhotoImage(peachjam_image),
    "Butter": ImageTk.PhotoImage(butter_image),
    "Cherry Yoghurt": ImageTk.PhotoImage(cherryyoghurt_image),
    "Cream": ImageTk.PhotoImage(cream_image),
    "Cheese": ImageTk.PhotoImage(cheese_image),
    "Forest Honey": ImageTk.PhotoImage(foresthoney_image),
    "Flower Honey": ImageTk.PhotoImage(flowerhoney_image),
    "Oranges": ImageTk.PhotoImage(oranges_image),
    "Peanuts": ImageTk.PhotoImage(peanuts_image),
    "Grapes": ImageTk.PhotoImage(grapes_image),
    "Peacocks": ImageTk.PhotoImage(peacocks_image),
    "Lemurs": ImageTk.PhotoImage(lemurs_image),
    "Mangos": ImageTk.PhotoImage(mangos_image),
    "Coconuts": ImageTk.PhotoImage(coconuts_image),
    "Bananas": ImageTk.PhotoImage(bananas_image),
    "Orange Fizz": ImageTk.PhotoImage(orangefizz_image),
    "Peanut Snack": ImageTk.PhotoImage(peanutsnack_image),
    "Summer Slush": ImageTk.PhotoImage(summerslush_image),
    "Nuts and Grapes": ImageTk.PhotoImage(nutsandgrapes_image),
    "Fruity Flip": ImageTk.PhotoImage(fruityflip_image),
    "Tropic Star": ImageTk.PhotoImage(tropicstar_image),
}

# # Set the window size and position it in the center of the screen
# window_width = 300
# window_height = 200

label0 = tk.Label(tab1, text="Market Demands Numbers")
label0.grid(row=0, column=0, columnspan=15, sticky="nsew")

label1 = tk.Label(tab1, image=assets["Wildflowers"])
label1.grid(row=1, column=0)
entry1 = tk.Entry(tab1, width=10)
entry1.grid(row=1, column=1)

label2 = tk.Label(tab1, image=assets["Corn"])
label2.grid(row=2, column=0)
entry2 = tk.Entry(tab1, width=10)
entry2.grid(row=2, column=1)

label3 = tk.Label(tab1, image=assets["Cabbage"])
label3.grid(row=3, column=0)
entry3 = tk.Entry(tab1, width=10)
entry3.grid(row=3, column=1)

label4 = tk.Label(tab1, image=assets["Wheat"])
label4.grid(row=4, column=0)
entry4 = tk.Entry(tab1, width=10)
entry4.grid(row=4, column=1)

label5 = tk.Label(tab1, image=assets["Dandelion"])
label5.grid(row=5, column=0)
entry5 = tk.Entry(tab1, width=10)
entry5.grid(row=5, column=1)

label6 = tk.Label(tab1, image=assets["Lamb's Lettuce"])
label6.grid(row=6, column=0)
entry6 = tk.Entry(tab1, width=10)
entry6.grid(row=6, column=1)

label7 = tk.Label(tab1, image=assets["Carrots"])
label7.grid(row=7, column=0)
entry7 = tk.Entry(tab1, width=10)
entry7.grid(row=7, column=1)

label8 = tk.Label(tab1, image=assets["Barley"])
label8.grid(row=8, column=0)
entry8 = tk.Entry(tab1, width=10)
entry8.grid(row=8, column=1)

label9 = tk.Label(tab1, image=assets["Daisies"])
label9.grid(row=9, column=0)
entry9 = tk.Entry(tab1, width=10)
entry9.grid(row=9, column=1)

label10 = tk.Label(tab1, image=assets["Eggs"])
label10.grid(row=1, column=2)
entry10 = tk.Entry(tab1, width=10)
entry10.grid(row=1, column=3)

label11 = tk.Label(tab1, image=assets["Pigs"])
label11.grid(row=2, column=2)
entry11 = tk.Entry(tab1, width=10)
entry11.grid(row=2, column=3)

label12 = tk.Label(tab1, image=assets["Milk"])
label12.grid(row=3, column=2)
entry12 = tk.Entry(tab1, width=10)
entry12.grid(row=3, column=3)

label13 = tk.Label(tab1, image=assets["Goat's Cheese"])
label13.grid(row=4, column=2)
entry13 = tk.Entry(tab1, width=10)
entry13.grid(row=4, column=3)

label14 = tk.Label(tab1, image=assets["Duck Feathers"])
label14.grid(row=5, column=2)
entry14 = tk.Entry(tab1, width=10)
entry14.grid(row=5, column=3)

label15 = tk.Label(tab1, image=assets["Sheep Wool"])
label15.grid(row=6, column=2)
entry15 = tk.Entry(tab1, width=10)
entry15.grid(row=6, column=3)

label16 = tk.Label(tab1, image=assets["Gray Wool"])
label16.grid(row=7, column=2)
entry16 = tk.Entry(tab1, width=10)
entry16.grid(row=7, column=3)

label17 = tk.Label(tab1, image=assets["White Wool"])
label17.grid(row=8, column=2)
entry17 = tk.Entry(tab1, width=10)
entry17.grid(row=8, column=3)

label18 = tk.Label(tab1, image=assets["Apples"])
label18.grid(row=9, column=2)
entry18 = tk.Entry(tab1, width=10)
entry18.grid(row=9, column=3)

label19 = tk.Label(tab1, image=assets["Cherries"])
label19.grid(row=1, column=4)
entry19 = tk.Entry(tab1, width=10)
entry19.grid(row=1, column=5)

label20 = tk.Label(tab1, image=assets["Almonds"])
label20.grid(row=2, column=4)
entry20 = tk.Entry(tab1, width=10)
entry20.grid(row=2, column=5)

label21 = tk.Label(tab1, image=assets["Peaches"])
label21.grid(row=3, column=4)
entry21 = tk.Entry(tab1, width=10)
entry21.grid(row=3, column=5)

label22 = tk.Label(tab1, image=assets["Lavender"])
label22.grid(row=4, column=4)
entry22 = tk.Entry(tab1, width=10)
entry22.grid(row=4, column=5)

label23 = tk.Label(tab1, image=assets["Aloe Vera"])
label23.grid(row=5, column=4)
entry23 = tk.Entry(tab1, width=10)
entry23.grid(row=5, column=5)

label24 = tk.Label(tab1, image=assets["Jasmine"])
label24.grid(row=6, column=4)
entry24 = tk.Entry(tab1, width=10)
entry24.grid(row=6, column=5)

label25 = tk.Label(tab1, image=assets["Vanilla"])
label25.grid(row=7, column=4)
entry25 = tk.Entry(tab1, width=10)
entry25.grid(row=7, column=5)

label26 = tk.Label(tab1, image=assets["Cocoa"])
label26.grid(row=8, column=4)
entry26 = tk.Entry(tab1, width=10)
entry26.grid(row=8, column=5)

label27 = tk.Label(tab1, image=assets["Olives"])
label27.grid(row=9, column=4)
entry27 = tk.Entry(tab1, width=10)
entry27.grid(row=9, column=5)

label28 = tk.Label(tab1, image=assets["Citrus Fruits"])
label28.grid(row=1, column=6)
entry28 = tk.Entry(tab1, width=10)
entry28.grid(row=1, column=7)

label29 = tk.Label(tab1, image=assets["Essence of Lavender"])
label29.grid(row=2, column=6)
entry29 = tk.Entry(tab1, width=10)
entry29.grid(row=2, column=7)

label30 = tk.Label(tab1, image=assets["Aloe Vera Gel"])
label30.grid(row=3, column=6)
entry30 = tk.Entry(tab1, width=10)
entry30.grid(row=3, column=7)

label31 = tk.Label(tab1, image=assets["Essence of Jasmine"])
label31.grid(row=4, column=6)
entry31 = tk.Entry(tab1, width=10)
entry31.grid(row=4, column=7)

label32 = tk.Label(tab1, image=assets["Vanilla Extract"])
label32.grid(row=5, column=6)
entry32 = tk.Entry(tab1, width=10)
entry32.grid(row=5, column=7)

label33 = tk.Label(tab1, image=assets["Cocoa Powder"])
label33.grid(row=6, column=6)
entry33 = tk.Entry(tab1, width=10)
entry33.grid(row=6, column=7)

label34 = tk.Label(tab1, image=assets["Olive Oil"])
label34.grid(row=7, column=6)
entry34 = tk.Entry(tab1, width=10)
entry34.grid(row=7, column=7)

label35 = tk.Label(tab1, image=assets["Citrus Oil"])
label35.grid(row=8, column=6)
entry35 = tk.Entry(tab1, width=10)
entry35.grid(row=8, column=7)

label36 = tk.Label(tab1, image=assets["Dough"])
label36.grid(row=9, column=6)
entry36 = tk.Entry(tab1, width=10)
entry36.grid(row=9, column=7)

label37 = tk.Label(tab1, image=assets["Bread"])
label37.grid(row=1, column=8)
entry37 = tk.Entry(tab1, width=10)
entry37.grid(row=1, column=9)

label38 = tk.Label(tab1, image=assets["Croissant"])
label38.grid(row=2, column=8)
entry38 = tk.Entry(tab1, width=10)
entry38.grid(row=2, column=9)

label39 = tk.Label(tab1, image=assets["Apple Strudel"])
label39.grid(row=3, column=8)
entry39 = tk.Entry(tab1, width=10)
entry39.grid(row=3, column=9)

label40 = tk.Label(tab1, image=assets["Sachertorte"])
label40.grid(row=4, column=8)
entry40 = tk.Entry(tab1, width=10)
entry40.grid(row=4, column=9)

label41 = tk.Label(tab1, image=assets["Carrot Cake"])
label41.grid(row=5, column=8)
entry41 = tk.Entry(tab1, width=10)
entry41.grid(row=5, column=9)

label42 = tk.Label(tab1, image=assets["Apple Jam"])
label42.grid(row=6, column=8)
entry42 = tk.Entry(tab1, width=10)
entry42.grid(row=6, column=9)

label43 = tk.Label(tab1, image=assets["Berry Jam"])
label43.grid(row=7, column=8)
entry43 = tk.Entry(tab1, width=10)
entry43.grid(row=7, column=9)

label44 = tk.Label(tab1, image=assets["Orange Jam"])
label44.grid(row=8, column=8)
entry44 = tk.Entry(tab1, width=10)
entry44.grid(row=8, column=9)

label45 = tk.Label(tab1, image=assets["Cherry Jam"])
label45.grid(row=9, column=8)
entry45 = tk.Entry(tab1, width=10)
entry45.grid(row=9, column=9)

label46 = tk.Label(tab1, image=assets["Peach Jam"])
label46.grid(row=1, column=10)
entry46 = tk.Entry(tab1, width=10)
entry46.grid(row=1, column=11)

label47 = tk.Label(tab1, image=assets["Butter"])
label47.grid(row=2, column=10)
entry47 = tk.Entry(tab1, width=10)
entry47.grid(row=2, column=11)

label48 = tk.Label(tab1, image=assets["Cherry Yoghurt"])
label48.grid(row=3, column=10)
entry48 = tk.Entry(tab1, width=10)
entry48.grid(row=3, column=11)

label49 = tk.Label(tab1, image=assets["Cream"])
label49.grid(row=4, column=10)
entry49 = tk.Entry(tab1, width=10)
entry49.grid(row=4, column=11)

label50 = tk.Label(tab1, image=assets["Cheese"])
label50.grid(row=5, column=10)
entry50 = tk.Entry(tab1, width=10)
entry50.grid(row=5, column=11)

label51 = tk.Label(tab1, image=assets["Forest Honey"])
label51.grid(row=6, column=10)
entry51 = tk.Entry(tab1, width=10)
entry51.grid(row=6, column=11)

label52 = tk.Label(tab1, image=assets["Flower Honey"])
label52.grid(row=7, column=10)
entry52 = tk.Entry(tab1, width=10)
entry52.grid(row=7, column=11)

label53 = tk.Label(tab1, text="Number 1")
label53.grid(row=1, column=12)
entry53 = tk.Entry(tab1, width=10)
entry53.grid(row=1, column=13)

label54 = tk.Label(tab1, text="Number 2")
label54.grid(row=2, column=12)
entry54 = tk.Entry(tab1, width=10)
entry54.grid(row=2, column=13)

label55 = tk.Label(tab1, text="Number 3")
label55.grid(row=3, column=12)
entry55 = tk.Entry(tab1, width=10)
entry55.grid(row=3, column=13)

label56 = tk.Label(tab1, text="Number 4")
label56.grid(row=4, column=12)
entry56 = tk.Entry(tab1, width=10)
entry56.grid(row=4, column=13)

label57 = tk.Label(tab1, text="Number 5")
label57.grid(row=5, column=12)
entry57 = tk.Entry(tab1, width=10)
entry57.grid(row=5, column=13)

label58 = tk.Label(tab1, text="Number 6")
label58.grid(row=6, column=12)
entry58 = tk.Entry(tab1, width=10)
entry58.grid(row=6, column=13)

label59 = tk.Label(tab1, text="Total sell price:")
label59.grid(row=12, column=0)
entry59 = tk.Entry(tab1, width=10)
entry59.grid(row=12, column=1)

label60 = tk.Label(tab1, text="Result:")
label60.grid(row=8, column=12)
res_label = tk.Label(tab1, text="")
res_label.grid(row=8, column=13)

label61 = tk.Label(tab1, text="Barnacle's Ship 299%\nBarnacle's Train 483%")
label61.grid(row=9, column=12)

def calculate_sum():
    # Get the input values from the entry widgets
    try:
        num1 = float(entry53.get())
    except ValueError:
        num1 = 0

    try:
        num2 = float(entry54.get())
    except ValueError:
        num2 = 0

    try:
        num3 = float(entry55.get())
    except ValueError:
        num3 = 0

    try:
        num4 = float(entry56.get())
    except ValueError:
        num4 = 0

    try:
        num5 = float(entry57.get())
    except ValueError:
        num5 = 0

    try:
        num6 = float(entry58.get())
    except ValueError:
        num6 = 0

    # Calculate the sum of all input values
    total = num1 + num2 + num3 + num4 + num5 + num6

    # Display the result in the result label
    res_label.config(text=str(total))

def clear():
    # Clear all the entry widgets
    entry53.delete(0, tk.END)
    entry54.delete(0, tk.END)
    entry55.delete(0, tk.END)
    entry56.delete(0, tk.END)
    entry57.delete(0, tk.END)
    entry58.delete(0, tk.END)
    res_label.config(text="")

button = tk.Button(tab1, text="Calculate", command=calculate_sum)
button.grid(row=7, column=12, columnspan=1)

button_clear = tk.Button(tab1, text="Clear", command=clear)
button_clear.grid(row=7, column=13)

def calculate():
    # Get the input values from the entry widgets
    try:
        num_wildflowers = int(entry1.get())
    except ValueError:
        num_wildflowers = 0

    try:
        num_corn = int(entry2.get())
    except ValueError:
        num_corn = 0

    try:
        num_cabbage = int(entry3.get())
    except ValueError:
        num_cabbage = 0

    try:
        num_wheat = int(entry4.get())
    except ValueError:
        num_wheat = 0

    try:
        num_dandelion = int(entry5.get())
    except ValueError:
        num_dandelion = 0

    try:
        num_lambs_lettuce = int(entry6.get())
    except ValueError:
        num_lambs_lettuce = 0

    try:
        num_carrots = int(entry7.get())
    except ValueError:
        num_carrots = 0

    try:
        num_barley = int(entry8.get())
    except ValueError:
        num_barley = 0

    try:
        num_daisies = int(entry9.get())
    except ValueError:
        num_daisies = 0

    try:
        num_eggs = float(entry10.get())
    except ValueError:
        num_eggs = 0

    try:
        num_pigs = float(entry11.get())
    except ValueError:
        num_pigs = 0

    try:
        num_milk = float(entry12.get())
    except ValueError:
        num_milk = 0

    try:
        num_goats_cheese = float(entry13.get())
    except ValueError:
        num_goats_cheese = 0

    try:
        num_duck_feathers = float(entry14.get())
    except ValueError:
        num_duck_feathers = 0

    try:
        num_sheep_wool = float(entry15.get())
    except ValueError:
        num_sheep_wool = 0

    try:
        num_gray_wool = float(entry16.get())
    except ValueError:
        num_gray_wool = 0

    try:
        num_white_wool = float(entry17.get())
    except ValueError:
        num_white_wool = 0

    try:
        num_apples = float(entry18.get())
    except ValueError:
        num_apples = 0

    try:
        num_cherries = float(entry19.get())
    except ValueError:
        num_cherries = 0

    try:
        num_almonds = float(entry20.get())
    except ValueError:
        num_almonds = 0

    try:
        num_peaches = float(entry21.get())
    except ValueError:
        num_peaches = 0

    try:
        num_lavender = float(entry22.get())
    except ValueError:
        num_lavender = 0

    try:
        num_aloe_vera = float(entry23.get())
    except ValueError:
        num_aloe_vera = 0

    try:
        num_jasmine = float(entry24.get())
    except ValueError:
        num_jasmine = 0

    try:
        num_vanilla = float(entry25.get())
    except ValueError:
        num_vanilla = 0

    try:
        num_cocoa = float(entry26.get())
    except ValueError:
        num_cocoa = 0

    try:
        num_olives = float(entry27.get())
    except ValueError:
        num_olives = 0

    try:
        num_citrus_fruits = float(entry28.get())
    except ValueError:
        num_citrus_fruits = 0

    try:
        num_essence_of_lavender = float(entry29.get())
    except ValueError:
        num_essence_of_lavender = 0

    try:
        num_aloe_vera_gel = float(entry30.get())
    except ValueError:
        num_aloe_vera_gel = 0

    try:
        num_essence_of_jasmine = float(entry31.get())
    except ValueError:
        num_essence_of_jasmine = 0

    try:
        num_vanilla_extract = float(entry32.get())
    except ValueError:
        num_vanilla_extract = 0

    try:
        num_cocoa_powder = float(entry33.get())
    except ValueError:
        num_cocoa_powder = 0

    try:
        num_olive_oil = float(entry34.get())
    except ValueError:
        num_olive_oil = 0

    try:
        num_citrus_oil = float(entry35.get())
    except ValueError:
        num_citrus_oil = 0

    try:
        num_dough = float(entry36.get())
    except ValueError:
        num_dough = 0

    try:
        num_bread = float(entry37.get())
    except ValueError:
        num_bread = 0

    try:
        num_croissant = float(entry38.get())
    except ValueError:
        num_croissant = 0

    try:
        num_apple_strudel = float(entry39.get())
    except ValueError:
        num_apple_strudel = 0

    try:
        num_sachertorte = float(entry40.get())
    except ValueError:
        num_sachertorte = 0

    try:
        num_carrot_cake = float(entry41.get())
    except ValueError:
        num_carrot_cake = 0

    try:
        num_apple_jam = float(entry42.get())
    except ValueError:
        num_apple_jam = 0

    try:
        num_berry_jam = float(entry43.get())
    except ValueError:
        num_berry_jam = 0

    try:
        num_orange_jam = float(entry44.get())
    except ValueError:
        num_orange_jam = 0

    try:
        num_cherry_jam = float(entry45.get())
    except ValueError:
        num_cherry_jam = 0

    try:
        num_peach_jam = float(entry46.get())
    except ValueError:
        num_peach_jam = 0

    try:
        num_butter = float(entry47.get())
    except ValueError:
        num_butter = 0

    try:
        num_cherry_yoghurt = float(entry48.get())
    except ValueError:
        num_cherry_yoghurt = 0

    try:
        num_cream = float(entry49.get())
    except ValueError:
        num_cream = 0

    try:
        num_cheese = float(entry50.get())
    except ValueError:
        num_cheese = 0

    try:
        num_forest_honey = float(entry51.get())
    except ValueError:
        num_forest_honey = 0

    try:
        num_flower_honey = float(entry52.get())
    except ValueError:
        num_flower_honey = 0

    try:
        total_sell_price = float(entry59.get())
    except ValueError:
        total_sell_price = 0


    # Set the price of each item
    wildflowers_price = 1
    corn_price = 5
    cabbage_price = 100
    wheat_price = 24
    dandelion_price = 6
    lambs_lettuce_price = 7
    carrots_price = 4
    barley_price = 5
    daisies_price = 5
    eggs_price = 9
    pigs_price = 4
    milk_price = 22
    goats_cheese_price = 10
    duck_feathers_price = 15
    sheep_wool_price = 7
    gray_wool_price = 6
    white_wool_price = 0
    apples_price = 24
    cherries_price = 100
    almonds_price = 60
    peaches_price = 26
    lavender_price = 3
    aloe_vera_price = 5
    jasmine_price = 30
    vanilla_price = 15
    cocoa_price = 13
    olives_price = 45
    citrus_fruits_price = 34
    essence_of_lavender_price = 10
    aloe_vera_gel_price = 16
    essence_of_jasmine_price = 77
    vanilla_extract_price = 11
    cocoa_powder_price = 27
    olive_oil_price = 51
    citrus_oil_price = 35
    dough_price = 86
    bread_price = 210
    croissant_price = 46
    apple_strudel_price = 45
    sachertorte_price = 0
    carrot_cake_price = 172
    apple_jam_price = 23
    berry_jam_price = 47
    orange_jam_price = 12
    cherry_jam_price = 152
    peach_jam_price = 0
    butter_price = 66
    cherry_yoghurt_price = 309
    cream_price = 43
    cheese_price = 123
    forest_honey_price = 0
    flower_honey_price = 0

    # Calculate the total price of all items the user has
    total_price = (num_wildflowers * wildflowers_price) + (num_corn * corn_price) + (num_cabbage * cabbage_price) + (num_wheat * wheat_price) + (num_dandelion * dandelion_price) + (num_lambs_lettuce * lambs_lettuce_price) + (num_carrots * carrots_price) + (num_barley * barley_price) + (num_daisies * daisies_price) + (num_eggs * eggs_price) + (num_pigs * pigs_price) + (num_milk * milk_price) + (num_goats_cheese * goats_cheese_price) + (num_duck_feathers * duck_feathers_price) + (num_sheep_wool * sheep_wool_price) + (num_gray_wool * gray_wool_price) + (num_white_wool * white_wool_price) + (num_apples * apples_price) + (num_cherries * cherries_price) + (num_almonds * almonds_price) + (num_peaches * peaches_price) + (num_lavender * lavender_price) + (num_aloe_vera * aloe_vera_price) + (num_jasmine * jasmine_price) + (num_vanilla * vanilla_price) + (num_cocoa * cocoa_price) + (num_olives * olives_price) + (num_citrus_fruits * citrus_fruits_price) + (num_essence_of_lavender * essence_of_lavender_price) + (num_aloe_vera_gel * aloe_vera_gel_price) + (num_essence_of_jasmine * essence_of_jasmine_price) + (num_vanilla_extract * vanilla_extract_price) + (num_cocoa_powder * cocoa_powder_price) + (num_olive_oil * olive_oil_price) + (num_citrus_oil * citrus_oil_price) + (num_dough * dough_price) + (num_bread * bread_price) + (num_croissant * croissant_price) + (num_apple_strudel * apple_strudel_price) + (num_sachertorte * sachertorte_price) + (num_carrot_cake * carrot_cake_price) + (num_apple_jam * apple_jam_price) + (num_berry_jam * berry_jam_price) + (num_orange_jam * orange_jam_price) + (num_cherry_jam * cherry_jam_price) + (num_peach_jam * peach_jam_price) + (num_butter * butter_price) + (num_cherry_yoghurt * cherry_yoghurt_price) + (num_cream * cream_price) + (num_cheese * cheese_price) + (num_forest_honey * forest_honey_price) + (num_flower_honey * flower_honey_price)

    # Calculate the percentage of the total sell price that the total price of all items represents
    percentage_market = (total_price / total_sell_price) * 100

    # Calculate the percentage of the total price that the total sell price at the barn represents
    percentage_barn = (total_sell_price / total_price) * 100

    # Compare the percentages to determine where it's better to sell
    if percentage_market < percentage_barn:
        result_label.config(text="It's better to sell at the market.\nThe percentage difference is {:.2f}% in favor of the market.".format(percentage_barn - percentage_market))
    elif percentage_market > percentage_barn:
        result_label.config(text="It's better to sell at the barn.\nThe percentage difference is {:.2f}% in favor of the barn.".format(percentage_market - percentage_barn))
    elif percentage_market == percentage_barn:
        result_label.config(text="It doesn't matter where you sell.")

def clear():
    # Clear all the entry widgets
    entry_list = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10,
                  entry11, entry12, entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20,
                  entry21, entry22, entry23, entry24, entry25, entry26, entry27, entry28, entry29, entry30,
                  entry31, entry32, entry33, entry34, entry35, entry36, entry37, entry38, entry39, entry40,
                  entry41, entry42, entry43, entry44, entry45, entry46, entry47, entry48, entry49, entry50,
                  entry51, entry52, entry59]
    for entry in entry_list:
        entry.delete(0, tk.END)
    result_label.config(text="")

button_calulate = tk.Button(tab1, text="Calculate", command=calculate)
button_calulate.grid(row=12, column=2)

button_clear = tk.Button(tab1, text="Clear", command=clear)
button_clear.grid(row=12, column=3)

result_label = tk.Label(tab1)
result_label.grid(row=13, column=0, columnspan=15)


# Another Calculator tab
label3 = tk.Label(tab2, text="Tropical Island Market")
label3.grid(row=0, column=0, columnspan=15, sticky="nsew")

# Add widgets for calculator 2 here
label61 = tk.Label(tab2, image=assets["Oranges"])
label61.grid(row=1, column=0)
entry61 = tk.Entry(tab2, width=10)
entry61.grid(row=1, column=1)

label62 = tk.Label(tab2, image=assets["Peanuts"])
label62.grid(row=2, column=0)
entry62 = tk.Entry(tab2, width=10)
entry62.grid(row=2, column=1)

label63 = tk.Label(tab2, image=assets["Grapes"])
label63.grid(row=3, column=0)
entry63 = tk.Entry(tab2, width=10)
entry63.grid(row=3, column=1)

label64 = tk.Label(tab2, image=assets["Peacocks"])
label64.grid(row=4, column=0)
entry64 = tk.Entry(tab2, width=10)
entry64.grid(row=4, column=1)

label65 = tk.Label(tab2, image=assets["Lemurs"])
label65.grid(row=5, column=0)
entry65 = tk.Entry(tab2, width=10)
entry65.grid(row=5, column=1)

label66 = tk.Label(tab2, image=assets["Mangos"])
label66.grid(row=6, column=0)
entry66 = tk.Entry(tab2, width=10)
entry66.grid(row=6, column=1)

label67 = tk.Label(tab2, image=assets["Coconuts"])
label67.grid(row=7, column=0)
entry67 = tk.Entry(tab2, width=10)
entry67.grid(row=7, column=1)

label68 = tk.Label(tab2, image=assets["Bananas"])
label68.grid(row=8, column=0)
entry68 = tk.Entry(tab2, width=10)
entry68.grid(row=8, column=1)

label69 = tk.Label(tab2, image=assets["Orange Fizz"])
label69.grid(row=1, column=2)
entry69 = tk.Entry(tab2, width=10)
entry69.grid(row=1, column=3)

label70 = tk.Label(tab2, image=assets["Peanut Snack"])
label70.grid(row=2, column=2)
entry70 = tk.Entry(tab2, width=10)
entry70.grid(row=2, column=3)

label71 = tk.Label(tab2, image=assets["Summer Slush"])
label71.grid(row=3, column=2)
entry71 = tk.Entry(tab2, width=10)
entry71.grid(row=3, column=3)

label72 = tk.Label(tab2, image=assets["Nuts and Grapes"])
label72.grid(row=4, column=2)
entry72 = tk.Entry(tab2, width=10)
entry72.grid(row=4, column=3)

label73 = tk.Label(tab2, image=assets["Fruity Flip"])
label73.grid(row=5, column=2)
entry73 = tk.Entry(tab2, width=10)
entry73.grid(row=5, column=3)

label74 = tk.Label(tab2, image=assets["Tropic Star"])
label74.grid(row=6, column=2)
entry74 = tk.Entry(tab2, width=10)
entry74.grid(row=6, column=3)

label75 = tk.Label(tab2, text="Total sell price:")
label75.grid(row=7, column=2)
entry75 = tk.Entry(tab2, width=10)
entry75.grid(row=7, column=3)

def calculate_island():
    # Get the input values from the entry widgets
    try:
        num_oranges = int(entry61.get())
    except ValueError:
        num_oranges = 0

    try:
        num_peanuts = int(entry62.get())
    except ValueError:
        num_peanuts = 0

    try:
        num_grapes = int(entry63.get())
    except ValueError:
        num_grapes = 0

    try:
        num_peacocks = int(entry64.get())
    except ValueError:
        num_peacocks = 0

    try:
        num_lemurs = int(entry65.get())
    except ValueError:
        num_lemurs = 0

    try:
        num_mangos = int(entry66.get())
    except ValueError:
        num_mangos = 0

    try:
        num_coconuts = int(entry67.get())
    except ValueError:
        num_coconuts = 0

    try:
        num_bananas = int(entry68.get())
    except ValueError:
        num_bananas = 0

    try:
        num_orange_fizz = int(entry69.get())
    except ValueError:
        num_orange_fizz = 0

    try:
        num_peanut_snack = float(entry70.get())
    except ValueError:
        num_peanut_snack = 0

    try:
        num_summer_slush = float(entry71.get())
    except ValueError:
        num_summer_slush = 0

    try:
        num_nuts_and_grapes = float(entry72.get())
    except ValueError:
        num_nuts_and_grapes = 0

    try:
        num_fruity_flip = float(entry73.get())
    except ValueError:
        num_fruity_flip = 0

    try:
        num_tropic_star = float(entry74.get())
    except ValueError:
        num_tropic_star = 0

    try:
        total_sell_price_island = float(entry75.get())
    except ValueError:
        total_sell_price_island = 0




    # Set the price of each item
    oranges_price = 4
    peanuts_price = 4
    grapes_price = 15
    peacocks_price = 8
    lemurs_price = 0
    mangos_price = 550
    coconuts_price = 400
    bananas_price = 1150
    orange_fizz_price = 200
    peanut_snack_price = 180
    summer_slush_price = 104
    nuts_and_grapes_price = 0
    fruity_flip_price = 0
    tropic_star_price = 0

    # Calculate the total price of all items the user has
    total_price_island = (num_oranges * oranges_price) + (num_peanuts * peanuts_price) + (num_grapes * grapes_price) + (num_peacocks * peacocks_price) + (num_lemurs * lemurs_price) + (num_mangos * mangos_price) + (num_coconuts * coconuts_price) + (num_bananas * bananas_price) + (num_orange_fizz * orange_fizz_price) + (num_peanut_snack * peanut_snack_price) + (num_summer_slush * summer_slush_price) + (num_nuts_and_grapes * nuts_and_grapes_price) + (num_fruity_flip * fruity_flip_price) + (num_tropic_star * tropic_star_price)

    # Calculate the percentage of the total sell price that the total price of all items represents
    percentage_island = (total_price_island / total_sell_price_island) * 100

    # Calculate the percentage of the total price that the total sell price at the barn represents
    percentage_barn = (total_sell_price_island / total_price_island) * 100

    # Compare the percentages to determine where it's better to sell
    if percentage_island < percentage_barn:
        result_label_tab2.config(text="It's better to sell at the adventure market.\nThe percentage difference is {:.2f}% in favor of the adventure market.".format(percentage_barn - percentage_island))
    elif percentage_island > percentage_barn:
        result_label_tab2.config(text="It's better to sell at the barn.\nThe percentage difference is {:.2f}% in favor of the barn.".format(percentage_island - percentage_barn))
    elif percentage_island == percentage_barn:
        result_label_tab2.config(text="It doesn't matter where you sell.")

def clear():
    # Clear all the entry widgets
    entry_list = [entry61, entry62, entry63, entry64, entry65,
                  entry66, entry67, entry68, entry69, entry70,
                  entry71, entry72, entry73, entry74, entry75]
    for entry in entry_list:
        entry.delete(0, tk.END)
    result_label.config(text="")

button_calulate = tk.Button(tab2, text="Calculate", command=calculate_island)
button_calulate.grid(row=8, column=2)

button_clear = tk.Button(tab2, text="Clear", command=clear)
button_clear.grid(row=8, column=3)

result_label_tab2 = tk.Label(tab2)
result_label_tab2.grid(row=13, column=0, columnspan=15)

root.mainloop()