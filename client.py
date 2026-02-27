from openai import OpenAI

client = OpenAI(api_key="apikey")

response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output[0].content[0].text)
