from hugchat import hugchat
from hugchat.login import Login

def ai_surov(referat_mavzu):
    EMAIL = "EMAIL"
    PASSWD = "PASSWD"
    cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

    #referat_mavzu = "Alisher Navoiy hayoti va ijodi"

    message_result = chatbot.chat(f"{referat_mavzu} - mavzusida maqola yoz") # note: message_result is a generator, the method will return immediately.
    print(message_result)

from g4f.client import Client
def gpt_surov(referat_mavzu):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{referat_mavzu} - mavzusida maqola yoz, maqola o'zbek tilida bo'lsin"}],
    )
    javob = response.choices[0].message.content
    return javob

# print(gpt_surov("Alisher Navoiy"))