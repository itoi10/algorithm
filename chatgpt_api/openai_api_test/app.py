# AWS Chalice https://github.com/aws/chalice
# OpenAI Python Library https://github.com/openai/openai-python
import openai
from chalice import Chalice, CORSConfig

app = Chalice(app_name="openai_api_test")
cors_config = CORSConfig(allow_origin="*")


@app.route("/chat", methods=["POST"], cors=cors_config)
def chat():
    """
    ## 受け取るJSONの例
    {"messages": [
        {"role": "user", "content": "こんにちは"},
        {"role": "assistant", "content": "こんにちは！私はAIアシスタントです。何かお手伝いできることがありますか？"},
        {"role": "user", "content": "次のメッセージ"},
    ]}

    ## テスト用コマンド
    - ローカル
    $ curl -XPOST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"こんにちは"}]}' | jq .

    - デプロイ
    $ curl -XPOST $(chalice url)/chat -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"こんにちは"}]}' | jq .
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
        return {"result": messages}

    except Exception as e:
        return {"message": f"{e}"}


@app.route("/threelines", methods=["POST"], cors=cors_config)
def threelines():
    """
    ## 受け取るJSONの例
    {"original_text": ”要約したい文章... ”}
    """

    try:
        # JSON読み込み
        original_text = app.current_request.json_body["original_text"]

        messages = [
            {"role": "system", "content": "次の文章を3行の箇条書きで簡潔に要約してください。要約できない場合は理由を含めて教えてください。"},
            {"role": "user", "content": original_text},
        ]

        # ChatGPTに送信
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # https://platform.openai.com/docs/models/gpt-3-5
            messages=messages,
            temperature=1,  # 0に近いほど決まった文章になる 0~2 デフォルト1
        )
        # レスポンスからメッセージを取得
        ai_message = response["choices"][0]["message"]["content"]
        # メッセージ一覧を返す
        return {"result": ai_message}

    except Exception as e:
        return {"message": f"{e}"}


@app.route("/useless", methods=["POST"], cors=cors_config)
def useless():
    """
    ## 受け取るJSONの例
    {"original_text": ”無駄に長くしたい文章... ”}
    """

    try:
        # JSON読み込み
        original_text = app.current_request.json_body["original_text"]

        messages = [
            {"role": "system", "content": "次の文章を無駄に長くしてください。"},
            {"role": "user", "content": original_text},
        ]

        # ChatGPTに送信
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # https://platform.openai.com/docs/models/gpt-3-5
            messages=messages,
            temperature=1,  # 0に近いほど決まった文章になる 0~2 デフォルト1
        )
        # レスポンスからメッセージを取得
        ai_message = response["choices"][0]["message"]["content"]
        # メッセージ一覧を返す
        return {"result": ai_message}

    except Exception as e:
        return {"message": f"{e}"}
