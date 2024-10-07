from PIL import Image, ImageDraw, ImageFont
import math
import random
import sys

def render_char_to_grid(char, font, size=8):
    img = Image.new('1', (size, size), 0)  # Binary image (black and white)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), char, font=font, fill=1)

    return [[img.getpixel((x, y)) for x in range(size)] for y in range(size)]

def create_message_grid(message, font, grid_width, grid_height):
    char_grids = [render_char_to_grid(char, font) for char in message]

    while len(char_grids) < grid_width * grid_height:
        char_grids.append(render_char_to_grid(' ', font))

    full_grid = [[0 for _ in range(grid_width * 8)] for _ in range(grid_height * 8)]

    for i, char_grid in enumerate(char_grids):
        row = (i // grid_width) * 8
        col = (i % grid_width) * 8
        for y in range(8):
            for x in range(8):
                full_grid[row + y][col + x] = char_grid[y][x]
    print(full_grid)
    return full_grid

def create_bmp_from_grid(grid, output_filename):
    height = len(grid)
    width = len(grid[0]) // 3 * 3

    img = Image.new('RGB', (width // 3, height), "black")
    pixels = img.load()

    for y in range(height):
        for x in range(0, width, 3):
            r = random.randint(100, 110) if grid[y][x] else random.randint(0,99)
            g = random.randint(100, 110) if grid[y][x+1] else random.randint(0,99)
            b = random.randint(100, 110) if grid[y][x+2] else random.randint(0,99)
            pixels[x // 3, y] = (b, g, r)

    img.save(output_filename, 'BMP')

def encode_message_to_bmp(message, output_filename):
    font = ImageFont.truetype("PressStart2P-Regular.ttf", 8)

    message_length = len(message)
    grid_width = math.ceil(math.sqrt(message_length))
    grid_height = math.ceil(message_length / grid_width)

    if grid_width % 3 != 0:
        grid_width += 3 - (grid_width % 3)

    message_grid = create_message_grid(message, font, grid_width, grid_height)

    create_bmp_from_grid(message_grid, output_filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py \"image.bmp\"")
        sys.exit(1)

    message = sys.argv[1]
    i = Image.open(message)
    _r = list(i.getdata())
    grid = []
    for y in range(i.height):
        grid.append([])
        for x in range(0, i.width):
            print(_r[x])
            b = 1 if _r[x+(y*i.width)][0] >= 100 else 0
            g = 1 if _r[x+(y*i.width)][1] >= 100 else 0
            r = 1 if _r[x+(y*i.width)][2] >= 100 else 0
            grid[y].append(r)
            grid[y].append(g)
            grid[y].append(b)
    print(grid)
    img = Image.new('1', (len(grid[0]), len(grid)), 0)
    pixels = img.load()

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            img.putpixel((x, y), grid[y][x])

    img.save(f"getowned{random.randint(100, 10000000)}.bmp", 'BMP')