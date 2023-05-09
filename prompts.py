def gen_prompt(theme, num):
    prompt = f"""
Generate {num} challenging trivia questions based on the theme, delimited by triple backticks.

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
    return prompt

def connect_four_prompt(num):
    prompt =  f"""
        Generate {num} challenging trivia questions.

        The question should follow a "connect four" format. 
        A "connect four" question includes four comma-separated examples, and the answer is what they share in common.

        Here is an examples of a "connect four" question:

        Question: "Paris, Nice, Versaille, Bordeaux"
        Answer: Cities in Paris

        Question: "Butter, Horse, Shoe, Crane"
        Answer: Types of fly

        """
    return prompt

def image_prompt(theme):
    prompt = f"""
Generate an image based on the theme delimited by triple backticks.

```{theme}```

"""
    return prompt