from api import stock_api
from speech import (create_mp3, play_mp3, create_text_from_answer)
import asyncio

stocks = []

async def main():
    print("Stocks: ")
    stocks = []
    user_input = "a"
    while user_input != "":
        user_input = input("")
        stocks.append(user_input)
    answer = []
    await stock_api(stocks, answer)
    answer_str = create_text_from_answer(answer)
    file_name= "podcast.mp3"
    create_mp3(answer_str, file_name)
    play_mp3(file_name) 

if __name__ == '__main__':
    asyncio.run(main())