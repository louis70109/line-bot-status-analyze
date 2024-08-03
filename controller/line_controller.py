import re
import logging
from flask import request
from flask_restful import Resource, abort
from utils.configmap import Config
from utils.gemini_service import GeminiService
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3 import WebhookHandler
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)


handler = WebhookHandler(Config.LINE_CHANNEL_SECRET)
configuration = Configuration(access_token=Config.LINE_CHANNEL_ACCESS_TOKEN)

logger = logging.getLogger(__name__)


class LineController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self):
        body = request.get_data(as_text=True)
        signature = request.headers["X-Line-Signature"]

        # get request body as text
        body = request.get_data(as_text=True)
        logger.info("Request body: " + body)

        # parse webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return "OK"

    @handler.add(MessageEvent, message=TextMessageContent)
    def handle_github_actions_message(event):
        text = event.message.text
        if re.search(r"!bot", text):
            prompt = (
                "你是一位軟體工程師，以下在 Updtime-Kuma status page 當中出現的資訊"
                "你需要評斷是否解釋給主管與非技術職同事，如果有需要修改或是支援，"
                "請提供需要幫忙的單位；如果沒有或只是測試訊息，則提出中文版相對建議。"
            )
            gemini_service = GeminiService()
            response = gemini_service.generate_content(prompt + "\n log: " + text)
            logger.info(response.text)
            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        replyToken=event.reply_token,
                        messages=[TextMessage(text=response.text)],
                    )
                )
