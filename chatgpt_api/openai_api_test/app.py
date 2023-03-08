# AWS Chalice https://github.com/aws/chalice
# OpenAI Python Library https://github.com/openai/openai-python
from chalice import Chalice, CORSConfig
import openai

app = Chalice(app_name="openai_api_test")
cors_config = CORSConfig(allow_origin="*")


@app.route("/", methods=["POST"], cors=cors_config)
def index():
    """
    ## 受け取るJSONの例
    { "messages": [
        {"role": "user", "content": "こんにちは"},
        {"role": "assistant", "content": "こんにちは！私はAIアシスタントです。何かお手伝いできることがありますか？"},
        {"role": "user", "content": "次のメッセージ"},
    ]}

    ## テスト用コマンド
    ### ローカルで動かす場合
    $ chalice local
    $ curl -XPOST http://localhost:8000 -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"こんにちは"}]}' | jq .

    ### AWSにデプロイする場合
    $ chalice deploy
    $ curl -XPOST <デプロイしたURL> -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"こんにちは"}]}' | jq .
    """

    try:
        # JSON読み込み
        messages = app.current_request.json_body["messages"]
        # ChatGPTに送信
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # https://platform.openai.com/docs/models/gpt-3-5
            messages=messages,
            temperature=1,  # 0に近いほど決まった文章になる 0~2 デフォルト1
        )
        # レスポンスからメッセージを取得
        ai_message = response["choices"][0]["message"]["content"]
        # AIメッセージを追加
        messages.append({"role": "assistant", "content": ai_message})
        # メッセージ一覧を返す
        return {"messages": messages}

    except Exception as e:
        return {"error": f"{e}"}
