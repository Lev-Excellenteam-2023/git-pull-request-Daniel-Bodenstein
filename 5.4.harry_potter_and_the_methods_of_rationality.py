import os
import re
from bs4 import BeautifulSoup

def extract_real_name(path):
    # Open the HTML file and read the contents
    potter_text = open(path, 'r', encoding="utf8").read()

    # Use Beautiful Soup to parse the HTML
    soup = BeautifulSoup(potter_text, 'html.parser')

    # Find the title element and extract the text
    title = (str)(soup.find('title').get_text)

    sp = re.split('Chapter |: |<', title)

    return (sp[3].zfill(3) + " " + sp[4])

def harry_potter_and_the_methods_of_rationality_5_4(path):
    # iterate over files in the directory
    for filename in os.scandir(path):
        if filename.is_file():
            real_name = extract_real_name(filename.path)
            os.rename(filename.path, os.path.join(path, real_name))


#harry_potter_and_the_methods_of_rationality_5_4(
#    r"C:\Users\User\Desktop\exelenteam\python\Notebooks\week05\resources\potter")
