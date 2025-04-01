from openai import OpenAI
import os
import sys

client = OpenAI()

# Get your prompt from command-line
prompt = sys.argv[1] if len(sys.argv) > 1 else "Write something creative about DreamCube"

messages = [
    {"role": "system", "content": "You are a creative copywriter. Generate SEO-optimized content using synonyms and varied wording."},
    {"role": "user", "content": prompt}
]

# Generate 3 creative versions
for i in range(3):
    response = client.chat.completions.create(
        model="gpt-4o",  # You can try other models like "gpt-4"
        messages=messages,
        temperature=1.0,
        top_p=0.95,
        presence_penalty=0.7,
        frequency_penalty=0.7,
        max_tokens=400,
    )

    print(f"\n=== Version {i+1} ===\n")
    print(response.choices[0].message.content)
