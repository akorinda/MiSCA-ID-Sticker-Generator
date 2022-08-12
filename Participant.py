"""
Stuff
"""
from dataclasses import dataclass, field

@dataclass(order=True)
class Participant:
    sort_index: list = field(init=False, repr=False)
    id: str
    upper_txt: str = None
    lower_txt: str = None

    def __post_init__(self):
        self.sort_index = [self.lower_txt, self.upper_txt]
        # Another option: sorted(employees, key=operator.attrgetter("age", "name"))
        # Reference: https://alysivji.github.io/python-sorting-multiple-attributes.html
        
    def text(self, *,
             upper_txt: str,
             lower_txt: str):
        self.upper_txt = upper_txt
        self.lower_txt = lower_txt
        
    def encode(self, code_type):
        # create teh QR code
        if code_type == 'qr':
            print(code_type)
        else:
            print('This is just started')


if __name__ == '__main__':
    x = Participant('2345235trw')
