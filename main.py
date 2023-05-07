import openai
key = open('./key.txt', 'r')

openai.api_key  = key.readline()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.2,
    )
    return response.choices[0].message["content"]

theme = """
Countries that no longer exist
"""

number = 5

gen_prompt = f"""
Generate {number} challenging trivia questions based on the theme, delimited by triple backticks.

```{theme}```

Questions should be of the following formats: Multiple Choice, Fill in the Blank, and Open Ended.

Here are examples of each question:

Multiple Choice:
Question: In what year did the Titanic sink?
Answers: 
A) 1910
B) 1912 (correct)
C) 1890
D) 1921

Fill in the Blank:
Question: In 2014, the Winter Olympics were hosted in _____.
Answer: "Sochi"

Open Ended:
Question: "What was the name of the horse the Roman Emperor Caligula appointed to Senate?"
Answer: "Incitatus"


"""

response = get_completion(gen_prompt)
print(response)