import pdfplumber


def DM(pdfList):
    pgList = []
    for i in pdfList:
        # Applied Data Science.pdf
        infile = "C://Users/karti/OneDrive/Documents/AUTOMATED Q&A/"+i

        with pdfplumber.open(infile) as pdf:
            totalpages = len(pdf.pages)
            for i in range(0, totalpages):
                page = pdf.pages[i]
                row = page.extract_text()
                pgList.append(row)

    # collect all text documents as list
    text_docs = pgList
    return text_docs
