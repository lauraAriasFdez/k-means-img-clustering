import random

# A variable defining "black" as a computer color.
# This is used in load when making an empty list-of-lists for loading data into.
# You probably don't need this, but what do I know?
BLACK = (0, 0, 0)


def read_ppm(filename):
    """
    Reads an image saved in ppm format (specifically, "plain" ppm format P3)
    :param filename: the name of the ppm file to load
    :return: a list-of-lists representing the image. The list-of-lists will be width x height, and each element will be
             a 3-tuple representing the color of the image as a red / green / blue value.
    """
    f = open(filename, "r")
    file = f.read().split()
    f.close()

    if file[0] != "P3":
        print("[ERROR] First line is not P3. File is probably not formatted correctly!")
    width = int(file[1])
    height = int(file[2])
    if file[3] != "255":
        print("[ERROR] ppm image uses a different color representation (not 255) than this code is designed for")

    image_dat = file[4:]

    image = []
    for columnNum in range(width):
        row = [BLACK] * height
        image.append(row)
    # a width x height list of lists (that is a width long list, each element of which is a height lon lists) of colors
    i = 0
    for row_num in range(height):
        for col_num in range(width):
            image[col_num][row_num] = (int(image_dat[i]), int(image_dat[i + 1]), int(image_dat[i + 2]))
            i += 3
    return image


def get_width_height(image):
    """ Returns a tuple (width, height) indicating the width and height of the image."""
    width = len(image)
    height = len(image[0])
    return width, height


def random_color():
    """Returns a random color as a 3-tuple representing the red, green, and blue values.
       Each color component will be between 0 and 255"""
    return (random.randrange(256), random.randrange(256), random.randrange(256))


def save_ppm(filename, image):
    """
    Writes an image in ppm format (specifically "plain" ppm format P3)
    :param filename: The filename to save to
    :param image: The image data, should be a width x height list-of-lists with each element
                being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
    :return: Nothing.
    """
    # Provided, open the file and write the first few lines, as these are required
    # Note, the syntax for writing to a file is a little different than print.
    out_file = open(filename, "w")
    print("P3", file=out_file)

    width, height = get_width_height(image)
    print(width, height, file=out_file)
    print(255, file=out_file)

    # From here, you need to write the image data.
    # To write one pixel you simply need to output the red, green, and blue components
    # in order with whitespace separating them. I would also recommend putting a newline after each pixed.
    # you need to output the image row-by-row, so all of the first row, then all of teh second etc.
    for row in range (len(image[0])):
        for column in range (len(image)):
            r,g,b = image [column] [row]
            print (r,g,b, file=out_file)

    # Provided - gotta close the file, skipping this is bad ok?
    out_file.close()
