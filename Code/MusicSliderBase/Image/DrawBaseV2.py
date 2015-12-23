#-------------------------------------------------------------------------------
# Name:        DrawBase
# Purpose:     To draw the image of the base for other music sliders
#              in 20 lines of codes by using Python Image Library
#
#              For unknown reasons, cannot use the TrueFont correctly
#              Alternatively, the bitmap font was used
#              based on halfinterval width = 19px
#
#              This program was written in portable python 2.7.3 (PIL included)
#
# Author:      Tatiana Simo, Luofeng Xu
#
# Created:     17/05/2013
# Copyright:
# Licence:
#-------------------------------------------------------------------------------

import os, sys
import Image
import ImageDraw
import ImageFont

def drawBaseImage(outputFileName):

    # Line 1: bitmap font character width 11pt, height 20pt
    font = ImageFont.load("courB14.pil")

    # Line 2: list of tuples (note,  left border position)
    #    the calculations are based on halfinterval width = 19px
    zp = [ ('C', 124), ('D', 181), ('E', 238), ('F', 276), ('G', 333),
           ('A', 390), ('B', 447), ('C', 485), ('D', 542), ('E', 599),
           ('F', 637), ('G', 694), ('A', 751), ('B', 808), ('C', 846) ]

    # Line 3: create Image
    img = Image.new("RGB", (884, 241), "olive")

    # Line 4: create 2D drawing interface
    draw = ImageDraw.Draw(img)

    # Line 5: draw Augumented frame rectangle
    draw.rectangle((-1, 0, 884, 32), outline="black", fill="khaki")

    # Line 6: draw FORM frame rectangle
    draw.rectangle((-1, 32, 884, 76), outline="black", fill="peru")

    # Line 7: draw rectangle border for character (its size always 19 * 2)
    #[draw.rectangle((x, 32, x + 38, 64), outline="black") for ch, x in zp]

    # 8  draw halfintervals
    #[draw.rectangle((124 + i * 19, 64, 124 + (i + 1) * 19, 76), outline="black") for i in range(45)]

    # 9  line that divides titles (FRAME, Argumented) from notes
    #draw.line((124, 0, 124, 76), "black")

    # 10  crop the top part
    #img_top = img.crop((0, 0, 884, 77))

    # 11  flip it
    #img_bottom = img_top.transpose(Image.FLIP_TOP_BOTTOM)

    # 12  insert at the bottom
    #img.paste(img_bottom, (0, 164))

    #13  build an array of frames, each element is a tuple
    #    (title, y-axis shift, x-axis shift for character, list of chars to draw)
    #    x-axis shift calculated based on the font size
    arr = [
        ("Diminished", 210, -5, 'b', zp[1:]),
        ("Augumented", 10, 33, '#', zp[:-1]),
        ("   FORM", 38, 14, '', zp),
        ("   FORM", 178, 14, '', zp)
    ]

    # 14   draw title
    #[draw.text((4, el[1]), el[0], fill="black", font=font) for el in arr]

    # 15   draw note character
    #[draw.text((x + el[2], el[1]), c, fill="black", font=font) for el in arr for c, x in el[4]]

    # 16   draw 'b's or '#'s - shift them 12 px from main character
    #[draw.text((x + el[2] + 12, el[1]), el[3], fill="black") for el in arr for c, x in el[4]]

    # 17 save image
    img.save(outputFileName + ".png", "PNG")


    """
    size = (1024, 768)
    chromaticScale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F',
                      'G', 'A', 'B', 'C']
    base = Image.new("RGB", size, (85, 107, 47))
    draw = ImageDraw.Draw(base)
#    width, height = base.size
    draw.line(((0, base.size[1]*1/9), (base.size[0], base.size[1]*1/9)), fill = 'black')
    draw.line(((0, base.size[1]*2/9), (base.size[0], base.size[1]*2/9)), fill = 'black')
    draw.line(((0, base.size[1]*3/9), (base.size[0], base.size[1]*3/9)), fill = 'black')

    draw.line(((base.size[0]/46*6, base.size[1]*3/9 - base.size[1]/9/3), (base.size[0], base.size[1]*3/9 - base.size[1]/9/3)), fill = 'black')
    draw.line(((base.size[0]/46*6, base.size[1]*6/9 + base.size[1]/9/3), (base.size[0], base.size[1]*6/9 + base.size[1]/9/3)), fill = 'black')

#    draw.text((0, base.size[1]*1/9), 'augmented', font = ImageFont.truetype('cour.ttf', 16))
    draw.line(((0, base.size[1]*6/9), (base.size[0], base.size[1]*6/9)), fill = 'black')
    draw.line(((0, base.size[1]*7/9), (base.size[0], base.size[1]*7/9)), fill = 'black')
    draw.line(((0, base.size[1]*8/9), (base.size[0], base.size[1]*8/9)), fill = 'black')

    for (position1, position2) in {(base.size[0]/46*6, base.size[1]*1/9):(base.size[0]/46*6, base.size[1]*3/9),
                                   (base.size[0]/46*7, base.size[1]/9*3 - base.size[1]/9/3):(base.size[0]/46*7, base.size[1]/9*3)}.items():
        draw.line((position1, position2), fill = 'black')
        draw.line(((position1[0], position1[1] + base.size[1]/9*3 + position2[1] - position1[1]), (position2[0], position2[1] + base.size[1]/9*3 + position2[1] - position1[1])), fill = 'black')

    base.save(sys.argv[1])
    """

if __name__ == '__main__':
    drawBaseImage("musicBase")


