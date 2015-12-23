import os
import sys
import itertools
from PIL import Image, ImageDraw, ImageFont


def draw_slider(outputFileName, chord_or_scale, *combination):

    font = ImageFont.load("courB14.pil")  # LINE 23

    notes = [('C', 129), ('#', 147), ('b', 164), ('D', 181), ('#', 198),
             ('b', 215), ('E', 233), ('#', 250), ('b', 250), ('F', 267),
             ('#', 284), ('b', 301), ('G', 319), ('#', 336), ('b', 353),
             ('A', 370), ('#', 387), ('b', 405), ('B', 422), ('#', 439),
             ('b', 439), ('C', 456), ('#', 473)]

    def build_pattern():
        global i
        temp = [0, 22]  # LINE 22
        i = 0  # LINE 21
        [(insert_tone(c), temp.insert(len(temp)-1, i))for c in combination]
        # LINE 20
        print(temp)
        img = Image.new("RGB", (474, 76), "peru")  # Line 1
        draw = ImageDraw.Draw(img)  # Line 2
        [(draw.rectangle((i, 0, 473, 75), outline="black"), draw.rectangle((
            112, 0, 473, 20), outline="black")) for i in
         range(0, 113, 112)]  # Line 3

        [(draw.text((4, 25), outputFileName, fill="black", font=font),
         draw_pattern(temp, img, draw), img.save("images\\" + chord_or_scale +
                                                 "\\" +
                                                 outputFileName.replace(
                                                     '\n', '') +
                                                 ".png", "PNG")) for i in
         range(0, 1)]  # Line 4

    def draw_pattern(the_dict, img, draw):
        [(draw.rectangle((112, 0, notes[x][1], 20), outline="black"),
         draw.text((notes[x][1]-4, 29), str(i+1), fill="black", font=font))
         for i, x in enumerate(the_dict) if i < len(the_dict)-1]
        #  Line 5

        [draw.rectangle((notes[the_dict[i-1]][1], 0, notes[x][1], 10),
                        outline="black") for i, x in enumerate(the_dict)
         if x - 2 == the_dict[i-1] or ((i >= 1) and (notes[(the_dict[(
            i-1)])+1][1] == notes[the_dict[i]-1][1]))]  # Line 6

        [draw.text((notes[x][1]+6, 29), notes[x][0], fill="black") for i,
         x in enumerate(the_dict) if notes[x][0] == "#" or notes[x][0] ==
         "b"]  # Line 7
        img_top = img.crop((112, 0, 474, 21))  # Line 8
        img_bottom = img_top.transpose(Image.FLIP_TOP_BOTTOM)  # Line 9
        img.paste(img_bottom, (112, 55))  # Line 10

    def insert_tone(c):
        global i
        for el in c:  # LINE 11
            if el.lower() == "w":   # LINE 12
                if i + 3 == 8 or i + 3 == 20:
                    i += 4   # LINE 13
                else:
                    i += 3   # LINE 14
            elif el.lower() == "s":   # LINE 15
                if i >= 6 and i <= 8:
                    i = 9   # LINE 16
                elif i >= 18 and i <= 20:
                    i = 21   # LINE 17
                else: 
                    i += 2   # LINE 18

    build_pattern()  # 19

if __name__ == '__main__':
    draw_slider("Major", "scales", "W", "W", "S", "W", "W", "W", "S")
    draw_slider("Minor", "scales", "W", "S", "W", "W", "S", "W", "W")
    draw_slider("Harmonic", "scales", "W", "S", "W", "W", "S", "SS", "S")
    draw_slider("Ascending\nMelodic", "scales", "W", "S", "W", "W", "W",
                "W", "S")
    draw_slider("Descending\nMelodic", "scales", "W", "S", "W", "W", "S","W",
                "W")

    draw_slider("Major", "chords", "WW", "SW", "WWS")
    draw_slider("Minor", "chords", "WS", "WW", "WWS")
    draw_slider("Dom7", "chords", "WW", "SW", "WS", "W")
    draw_slider("Augmented", "chords", "WW", "WSS", "WWS")
    draw_slider("Diminish", "chords", "WS", "WS", "SS", "WW")
