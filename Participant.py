"""
Stuff
"""

class Participant:
    def __init__(self,
                 unique_id: str,
                 sort_name: str):
        self.id = unique_id
        self.name = sort_name
        
    def text(self,
             upper_txt: str,
             lower_txt: str):
        self.upper = upper_txt
        self.lower = lower_txt
        
    def encode(self, code_type):
        # create teh QR code
        if code_type == 'qr':
            print(code_type)
        else:
            print('This is just started')
