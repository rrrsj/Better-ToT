import json
import re
from test import get_ans
def normail_work_output(message):
    ans = get_ans("Please change this string to json format.\\n" + message)
    ans = ans.replace('\'', '\"')
    ans = ans.replace('\\n', '')
    step=json.loads(ans)
    return step