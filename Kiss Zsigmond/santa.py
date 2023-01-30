# define list of children
children = ["Timmy", "Sally", "Billy", "Sue"]

# define list of presents
presents = ["toy train", "doll", "book", "puzzle"]

# initialize Santa's starting location
current_location = "North Pole"

# initialize list of visited houses
visited_houses = []


# define function to move Santa to a new location
def move_santa(new_location):
    global current_location
    current_location = new_location


# define function to deliver presents to a child
def deliver_presents(child):
    global presents

    # check if Santa has any presents left
    if len(presents) == 0:
        print("Oh no! Santa has run out of presents!")
    else:
        # deliver a present to the child
        present = presents.pop(0)
        print("Santa delivers a " + present + " to " + child + ".")


# define function to visit a house
def visit_house(child):
    global visited_houses

    # add house to visited houses list
    visited_houses.append(child)

    # deliver presents to child
    deliver_presents(child)


# main game loop
while len(visited_houses) < len(children):
    # print current location
    print("Santa is currently at the " + current_location + ".")

    # get user input for next location
    next_location = input("Where would you like to go next? ")

    # move Santa to the next location
    move_santa(next_location)

    # check if Santa is at a house with a child
    if next_location in children:
        # visit the house and deliver presents to the child
        visit_house(next_location)

# print final message
print("Santa has visited all the houses and delivered all the presents!")