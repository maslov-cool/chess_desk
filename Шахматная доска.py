from PIL import Image, ImageDraw


def board(num, size):
    size_x, size_y = size * num, size * num
    new_color = (34, 45, 0)
    newImage = Image.new("RGB", (size_x, size_y), 'white')
    draw = ImageDraw.Draw(newImage)
    for i in range(num):
        for j in range(num):
            if (not i % 2 and j % 2) or (i % 2 and not j % 2):
                draw.rectangle((j * size, i * size, j * size + size, i * size + size), (255, 255, 255))
            else:
                draw.rectangle((j * size, i * size, j * size + size, i * size + size), (0, 0, 0))
    newImage.save('res.png')


board(8, 50)

