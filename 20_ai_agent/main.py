import os
import json
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def get_weather(city: str) -> str:
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}&units=metric"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error: Could not get weather for {city}"
    data = response.json()
    return f"{city}: {data['weather'][0]['description']}, {data['main']['temp']}°C"


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"}
                },
                "required": ["city"],
            },
        },
    }
]

available_tools = {"get_weather": get_weather}


def run_agent(user_query: str):
    messages = [{"role": "user", "content": user_query}]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
        )

        message = response.choices[0].message

        # no tool call — final answer
        if not message.tool_calls:
            print(message.content)
            break

        # tool call — execute and feed result back
        messages.append(message)

        for tool_call in message.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)
            fn_result = available_tools[fn_name](**fn_args)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": fn_result,
            })


def main():
    user_query = input("> ")
    run_agent(user_query)


if __name__ == "__main__":
    main()
