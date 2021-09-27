"""Create scannable code images

Packages: sys, os, pandas, qrcode, PIL, datetime

"""

__authors__ = "Andrew Korinda"
__copyright__ = "Copyright 2021, Midland Moutain Bike Crew"
__credits__ = ["Andrew Korinda"]
__license__ = "GPL-3.0-or-later"
__version__ = "0.1"
__maintainer__ = "https://github.com/akorinda/MiSCA-ID-Sticker-Generator"
__status__ = "Prototype"


# Imports
import sys
import os
import pandas
import qrcode
from PIL import Image, ImageDraw, ImageFont
from datetime import date


# Constants

def qr_create(txt_data):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=40,
        border=7
    )

    qr.add_data(txt_data)
    qr.make(fit=True)

    qr_img = qr.make_image(
        fill='black',
        back_color='white'
    )

    return qr_img


def frame_create(group):
    frame_img = Image.new(
        'RGB',
        (2100, 2611),
        color=group
    )

    # img = Image.open('Black-Soil_Tall.jpg', mode='r')
    frame_img = frame_img.resize((2000, 2511))

    border_img = Image.new(
        'RGB',
        (2100, 2611),
        color='white'
    )

    border_img.paste(
        frame_img,
        (50,
         50),
        mask=None
    )

    return border_img


def set_font(default_font_size):
    default_font = ImageFont.truetype(
        font='arialbd.ttf',
        size=default_font_size
    )

    return default_font


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prepare
    # % Layers
    layer_frame = frame_create('white')
    # layer_logo = layer_logo.resize((399, 399))

    # % Dimensions
    frame_w, frame_h = layer_frame.size

    # Rider loops
    try:
        riders = pandas.read_excel('Rider-List_Update.xlsx')
    except PermissionError:
        print('Rider-List.xlsx is not accessible. Likely in use by another application.')
        sys.exit(1)

    qrPath = 'QR-Export/' + date.today().strftime('%Y-%m-%d')
    if not os.path.exists(qrPath):
        os.makedirs(qrPath)

    for x in range(riders['RegistrantId'].size):
        if riders['Role'][x] == 'Rider':
            rider_code = str(int(riders['RegistrantId'][x]))  # + '\t' + \
                        # riders['Firstname'][x] + '\t' + riders['Lastname'][x]
            rider_file =riders['Lastname'][x].title() + ' ' + riders['Firstname'][x].title()
            rider_name = riders['Firstname'][x].title() + '\n' + riders['Lastname'][x].title()
            rider_group = 'white'

            # Resize QR and logo per border definition
            layer_qr = qr_create('')
            layer_logo = Image.open('MMBC-Tire_2020.jpg', mode='r')
            logo_dim = round((0.07 * layer_qr.size[0] * layer_qr.size[1]) ** 0.5)
            layer_logo = layer_logo.resize((logo_dim, logo_dim))

            # % Dimensions
            logo_w, logo_h = layer_logo.size
            qr_w, qr_h = layer_qr.size
            qr_buffer = round((frame_w - qr_w) / 2)

            # Create layers
            layer_qr = qr_create(rider_code)
            layer_frame = frame_create(rider_group)

            # Stack layers
            rider_qr = layer_frame
            rider_qr.paste(
                layer_qr,
                (qr_buffer,
                 qr_buffer),
                mask=None
            )
            rider_qr.paste(
                layer_logo,
                (round((frame_w - logo_w) / 2),
                 round((qr_h - logo_h) / 2) + qr_buffer),
                mask=None
            )

            # Add rider name text
            start_size = 240
            font_size = start_size
            font = set_font(font_size)

            if len(riders['Firstname'][x]) > len(riders['Lastname'][x]):
                name_limit = riders['Firstname'][x]
            else:
                name_limit = riders['Lastname'][x]

            # Make sure the name fits
            while True:
                font_size = font_size - 20
                font = set_font(font_size)
                text_vert_pos = frame_h / 2 + qr_h / 2 - qr_buffer / 2 # was + qr_buffer

                if (font.getsize(name_limit)[0] < qr_w) or (font.size <= 0): break

            name_color = 'black'

            rider_label = ImageDraw.Draw(rider_qr)
            rider_label.text(
                (round(frame_w / 2),
                 text_vert_pos),
                rider_name,
                fill=name_color,
                anchor='mm',
                align='center',
                font=font
            )

            # Outputs
            rider_qr = rider_qr.resize((300, 373))
            rider_qr.save(qrPath + '/' + rider_file + '.png')

# rider_qr.show()
