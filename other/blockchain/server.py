import os
from bottle import get, post, run, request, template
from module.blockchain import BlockChain


@get("/")
@post("/")
def index():
    if data := request.forms.data:
        block_chain.add_block(data)
    if request.query.delete == "true":
        block_chain.delete()

    return template(
        """
      <!DOCTYPE html>
      <html><head>
        <meta charset="utf-8"/>
        <title>ブロックチェーン デモ</title>
        <style>
          table { width: 100%; table-layout: fixed; }
          table td { overflow-wrap : break-word; text-align: center; }
        </style>
      </head><body>
        <h3>ブロックチェーン デモ</h3>
        <form action="/" method="POST">
          データ: <input name="data" size="50" type="text" />
          <input value="追加" type="submit" />
        </form>
        <a href="/?delete=true">１つ削除</a>
        <hr/>
        <table border="1">
          <thead>
            <tr>
              <th width="10%" style="background: royalblue; color: white;">(a) index</th>
              <th width="20%" style="background: royalblue; color: white;">(b) timestamp</th>
              <th width="40%" style="background: royalblue; color: white;">(c) データ</th>
              <th width="15%" style="background: royalblue; color: white;">(d) 前のhash</th>
              <th width="15%" style="background: forestgreen; color: white;">Hash(a, b, c, d)</th>
            </tr>
          </thead>
          <tbody>
          %for block in block_chain:
            <tr>
              <td>{{block.index}}</td>
              <td>{{block.timestamp}}</td>
              <td>{{block.data}}</td>
              <td>{{block.previous_hash}}</td>
              <td>{{block.hash}}</td>
            </tr>
          %end
          </tbody>
        </table>
      </body></html>
    """,
        block_chain=block_chain.get_history(),
    )


if __name__ == "__main__":
    block_chain = BlockChain()

    # test data
    block_chain.add_block('{"送金元":"Aさん","送金先":"Bさん","金額":"12345"}')
    block_chain.add_block('{"送金元":"Cさん","送金先":"Dさん","金額":"98765"}')
    block_chain.add_block('{"送金元":"Eさん","送金先":"Fさん","金額":"55555"}')
    block_chain.add_block("Hello, World!")

    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
