from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)



line_bot_api = LineBotApi('179w/TtDVAh5Ga3Wj5wyD729bLgCLqwO1QW0SybB4n1Zt+yU2WdlzdmWyYOxAIoZH7dFKC+xHWXrga0tCxplGbHYWxtwhfSF71P+V7lASb5wO7KnYjEiX2qtUls5gTooYuic4hXyCY9NotQgd743JgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b9e9b549a09e2eeb3dca73168a3c51fa')

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
