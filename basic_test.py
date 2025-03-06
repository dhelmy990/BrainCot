from search import find
from read_utils.read_utils import preextract
from read_utils.GPT import getGPTresponse
import sys
import os

def main():

    keyword = input("Give me a topic. Technically i can pass in multiple.")
    searches = find([keyword])
    print("Now im just going to take the top result. But feel free to choose.")
    paper = searches.popleft()
    preextract(paper)
    os.chdir("./downloads/" + paper["title"])
    with open('./speech.txt', 'w') as file:
        file.write(getGPTresponse())    
    os.chdir("../..")
    
    







if __name__ == "__main__":
    main()