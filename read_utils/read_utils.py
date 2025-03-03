import arxiv
import paperscraper
import fitz
import os
import requests
from openai import OpenAI
from openai.types.beta.threads.message_create_params import (
    Attachment,
    AttachmentToolFileSearch,
)
import prompt
import sys

paper_id = "1312.6211"

def download_paper(paper_id):
    """
        Attempt to download paper. Return None if paper fails to be downloaded. 
        Else return path to paper.
    """
    dir_path = os.path.join("./downloads/", paper_id)
    os.makedirs(dir_path, exist_ok=True)
    full_path = os.path.join(dir_path, "pdf")

    if not os.path.exists(full_path):
        try:
            paper = next(arxiv.Client().results(arxiv.Search(id_list=[paper_id])))
            paper.download_pdf(dirpath=dir_path, filename="pdf")
        except Exception as e:
            print(e)
            return None
    return full_path

def get_images(doc):
    for page_number, page in enumerate(doc):
        for index, img in enumerate(page.get_images(full=True)): 
            named = f"{page_number + 1}_{index}.png"
            pix = fitz.Pixmap(doc, img[0])  # Get image
            if pix.n < 5:  # Not CMYK
                pix.save(named)
            else:  # Convert CMYK to RGB
                fitz.Pixmap(fitz.csRGB, pix).save(named)

def preextract(paper_id : str):
    """
        Downloads the pdf and gets the images. 
        Later on I plan to make it possible to skip the download phase should it exist.
    """
    pdf_path = download_paper(paper_id)
    if pdf_path is None: 
        raise OSError("""Diego says: For whatever reason I could not get this file. 
                      Just catch this error, and don't offer this as an optional next scroll.""")


    #open doc, enter the directory, download images, exit the directory
    doc = fitz.open(pdf_path)
    os.chdir("./downloads/" + paper_id)
    get_images(doc)
    os.chdir("../..")
    return doc

def main():
    text = preextract(paper_id)


# Example usage

""" 
api_key = "your-api-key"
file_path = "path/to/research_paper.pdf"
summary, key_terms = getGPTresponse(api_key, file_path)

print("Summary:\n", summary)
print("\nKey Terms:\n", key_terms)

"""


# Example Usage

    

print("Full text extracted!")
#print(text)






