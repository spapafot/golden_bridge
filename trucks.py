import pandas as pd
import pdfplumber
import re

def main(fname):
    
    final = []
    text = ""
    
    with pdfplumber.open(fname) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    with open("sample.txt", "w", encoding='utf-8') as text_file:
        text_file.write(text)

    with open("sample.txt", "r", encoding='utf-8') as txt:
        text_file_ = txt.readlines()

    # Only unique line identifier is "|F"
    
    for i in text_file_:
        if "¦F" in i:
            if "VESSEL" not in i:
                i = i[1:]
                a = i.split("DEBIT", maxsplit=1)
                b = re.split("GOLDEN |¦ ", a[0])
                final.append(b)

    data = pd.DataFrame(final)
    
    # Duplicates are canceled tickets (eg F54421 +200 and F54421 -200) so discard them
    
    data = data.drop_duplicates(subset=[0], keep=False)
    data[1] = data[1].str[1:]

    for i in range(3, 8):
        data[i] = data[i].str.replace(",", ".").astype(float)

    # Group by company can be done with cashier, more accurate as it is agency handled
    
    with pd.ExcelWriter("trucks.xlsx", "xlsxwriter") as writer:
        pd.DataFrame(data).to_excel(writer, index=None)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filename')
    parser.add_argument('-f', type=str, required=True, help="Enter the filename in '1607BRIG.pdf' format")
    args = parser.parse_args()
    main(args.fname)
