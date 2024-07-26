import openai

class OpenAIModel:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_report(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a senior financial planner."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
