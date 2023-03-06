from chalice import Chalice, CORSConfig
import openai

app = Chalice(app_name="openai_api_test")

cors_config = CORSConfig(allow_origin="*")


@app.route("/", methods=["POST"], cors=cors_config)
def index():
    """
    受け取るJSON
    { "messages": [
        {"role": "user", "content": "こんにちは"},
        {"role": "assistant", "content": "こんにちは！私はAIアシスタントです。何かお手伝いできることがありますか？"},
        {"role": "user", "content": "次のメッセージ"},
    ]}

    例
    $ curl -XPOST <デプロイしたURL> -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"こんにちは"}]}'
    """

    try:
        # JSON読み込み
        messages = app.current_request.json_body["messages"]

        # ChatGPTに送信
        response = openai.ChatCompletion.create(
            # モデル https://platform.openai.com/docs/models/gpt-3-5
            model="gpt-3.5-turbo",
            messages=messages,
            # 0に近いほど決まった文章になる 0~2 デフォルト1
            temperature=1,
        )

        # レスポンスからメッセージを取得
        assistant_message = response["choices"][0]["message"]["content"]

        # メッセージを追加
        messages.append({"role": "assistant", "content": assistant_message})

        # メッセージ履歴を返す
        return {"messages": messages}

    except Exception as e:
        return {"error": f"{e}"}
