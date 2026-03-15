from groq import Groq

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "hello"}
    ]
)

print(response.choices[0].message.content)