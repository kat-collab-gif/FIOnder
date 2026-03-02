"""
Пример: Сохранить текст из PDF в TXT файл + поиск и подсветка слов
"""

import os
import time

from ocr_search import extract_words_with_coords, process_pdf
from search import find_and_highlight

# === НАСТРОЙКИ ===
FILE_INPUT = "CROC"  # Без расширения .pdf
SEARCH_TERMS = "Денис, Сабина, Сертификат"  # Искомые слова через запятую
# =================

start = time.time()
ts = int(start)

os.makedirs("output", exist_ok=True)
output_txt = f"output/{FILE_INPUT}Output{ts}.txt"
output_pdf = f"output/{FILE_INPUT}Highlighted{ts}.pdf"

print(f"Обработка {FILE_INPUT}.pdf...")

# 1. Извлекаем текст (OCR + фильтрация)
result = process_pdf(f"{FILE_INPUT}.pdf")

# Сохраняем текст в файл
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\nТекст сохранён в: {output_txt}")

# 2. Извлекаем слова с координатами для поиска
print("\nИзвлечение слов с координатами...")
words_with_coords = extract_words_with_coords(f"{FILE_INPUT}.pdf")
print(f"Найдено слов: {len(words_with_coords)}")

# 3. Поиск и подсветка
print(f'\nПоиск: "{SEARCH_TERMS}"...')
found = find_and_highlight(
    f"{FILE_INPUT}.pdf", output_pdf, words_with_coords, SEARCH_TERMS
)

print(f"Найдено совпадений: {len(found)}")
if found:
    print("\nРезультаты:")
    for item in found:
        print(f"  Стр. {item['page']}: {item['found_text']}")
    print(f"\nПодсвеченный PDF: {output_pdf}")
