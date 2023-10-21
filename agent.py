import openai
import json
from key import api_key
openai.api_base = "https://api.chatanywhere.com.cn/v1"
openai.api_key = api_key
class Model():
    def __call__(
        self,
        message: str,
    ):
        ans=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message
        )
        return ans