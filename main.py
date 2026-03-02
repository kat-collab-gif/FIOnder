"""
Пример: Сохранить текст из PDF в TXT файл
"""

import os
import time

from ocr_search import process_pdf

# === НАСТРОЙКИ ===
FILE_INPUT = "new"  # Без расширения .pdf
# =================

start = time.time()
ts = int(start)

os.makedirs("output", exist_ok=True)
output = f"output/{FILE_INPUT}Output{ts}.txt"

print(f"Обработка {FILE_INPUT}.pdf...")

# Обрабатываем PDF один раз
print(">>> Вызов process_pdf...")
result = process_pdf(f"{FILE_INPUT}.pdf")
print(f">>> process_pdf завершён за {result['elapsed_time']:.2f} сек.")

# Сохраняем текст в файл
with open(output, "w", encoding="utf-8") as f:
    f.write(result["text"])

print("\nРезультаты:")
print(f"  Страниц: {result['pages']}")
print(f"  Средняя уверенность: {result['confidence']:.1f}%")
print(f"  Распознано слов: {result['words']}")
print(f"  Время обработки: {result['elapsed_time']:.2f} сек.")
print(f"\nСохранено в: {output}")
print(f"Общее время: {time.time() - start:.2f} сек.")
