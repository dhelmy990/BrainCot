from openai import OpenAI, api_key
from texts import job
import prompt


client = OpenAI(
    api_key="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"
)

def getGPTresponse(api_key, file_path, persona="Peter Griffin"):
    # Construct the prompt
    prompt = prompt.basic

    data = {
        "model": "gpt-4-turbo",
        "messages": [{"role": "system", "content": persona},
                     {"role": "user", "content": prompt}],
        "max_tokens": 1000  # Adjust based on your needs
    }

    # Upload the file and make the request
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, headers=headers, json=data, files=files)

    if response.status_code == 200:
        result = response.json()
        summary_text = result["choices"][0]["message"]["content"]

        key_terms = []

        return summary_text, key_terms
    else:
        return f"Error: {response.status_code} - {response.text}", []