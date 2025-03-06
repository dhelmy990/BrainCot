from core_secret import API_KEY
import requests
import pprint
from collections import deque

RESULTS_NEEDED = 5
RETRIES_ALLOWED = 10

def find(keywords : list):
    """

    """

    query = "|".join(keywords)
    url = f"https://api.core.ac.uk/v3/search/works?q={query}&limit=5"

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)


    final_answer = deque()
    for i in range(RETRIES_ALLOWED):
        if response.status_code == 200:
            papers = response.json()["results"]
            for index, paper in enumerate(papers):
                if paper['downloadUrl'] is not None:
                    final_answer.append(paper)
            break
        else:
            print("Error:", response.json())
    
    return final_answer

#find(["machine learning", "neuroscience", "brain-computer interface"])

