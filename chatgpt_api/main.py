"""
環境変数にAPI_KEYをsetしておく
$ export OPENAI_API_KEY=<OpenAIのAPI_KEY>
"""

import openai
import time


try:

    messages = []

    while True:

        user_message = input("あなた:")
        messages.append({"role": "user", "content": user_message})

        response = openai.ChatCompletion.create(
            # モデル https://platform.openai.com/docs/models/gpt-3-5
            model="gpt-3.5-turbo",
            messages=messages,
            # 0に近いほど決まった文章になる 0~2 デフォルト1
            temperature=1,
        )

        assistant_message = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": assistant_message})

        print(assistant_message)
        time.sleep(1)


except Exception as e:
    result = "エラーが発生しました。"

print(result)
