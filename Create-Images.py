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


def add_to_info_list(current_list, available_list, add_index:int):
    add_item = available_list[add_index]
    current_list.append(add_item)
        
    return current_list


# Run the program
if __name__ == '__main__':
    print("\n----------- Welcome to Making QR Code Rider Sheets -----------")
    print("- 'X' to return not implemented")
    print("- 'H' for help text not implemented")
    print("- 'Q' to quit the program not implemented")
    print("\nThe order of operations is not yet configurable.\nIt is:")
    print("1) Select the rider data file")
    print("3) ***Selection of worksheet not implemented")
    print("4) Select a temperary folder of the produced images")
    print("5) Select the columns which will be part of the qr code or barcode")
    print("6) ***Filters to be implemented***")
    print("7) ***Selection of qr code or barcode not implemented***")
    print("8) Images are created")
    print("9) Execute the create-document.py script")
    
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
    print("\n\nProvide the file with the rider list. An Excel formant, *.xls or *.xlsx is expected")
    rider_file, riders = data_file('Open Rider List')
    print(f"Using {os.path.basename(rider_file)} for rider information")

    # Select where image files get saved
    print("\nProvide a folder where QR images can be temporarily stored")
    qrPath = temp_img_path(os.path.dirname(rider_file))
    print(f"Using {qrPath} as the temporary image folder")

    # Resize QR and logo per border definition
    layer_qr = qr_create('')
    print("\nAskingif logo desired not implemented")
    layer_logo = handle_logo(os.path.dirname(rider_file), layer_qr)
    # % Dimensions
    logo_w, logo_h = layer_logo.size
    qr_w, qr_h = layer_qr.size
    qr_buffer = round((frame_w - qr_w) / 2)
    
    print("\nWhat information should be in the QR code, in order?")
    rider_info = []
    iList_size = 9
    xStart = 0
    continue_selection:bool = True
    delim = '\t'
    while continue_selection:
        print(f"\nCurrent information: {delim.join(rider_info)}")
        print("Next item to include:")
        iList = 1
        dList = []
        
        for x in range(xStart, min(xStart + iList_size, riders.columns.size)):
            print(f"     {iList}. {riders.columns[x]}")
            iList += 1
            dList.append(riders.columns[x])
        print("     0. Show more columns [More]")
        print("     99. Done with selections [Done]")
        print("     ~. Remove last selection [Backspace]")
        print("     *. [Clear list]")
        
        info_selection = input("Choice (1:9): ")
        if info_selection.lower() == 'q':
            print('\n\nThe user choose to quit the program')
            sys.exit()
        elif info_selection.lower() == "more" or info_selection == '0':
            xStart += iList_size
            if xStart > riders.columns.size: xStart = 0
        elif info_selection.lower() == 'done' or info_selection == '99':
            if len(rider_info) > 0:
                continue_selection = False
            else:
                print('\nAt least one selection must be made, currently there are none.')
        elif info_selection.lower() == 'clear list' or info_selection == '*':
            rider_info = []
            xStart = 0
        elif info_selection.lower() == 'backspace' or info_selection =='*':
            if len(rider_info) > 0:
                rider_info.pop()
        elif info_selection.lower() in map(lambda x:x.lower(), dList):
            info_selection = [var.lower() for var in dList].index(info_selection)
            rider_info = add_to_info_list(rider_info, 
                                          dList,
                                          info_selection)
        elif info_selection in map(str, range(1,iList_size + 1)):
            rider_info = add_to_info_list(rider_info, 
                                          dList, 
                                          int(info_selection) - 1)
        else:
            print("\n!!!!! Selection was not recognized !!!!!")
            print("Options available at this are:")
            print("Number without period or column name")
            print("0 or More")
            print("99 or Done")
            print("~ or Backspace")
            print("* or Clear list")
    
    
    # ToDo: make range of riders selectable
    for x in range(len(riders)):
        if riders['Role'][x] == 'Rider': #Filters
            # ToDo: make data fields selectable
            rider_code = delim.join([str(var) for var in rider_info])
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
