import openai
from openai import OpenAI

# To set your environment variables in your terminal run the following line:
#   setx OPENAI_API_KEY "place_your_key_here"
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

# Set the API key from the environment variable
client = OpenAI()

def createText():
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
      ]
    )
    return completion.choices[0].message.content


print(createText())




















































































