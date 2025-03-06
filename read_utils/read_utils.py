import arxiv
import fitz
import os
import requests
from . import prompt
import sys
from time import sleep

paper_id = "1312.6211"

def vet(url):
    """
        This function exists because for some reason some times downloadPdf is insistent on sending you to the page
        just outside the pdf download. Annoying
    """

    if 'arxiv' in url:
        # Replace 'abs' with 'pdf' in the URL
        return url.replace('abs', 'pdf')
    return url

def download_paper(paper_id, download_url):
    """
        Attempt to download paper. Return None if paper fails to be downloaded. 
        Else return path to paper.
    """

    dir_path = os.path.join("./downloads/", paper_id)
    os.makedirs(dir_path, exist_ok=True)
    full_path = os.path.join(dir_path, "pdf")


    if not os.path.exists(full_path):
        try:
            download_url = vet(download_url)
            response = requests.get(download_url)
            if response.status_code == 200:
                with open(full_path, 'wb') as f:
                    f.write(response.content)
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
                

def preextract(paper : dict):
    """
        Downloads the pdf and gets the images. 
        Later on I plan to make it possible to skip the download phase should it exist.
    """


    pdf_path = download_paper(paper["title"], paper["downloadUrl"])
    if pdf_path is None: 
        raise OSError("""Diego says: For whatever reason I could not get this file. 
                      Just catch this error, and don't offer this as an optional next scroll.""")
    sleep(1)

    #open doc, enter the directory, download images, exit the directory
    doc = fitz.open(pdf_path)
    
    os.chdir("./downloads/" + paper["title"])
    get_images(doc)
    with open('extract.txt', 'w') as file:
        file.write(paper["fullText"])
    os.chdir("../..")
    return pdf_path

def main():
    text = preextract({"title" : "JNEEG shield for Jetson Nano for real-time EEG signal processing with deep learning", "downloadUrl" : "http://arxiv.org/abs/2405.09575"})

# Example Usage
#print("Full text extracted!")







