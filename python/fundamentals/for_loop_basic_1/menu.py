"""
Module to print a cmd line menu of a given list of items and return the index of the selected item
"""
class FuncObj:
    """
    The only purpose of this is so str() can be called on functions
    so they can be used in RunMenu()
    """
    def __init__(self, func):
        self.func = func

    def __str__(self) -> str:
        return self.func.__name__;


def PrintMenu(header_string, objects: list):
    """
    Takes in a header_string and a list of objects and prints out a menu. 
    Menu will grow to the largest string provided between the header_string and all of the 
    object strings while keeping the header string centered.
    Does not handle multi-line strings.

    :param header_string: Can be menu title or description or anything really
    :param objects: Assumes a list is provided. Realies on str() method to get
                    the string to print to the menu.
    """
    # Create final header string
    header_string = f"* {header_string} *"

    # ctrl-c to exit string
    exit_string = f"* [Ctrl-C] Exit *"

    # Create a list of all final strings AND 
    # calculate max width including final header string
    max_width = len(header_string) if len(header_string) > len(exit_string) else len(exit_string)
    menu_strings = []
    for i,o in enumerate(objects):
        string_rep = f"* [{str(i + 1)}] {str(o)} *"
        menu_strings.append(string_rep)
        if len(string_rep) > max_width:
            max_width = len(string_rep)
    
    final_strings = []

    # add wall on top
    wall = '*' * max_width + '\n'
    final_strings.append(wall)

    # Add space to left and right of final header string
    # to center it if header string is not the max width
    # item
    total_spaces_to_add = max_width - len(header_string)
    front_spaces_to_add = total_spaces_to_add // 2
    back_spaces_to_add = total_spaces_to_add - front_spaces_to_add
    header_string = f"* {' ' * front_spaces_to_add}{header_string[2:-2]}{' ' * back_spaces_to_add} *\n"
    final_strings.append(header_string)

    # add wall below header
    final_strings.append(wall)

    # add spaces to any string to make them
    # equal to the max width string
    for s in menu_strings:
        spaces_to_add = max_width - len(s)
        s = f"{s[:-2]}{' ' * spaces_to_add} *\n"
        final_strings.append(s)

    spaces_to_add = max_width - len(exit_string)
    exit_string = f"{exit_string[:-2]}{' ' * spaces_to_add} *\n"
    final_strings.append(exit_string)
    
    # add final wall
    final_strings.append(wall)

    print(''.join(final_strings))

def RunMenu(menu_header, menu_items):
    """
    Prints a menu and waits for input get item selection from command line.
    Menu items are numbered [1, len(menu_items)].
    All input other than these numbers are rejected. 
    Ctrl-C quits.

    :param menu_header: header string to be passed to PrintMenu()
    :param menu_items: list of objects to be passed to PrintMenu()
    :return: Returns an index based on where the item is located in the 
             menu_items list. Simply returns one less than the item number
             that is printed on the screen.
    """
    while True:
        PrintMenu(menu_header, menu_items)
        print("> ", end='')
        i = input()
        try:
            index = int(i)
            if index < 1 or index > len(menu_items):
                raise ValueError
            else:
                return index - 1
        except ValueError:
            print("\nNot an option. Try again")
            continue

class Test:
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    stuff = [Test(), "Thing 2", "Thing 3", "Thing with a reallllllllllllllllly loooooooooooooooooooong NAaaaaaaaaaaaaaaammmme"]
    RunMenu("Menu of \nstuffstuffstuff\n", stuff)
