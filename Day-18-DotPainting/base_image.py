import colorgram

colors1 = colorgram.extract('Wet Dog and Husband.jpg', 20)

rgb_colors1 = []
for color in colors1:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_colors1 = (r, g, b)
    rgb_colors1.append(new_colors1)

print(rgb_colors1)
