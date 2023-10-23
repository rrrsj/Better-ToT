import re
from test import get_ans
import json
def normail_tool_output(message):
    ans = get_ans("Please change this string to json format.\\n" + message)
    ans = ans.replace('\'', '\"')
    ans = ans.replace('\\n', '')
    step = json.loads(ans)
    return 