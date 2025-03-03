import arxiv
import paperscraper
import fitz





paper_id = "1312.6211"

paper = next(arxiv.Client().results(arxiv.Search(id_list=[paper_id])))
paper.download_pdf(dirpath="./papers", filename=paper_id)

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text("text") for page in doc)
    
    with open("full_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    for page in doc:
        for img in page.get_images(full=True):
            xref = img[0]  # Image reference number
            pix = fitz.Pixmap(doc, xref)  # Get image

            if pix.n < 5:  # Not CMYK
                pix.save(f"image_{xref}.png")
            else:  # Convert CMYK to RGB
                fitz.Pixmap(fitz.csRGB, pix).save(f"image_{xref}.png")

    return text


# Example Usage
text = extract_text("papers/" + paper_id)
    

print("Full text extracted!")
#print(text)






