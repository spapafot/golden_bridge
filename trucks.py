import pandas as pd
import pdfplumber
import re

fname = "GBA.pdf"
final = []
text = ""

with pdfplumber.open(fname) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

with open("sample.txt", "w", encoding='utf-8') as text_file:
    text_file.write(text)

with open("sample.txt", "r", encoding='utf-8') as txt:
    text_file_ = txt.readlines()

for i in text_file_:
    if "¦F" in i:
        if "VESSEL" not in i:
            i = i[1:]
            a = i.split("DEBIT", maxsplit=1)
            b = re.split("GOLDEN |¦ ", a[0])
            final.append(b)

data = pd.DataFrame(final)
data = data.drop_duplicates(subset=[0], keep=False)
data[1] = data[1].str[1:]

for i in range(3, 8):
    data[i] = data[i].str.replace(",", ".").astype(float)

data_ = data[data[1].str.contains("02/07")]

x = data.groupby([4])[4].count()
print(x)

with pd.ExcelWriter("trucks.xlsx", "xlsxwriter") as writer:
    pd.DataFrame(data_).to_excel(writer, index=None)

