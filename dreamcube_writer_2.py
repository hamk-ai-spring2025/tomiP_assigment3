import os
from openai import OpenAI

client = OpenAI()

system_prompt = """
You are a bold, sarcastic, and brutally honest copywriter who hates boring pillow ads. Use humor, sharp language, and make DreamCube stand out. Avoid clichés. Mock traditional pillow marketing. Add some edgy flair. End each ad with a punchline or bold claim.
"""

prompt = input("Enter the topic or feature you'd like to highlight for DreamCube: ")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ],
    temperature=1.2,
    top_p=0.95,
    presence_penalty=0.6,
    frequency_penalty=0.2,
    n=3,
    stream=False,
    max_tokens=800,
)

for i, choice in enumerate(response.choices):
    print(f"\n=== Version {i + 1} ===\n")
    print(choice.message.content)