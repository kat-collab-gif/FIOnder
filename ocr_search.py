"""
Простой OCR для PDF.

Две функции:
    1. get_text(pdf_path) — возвращает текст из PDF
    2. save_to_txt(pdf_path, txt_path, with_coords=False) — сохраняет текст в файл
"""

import fitz
import pytesseract
from PIL import Image
import io


def get_text(pdf_path):
    """
    Получает текст из PDF.

    pdf_path: путь к PDF файлу

    Возвращает: список строк (по одной строке на страницу)
    """
    doc = fitz.open(pdf_path)
    all_text = []

    for page in doc:
        pix = page.get_pixmap()
        img_data = pix.tobytes('png')
        image = Image.open(io.BytesIO(img_data))

        text = pytesseract.image_to_string(image, lang='rus+eng')
        all_text.append(text)

    doc.close()
    return all_text


def save_to_txt(pdf_path, txt_path, with_coords=False):
    """
    Сохраняет текст из PDF в TXT файл.

    pdf_path: путь к PDF файлу
    txt_path: путь куда сохранить TXT
    with_coords: True — координаты, False — простой текст
    """
    doc = fitz.open(pdf_path)

    with open(txt_path, 'w', encoding='utf-8') as f:
        for page_num, page in enumerate(doc, start=1):
            pix = page.get_pixmap()
            img_data = pix.tobytes('png')
            image = Image.open(io.BytesIO(img_data))

            data = pytesseract.image_to_data(image, lang='rus+eng', output_type=pytesseract.Output.DICT)

            for i in range(len(data['text'])):
                txt = data['text'][i].strip()
                conf = float(data['conf'][i])
                if not txt or conf < 40:
                    continue

                if with_coords:
                    f.write(f"{page_num}|{txt}|{data['left'][i]}|{data['top'][i]}|{data['width'][i]}|{data['height'][i]}|{conf:.1f}\n")
                else:
                    f.write(txt + ' ')

    doc.close()
