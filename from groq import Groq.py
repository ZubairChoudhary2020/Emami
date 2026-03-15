from groq import Groq

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[
        {"role": "user", "content": "hello"}
    ]
)

print(response.choices[0].message.content)