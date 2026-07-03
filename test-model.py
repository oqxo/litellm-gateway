from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000/v1",
    api_key="sk-GsNwdMUVXAnlLiEvxjh4VA"  # your virtual key
)

response = client.chat.completions.create(
    model="spark-nano-5",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)