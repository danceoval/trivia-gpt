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
20th Century Literature
"""

number = 4

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

connect_four_prompt = f"""
Generate {number} challenging trivia questions delimited by triple backticks.

The question should follow a "connect four" format. 
A "connect four" question includes four comma-separated examples, and the answer is what they share in common.

Here is an examples of a "connect four" question:

Question: "Paris, Nice, Versaille, Bordeaux"
Answer: Cities in Paris

Question: "Butter, Horse, Shoe, Crane"
Answer: Types of fly

"""

response = get_completion(connect_four_prompt)
print(response)