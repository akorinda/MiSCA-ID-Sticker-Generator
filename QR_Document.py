from dataclasses import dataclass
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_TAB_ALIGNMENT, WD_LINE_SPACING

@dataclass
class QRDocument:
    file: str
    size: str = '8.5x11'
    avery_template: int = 94103
