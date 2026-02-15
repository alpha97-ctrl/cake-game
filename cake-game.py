cake_1 = input("Pick the color of your 1st cake: ")

cake_2 = input("Pick the color of your 2nd cake: ")

cake_3 = input("Pick the color of your 3rd cake: ")

color_selection = {"BLUE", "RED", "GREEN", "BROWN"}

if cake_1 or cake_2 or cake_3 not in color_selection:
    print("Sorry, we don't have that color.")
    print("Please pick either blue, red, green or brown!") #and/or
else:
    print("What a nice combination of cake colors!")

