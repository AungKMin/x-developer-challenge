from dotenv import  load_dotenv
load_dotenv()

import asyncio
import xai_sdk
import json

async def stock_api(stocks, answer):
    client = xai_sdk.Client()
    sampler = client.sampler

    PREAMBLE = """\
This is a conversation between a human user and a highly intelligent AI. The AI's name is Grok and it makes every effort to truthfully answer a user's questions. It always responds politely but is not shy to use its vast knowledge in order to solve even the most difficult problems. The conversation begins.

Human: I want you to tell me whether the sentiments of stocks are bullish or bearish, and why. Use the most up to date and relevant information on X.

Please format your answer as a valid JSON. For eg. if the stocks I asked for are AAPL and AMZN, and the sentiment for AAPL is bullish, and the sentiment for AMZN is bearish, your output should be

[
    {
        "name": "AAPL",
        "sentiment": "bullish",
        "reason": "some reason"
    },
    {
        "name": "AMZN",
        "sentiment": "bearish",
        "reason": "some reason"
    }
]
<|separator|>

Assistant: Understood! Please provide the list of stocks as a list"""

# AAPL, AMZN

    text = ', '.join(stocks)

    prompt = PREAMBLE + f"<|separator|>\n\nHuman: {text}<|separator|>\n\nAssistant: " + "{\n"
    # print(prompt)
    async for token in  sampler.sample(
        prompt=prompt,
        max_len=1024,
        stop_tokens=["<|separator|>"],
        temperature=0.5,
        nucleus_p=0.95):
        answer.append(token.token_str)

if __name__ == '__main__':
    stocks = ['SNOW', 'GME']
    answer = []
    asyncio.run(stock_api(stocks, answer))
    
    answer_str = "{" + ''.join(answer)
    print(answer_str)
    print("---")
    print(json.loads(answer_str))
