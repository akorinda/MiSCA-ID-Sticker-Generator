"""Create scannable code images

Packages: sys, os, pandas, qrcode, PIL, datetime, tkinter

"""

__authors__ = "Andrew Korinda"
__copyright__ = "Copyright 2021, Midland Mountain Bike Crew"
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
from tkinter import filedialog


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


def handle_logo(int_path, base_img):
    logo_file = filedialog.askopenfilename(
        title='Open Center Logo',
        filetypes=[("Image file", "*.jpg *.jpeg *.png")],
        initialdir=int_path
    )

    try:
        logo_img = Image.open(logo_file, mode='r')
        logo_dim = round((0.07 * base_img.size[0] * base_img.size[1]) ** 0.5)
        logo_img = logo_img.resize((logo_dim, logo_dim))
    except AttributeError:
        logo_n = 1
        logo_img = Image.new('RGB', (logo_n, logo_n))

    return logo_img


def data_file(def_title):
    selected_file = filedialog.askopenfilename(
        title=def_title,
        filetypes=[("Excel file", "*.xlsx *.xls")]
    )

    # Rider loops
    try:
        data_rows = pandas.read_excel(selected_file)  # 'Rider-List_Update.xlsx')
    except PermissionError:
        print(os.path.basename(selected_file) + ' is not accessible. Likely in use by another application.')
        sys.exit(1)
    except AssertionError:
        print('No rider list was selected. Exiting')
        sys.exit(0)

    return selected_file, data_rows


def temp_img_path(int_path):
    try:
        img_path = filedialog.askdirectory(
            title='QR Images Save Location',
            initialdir=int_path
        )

        if img_path == '':
            print('No output path was selected. Exiting')
            sys.exit(0)
    except FileNotFoundError:
        print('The system cannot find the path specified. Exiting')
        sys.exit(0)
    if not os.path.exists(img_path):
        try:
            os.makedirs(img_path)
        except PermissionError:
            print(img_path + ' is not accessible.')
            sys.exit(1)
        except AssertionError:
            print('No output path was selected. Exiting')
            sys.exit(0)
        except FileNotFoundError:
            print('The system cannot find the path specified. Exiting')
            sys.exit(0)

    return img_path


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prepare
    # % Layers
    layer_frame = frame_create('white')
    # layer_logo = layer_logo.resize((399, 399))

    # % Dimensions
    frame_w, frame_h = layer_frame.size

    # ToDo: resolved error in PIL Image when from tkinter import * and Tk() is used
    # root = Tk()  # pointing root to Tk() to use it as Tk() in program.
    # root.withdraw()  # Hides small tkinter window.
    # root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.

    # Ask for xlsx rider list
    rider_file, riders = data_file('Open Rider List')

    # Select where image files get saved
    qrPath = temp_img_path(os.path.dirname(rider_file))

    # Resize QR and logo per border definition
    layer_qr = qr_create('')
    layer_logo = handle_logo(os.path.dirname(rider_file), layer_qr)
    # % Dimensions
    logo_w, logo_h = layer_logo.size
    qr_w, qr_h = layer_qr.size
    qr_buffer = round((frame_w - qr_w) / 2)

    # ToDo: make range of riders selectable
    for x in range(riders['RegistrantId'].size):
        if riders['Role'][x] == 'Rider':
            # ToDo: make data fields selectable
            rider_code = str(int(riders['RegistrantId'][x]))  # + '\t' + \
                        # riders['Firstname'][x] + '\t' + riders['Lastname'][x]
            rider_file = riders['Lastname'][x].title() + ' ' + riders['Firstname'][x].title()
            rider_name = riders['Firstname'][x].title() + '\n' + riders['Lastname'][x].title()
            rider_group = 'white'

            # ToDo: make the code type selectable

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
                text_vert_pos = frame_h / 2 + qr_h / 2 - qr_buffer / 2  # was + qr_buffer

                if (font.getsize(name_limit)[0] < qr_w) or (font.size <= 0):
                    break

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
