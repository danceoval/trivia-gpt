import openai
from prompts import gen_prompt, connect_four_prompt, image_prompt

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

def get_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )
    return response["data"][0]["url"]

def main(q_count):
    print("*** RUNNING ***")
    input_str = input('Enter your topics for each trivia round, separated by topic:')
    topics = input_str.split(", ")
    for topic in topics:
        prompt = gen_prompt(topic, q_count)
        response = get_completion(prompt)
        print(response)
    print("** DONE **")

main(3)