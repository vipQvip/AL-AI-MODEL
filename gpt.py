#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
                                                         #ملاحظة مهمة#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#ملاحظة : لازم تجدد البروكسيات من اي موقع واي نوع بروكسي اهم شي يكون شغال لازم يكون  بروكسي من دول اوربية علمود ما تواجهك مشاكل والافضل على الولايات المتحدة الامريكية اذا ضفت بروكسي وما اشتغل وياك او ما طبعلك الايميل الجديد يعني لازم تجدد البروكسي 

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
                                                        #طريقة التشغيل#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#-1- => شغل الكود 
#-2- => اختار الخيار الاول او الثاني 
# -أ- الخيار الاول => اذا جنت تريد الجواب باستخدام البحث بجميع النماذج التختارها 
# -ب- الخيار الثاني => اذا جنت تريد الجواب بدون خاصية البحث 
# -3- => تكدر تختار الجواب من 12 نموذج اول 7 هية النماذج الاساسية مثلا اول خيار بي نماذج chatgpt فقط والثاني فقط كلود الى 7 
#=> عندك باقي الخيارات من 8 الى 12 بيهة كل النماذج يعني الموجودة من الخيار الاول الى 7 تكدر تختار منهم 
#-4- => بعد اتيار النماذج الي تريد ترسل الها السئال تضغط enter 
#-5- => من تضغط راح يبدي يسويلك حساب وهمي تلقائيا 
#-6- => بعدها يطلب منك text يعني السؤال بس تكتبة راح يبدي يجيبلك الجواب من كل النماذج ويطبعلك اسم النموذج والجواب مالة 

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                        #برمجة @vipQvip#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#الاداة متعوب عليها 3 ايام تخمط اذكر المصدر او حولها من قناتي لقناتك


                                                         #English#


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
                                                        #Important Note#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#Note: You must renew the proxies from any provider and of any type; the important thing is that they work. Proxies should be from European countries to avoid problems, and preferably from the United States of America. If you add a proxy and it does not work for you or it does not print the new email, you must renew the proxy.

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
                                                         #How to Run#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#-1- => Run the code.
#-2- => Choose option one or two.

# -A- Option One => If you want the answer using the search feature across all the models you select.

# -B- Option Two => If you want the answer without the search feature.

# -3- => You can choose the answer from 12 models; the first seven are the core models. For example, the first option may include ChatGPT models only, the second Claude only, and so on up to the seventh.

#=> Options 8 to 12 include all the models mentioned in options 1–7, and you may choose from them.
#-4- => After selecting the models you want to send the question to, press Enter.
#-5- => Upon pressing, it will start creating a fake account automatically.
#-6- => Afterwards it will ask you for the text (the question). Once you type it, it will fetch answers from all the models and print each model's name and its answer.

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
                                                  #Programmed by: @vipQvip#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#The tool took three days of work; if you use it, mention the source or transfer it from my channel to your channel.

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
                                                          #Code# #الكود#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


import requests
import json
import base64
from datetime import datetime
import time
import re
import random


aa1= input("choose  : web_search=>-1- no_search=>-2- => :")

if aa1 == "1":
    web_search = []
elif aa1 == "2":
    web_search = ['web_search']

a1 = input("choose :/n-1- openai/gpt-5 -2- openai/gpt-5-thinking -3- openai/gpt-5-mini -4- openai/gpt-4.1 -5- openai/gpt-4o -6- openai/o4-mini/n -7- openai/gpt-oss=> : ")
a2 = input("choose :/n -1- anthropic/claude-sonnet-4 -2- anthropic/claude-3.7-sonnet -3- anthropic/claude-3.5-haiku=> : ")
a3 = input("choose :/n -1- google/gemini-2.5-pro -2- google/gemini-2.5-flash=> : ")
a4 = input("choose :/n -1- deepseek/deepseek-r1 -2- deepseek/deepseek-v3=> : ")
a5 = input("choose :/n -1- x-ai/grok-4=> : ")
a6 = input("choose :/n -1- perplexity/sonar-online=> : ")
a7 = input("choose :/n-1- zai/glm-4.6=> : ")
a8 = input("choose :/n-1- openai/gpt-5 -2- openai/gpt-5-thinking -3- openai/gpt-5-mini -4- openai/gpt-4.1 -5- openai/gpt-4o -6- openai/o4-mini/n -7- openai/gpt-oss /n-8- anthropic/claude-sonnet-4 -9- anthropic/claude-3.7-sonnet -10- anthropic/claude-3.5-haiku/n-11- google/gemini-2.5-pro -12- google/gemini-2.5-flash/n-13- deepseek/deepseek-r1 -14- deepseek/deepseek-v3/n-15- x-ai/grok-4/n-16- perplexity/sonar-online -17- zai/glm-4.6=> : ")
a9 = input("choose :/n-1- openai/gpt-5 -2- openai/gpt-5-thinking -3- openai/gpt-5-mini -4- openai/gpt-4.1 -5- openai/gpt-4o -6- openai/o4-mini/n -7- openai/gpt-oss /n-8- anthropic/claude-sonnet-4 -9- anthropic/claude-3.7-sonnet -10- anthropic/claude-3.5-haiku/n-11- google/gemini-2.5-pro -12- google/gemini-2.5-flash/n-13- deepseek/deepseek-r1 -14- deepseek/deepseek-v3/n-15- x-ai/grok-4/n-16- perplexity/sonar-online -17- zai/glm-4.6=> : ")
a10 = input("choose :/n-1- openai/gpt-5 -2- openai/gpt-5-thinking -3- openai/gpt-5-mini -4- openai/gpt-4.1 -5- openai/gpt-4o -6- openai/o4-mini/n -7- openai/gpt-oss /n-8- anthropic/claude-sonnet-4 -9- anthropic/claude-3.7-sonnet -10- anthropic/claude-3.5-haiku/n-11- google/gemini-2.5-pro -12- google/gemini-2.5-flash/n-13- deepseek/deepseek-r1 -14- deepseek/deepseek-v3/n-15- x-ai/grok-4/n-16- perplexity/sonar-online -17- zai/glm-4.6=> : ")
a11 = input("choose :/n-1- openai/gpt-5 -2- openai/gpt-5-thinking -3- openai/gpt-5-mini -4- openai/gpt-4.1 -5- openai/gpt-4o -6- openai/o4-mini/n -7- openai/gpt-oss /n-8- anthropic/claude-sonnet-4 -9- anthropic/claude-3.7-sonnet -10- anthropic/claude-3.5-haiku/n-11- google/gemini-2.5-pro -12- google/gemini-2.5-flash/n-13- deepseek/deepseek-r1 -14- deepseek/deepseek-v3/n-15- x-ai/grok-4/n-16- perplexity/sonar-online -17- zai/glm-4.6=> : ")
a12 = input("choose :/n-1- openai/gpt-5 -2- openai/gpt-5-thinking -3- openai/gpt-5-mini -4- openai/gpt-4.1 -5- openai/gpt-4o -6- openai/o4-mini/n -7- openai/gpt-oss /n-8- anthropic/claude-sonnet-4 -9- anthropic/claude-3.7-sonnet -10- anthropic/claude-3.5-haiku/n-11- google/gemini-2.5-pro -12- google/gemini-2.5-flash/n-13- deepseek/deepseek-r1 -14- deepseek/deepseek-v3/n-15- x-ai/grok-4/n-16- perplexity/sonar-online -17- zai/glm-4.6=> : ")

if a1 == "1":
    a1 = "openai/gpt-5" 
elif a1 == "2":
    a1 = "openai/gpt-5-thinking"
elif a1 == "3":
    a1 = "openai/gpt-5-mini"
elif a1 == "4":
    a1 = "openai/gpt-4.1"
elif a1 == "5":
    a1 = "openai/gpt-4o"
elif a1 == "6":
    a1 = "openai/o4-mini"
elif a1 == "7":
    a1 = "openai/gpt-oss"
if a2 == "1":
    a2 = "anthropic/claude-sonnet-4"
elif a2 == "2":
    a2 = "anthropic/claude-3.7-sonnet"
elif a2 == "3":
    a2 = "anthropic/claude-3.5-haiku"
if a3 == "1":
    a3 = "google/gemini-2.5-pro"
elif a3 == "2":
    a3 = "google/gemini-2.5-flash"
if a4 == "1":
    a4 = "deepseek/deepseek-r1"
elif a4 == "2":
    a4 = "deepseek/deepseek-v3"
if a5 == "1":
    a5 = "x-ai/grok-4"
if a6 == "1":
    a6 = "perplexity/sonar-online"
if a7 == "1":
    a7 = "zai/glm-4.6"
if a8 == "1":
    a8 = "openai/gpt-5"
elif a8 == "2":
    a8 = "openai/gpt-5-thinking"
elif a8 == "3":
    a8 = "openai/gpt-5-mini"
elif a8 == "4":
    a8 = "openai/gpt-4.1"
elif a8 == "5":
    a8 = "openai/gpt-4o"
elif a8 == "6":
    a8 = "openai/o4-mini"
elif a8 == "7":
    a8 = "openai/gpt-oss"
elif a8 == "8":
    a8 = "anthropic/claude-sonnet-4"
elif a8 == "9":
    a8 = "anthropic/claude-3.7-sonnet"
elif a8 == "10":
    a8 = "anthropic/claude-3.5-haiku"
elif a8 == "11":
    a8 = "google/gemini-2.5-pro"
elif a8 == "12":
    a8 = "google/gemini-2.5-flash"
elif a8 == "13":
    a8 = "deepseek/deepseek-r1"
elif a8 == "14":
    a8 = "deepseek/deepseek-v3"
elif a8 == "15":
    a8 = "x-ai/grok-4"
elif a8 == "16":
    a8 = "perplexity/sonar-online"
elif a8 == "17":
    a8 = "zai/glm-4.6"
if a9 == "1":
    a9 = "openai/gpt-5"
elif a9 == "2":
    a9 = "openai/gpt-5-thinking"
elif a9 == "3":
    a9 = "openai/gpt-5-mini"
elif a9 == "4":
    a9 = "openai/gpt-4.1"
elif a9 == "5":
    a9 = "openai/gpt-4o"
elif a9 == "6":
    a9 = "openai/o4-mini"
elif a9 == "7":
    a9 = "openai/gpt-oss"
elif a9 == "8":
    a9 = "anthropic/claude-sonnet-4"
elif a9 == "9":
    a9 = "anthropic/claude-3.7-sonnet"
elif a9 == "10":
    a9 = "anthropic/claude-3.5-haiku"
elif a9 == "11":
    a9 = "google/gemini-2.5-pro"
elif a9 == "12":
    a9 = "google/gemini-2.5-flash"
elif a9 == "13":
    a9 = "deepseek/deepseek-r1"
elif a9 == "14":
    a9 = "deepseek/deepseek-v3"
elif a9 == "15":
    a9 = "x-ai/grok-4"
elif a9 == "16":
    a9 = "perplexity/sonar-online"
elif a9 == "17":
    a9 = "zai/glm-4.6"
if a10 == "1":
    a10 = "openai/gpt-5"
elif a10 == "2":
    a10 = "openai/gpt-5-thinking"
elif a10 == "3":
    a10 = "openai/gpt-5-mini"
elif a10 == "4":
    a10 = "openai/gpt-4.1"
elif a10 == "5":
    a10 = "openai/gpt-4o"
elif a10 == "6":
    a10 = "openai/o4-mini"
elif a10 == "7":
    a10 = "openai/gpt-oss"
elif a10 == "8":
    a10 = "anthropic/claude-sonnet-4"
elif a10 == "9":
    a10 = "anthropic/claude-3.7-sonnet"
elif a10 == "10":
    a10 = "anthropic/claude-3.5-haiku"
elif a10 == "11":
    a10 = "google/gemini-2.5-pro"
elif a10 == "12":
    a10 = "google/gemini-2.5-flash"
elif a10 == "13":
    a10 = "deepseek/deepseek-r1"
elif a10 == "14":
    a10 = "deepseek/deepseek-v3"
elif a10 == "15":
    a10 = "x-ai/grok-4"
elif a10 == "16":
    a10 = "perplexity/sonar-online"
elif a10 == "17":
    a10 = "zai/glm-4.6"
if a11 == "1":
    a11 = "openai/gpt-5"
elif a11 == "2":
    a11 = "openai/gpt-5-thinking"
elif a11 == "3":
    a11 = "openai/gpt-5-mini"
elif a11 == "4":
    a11 = "openai/gpt-4.1"
elif a11 == "5":
    a11 = "openai/gpt-4o"
elif a11 == "6":
    a11 = "openai/o4-mini"
elif a11 == "7":
    a11 = "openai/gpt-oss"
elif a11 == "8":
    a11 = "anthropic/claude-sonnet-4"
elif a11 == "9":
    a11 = "anthropic/claude-3.7-sonnet"
elif a11 == "10":
    a11 = "anthropic/claude-3.5-haiku"
elif a11 == "11":
    a11 = "google/gemini-2.5-pro"
elif a11 == "12":
    a11 = "google/gemini-2.5-flash"
elif a11 == "13":
    a11 = "deepseek/deepseek-r1"
elif a11 == "14":
    a11 = "deepseek/deepseek-v3"
elif a11 == "15":
    a11 = "x-ai/grok-4"
elif a11 == "16":
    a11 = "perplexity/sonar-online"
elif a11 == "17":
    a11 = "zai/glm-4.6"
if a12 == "1":
    a12 = "openai/gpt-5"
elif a12 == "2":
    a12 = "openai/gpt-5-thinking"
elif a12 == "3":
    a12 = "openai/gpt-5-mini"
elif a12 == "4":
    a12 = "openai/gpt-4.1"
elif a12 == "5":
    a12 = "openai/gpt-4o"
elif a12 == "6":
    a12 = "openai/o4-mini"
elif a12 == "7":
    a12 = "openai/gpt-oss"
elif a12 == "8":
    a12 = "anthropic/claude-sonnet-4"
elif a12 == "9":
    a12 = "anthropic/claude-3.7-sonnet"
elif a12 == "10":
    a12 = "anthropic/claude-3.5-haiku"
elif a12 == "11":
    a12 = "google/gemini-2.5-pro"
elif a12 == "12":
    a12 = "google/gemini-2.5-flash"
elif a12 == "13":
    a12 = "deepseek/deepseek-r1"
elif a12 == "14":
    a12 = "deepseek/deepseek-v3"
elif a12 == "15":
    a12 = "x-ai/grok-4"
elif a12 == "16":
    a12 = "perplexity/sonar-online"
elif a12 == "17":
    a12 = "zai/glm-4.6"

proxies = [
    '35.243.0.245:10052',
    '35.243.0.211:10016'
]
hh = random.choice(proxies)
proxies = {
    'http': f'http://{hh}',
    'https': f'http://{hh}'
}

def ree(response_text):
    lines = response_text.strip().split('\n')
    xxx = ""
    for line in lines:
        if line.startswith('data: '):
            try:
                data = json.loads(line[6:])
                if data.get('type') == 'text-delta':
                    xxx += data.get('textDelta', '')
            except:
                pass
    return xxx


cookies = {
    '_ga_SNRFLG64RE': 'GS2.1.s1759401640$o1$g0$t1759401640$j60$l0$h0',
    '_ga': 'GA1.1.1328009023.1759401641',
    '__gads': 'ID=0a54f1cb8d531425:T=1759401642:RT=1759401642:S=ALNI_MbYLL1uGPJH4NtD_mY_-92He57Smw',
    '__gpi': 'UID=0000129354c9e48c:T=1759401642:RT=1759401642:S=ALNI_Mbdb_sNViG11dK2JNf_4YDI0mNNiw',
    '__eoi': 'ID=a567755043a133ec:T=1759401642:RT=1759401642:S=AA-AfjYY1RayGJ7IkfxpZVFMFE4b',
    'FCNEC': '%5B%5B%22AKsRol9AXgYS0dljjZmxXlt7WvLZ1gAB41W7Iegf1ChsxQoE8Cd5jP4ahCbREoosaFgAxVuhu0N_vAe4D-nIhA-0qvlfJyLSjzhIQjOkOTpYJX7GMl4B_Q7tUrW_zggHlsuRxZCopgNXEo83FhDsZlEdJhp0JdrioA%3D%3D%22%5D%5D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'priority': 'u=1, i',
    'referer': 'https://temporarymail.com/ar/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'action': 'generateRandomName',
    'value': '1',
}

response = requests.get('https://temporarymail.com/api/', params=params, cookies=cookies, headers=headers)
data1 = json.loads(response.text)
aa = data1['address']
print(aa)

cookies = {
    '_ga_SNRFLG64RE': 'GS2.1.s1759401640$o1$g0$t1759401640$j60$l0$h0',
    '_ga': 'GA1.1.1328009023.1759401641',
    '__gads': 'ID=0a54f1cb8d531425:T=1759401642:RT=1759401642:S=ALNI_MbYLL1uGPJH4NtD_mY_-92He57Smw',
    '__gpi': 'UID=0000129354c9e48c:T=1759401642:RT=1759401642:S=ALNI_Mbdb_sNViG11dK2JNf_4YDI0mNNiw',
    '__eoi': 'ID=a567755043a133ec:T=1759401642:RT=1759401642:S=AA-AfjYY1RayGJ7IkfxpZVFMFE4b',
    'FCNEC': '%5B%5B%22AKsRol9AXgYS0dljjZmxXlt7WvLZ1gAB41W7Iegf1ChsxQoE8Cd5jP4ahCbREoosaFgAxVuhu0N_vAe4D-nIhA-0qvlfJyLSjzhIQjOkOTpYJX7GMl4B_Q7tUrW_zggHlsuRxZCopgNXEo83FhDsZlEdJhp0JdrioA%3D%3D%22%5D%5D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'priority': 'u=1, i',
    'referer': 'https://temporarymail.com/ar/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

respons = requests.get(
    f'https://temporarymail.com/api/?action=requestEmailAccess&key=&value={aa}@FusionInbox.com&r=https%3A%2F%2Fwww.google.com%2F',
    cookies=cookies,
    headers=headers,
    proxies=proxies,
)
data2 = json.loads(respons.text)
ss = data2['secretKey']
dd = data2['address']
print(ss)
print(dd)

email = dd

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNyaGh0Y3VqdGhrZ2RmY3F5YmJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg1MDg4MTAsImV4cCI6MjAyNDA4NDgxMH0.bWOkpy_2dxno_AfRUNOwFhe4zgMQXhCyRYdjROFtePs',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNyaGh0Y3VqdGhrZ2RmY3F5YmJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg1MDg4MTAsImV4cCI6MjAyNDA4NDgxMH0.bWOkpy_2dxno_AfRUNOwFhe4zgMQXhCyRYdjROFtePs',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.chathub.gg',
    'priority': 'u=1, i',
    'referer': 'https://app.chathub.gg/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-client-info': 'supabase-ssr/0.7.0 createBrowserClient',
    'x-supabase-api-version': '2024-01-01',
}

params = {
    'redirect_to': 'https://app.chathub.gg/auth/callback?next=%2F',
}

json_data = {
    'email': email,
    'data': {},
    'create_user': True,
    'gotrue_meta_security': {},
    'code_challenge': 'XrO-y767X30aCTGrJ90iH3nQiRqrMh5fW2IlM5t2IZQ',
    'code_challenge_method': 's256',
}

response = requests.post('https://srhhtcujthkgdfcqybbw.supabase.co/auth/v1/otp', params=params, headers=headers, json=json_data)
print(response.text)

time.sleep(5)

cookies = {
    '_ga_SNRFLG64RE': 'GS2.1.s1759401640$o1$g0$t1759401640$j60$l0$h0',
    '_ga': 'GA1.1.1328009023.1759401641',
    '__gads': 'ID=0a54f1cb8d531425:T=1759401642:RT=1759401642:S=ALNI_MbYLL1uGPJH4NtD_mY_-92He57Smw',
    '__gpi': 'UID=0000129354c9e48c:T=1759401642:RT=1759401642:S=ALNI_Mbdb_sNViG11dK2JNf_4YDI0mNNiw',
    '__eoi': 'ID=a567755043a133ec:T=1759401642:RT=1759401642:S=AA-AfjYY1RayGJ7IkfxpZVFMFE4b',
    'FCNEC': '%5B%5B%22AKsRol9AXgYS0dljjZmxXlt7WvLZ1gAB41W7Iegf1ChsxQoE8Cd5jP4ahCbREoosaFgAxVuhu0N_vAe4D-nIhA-0qvlfJyLSjzhIQjOkOTpYJX7GMl4B_Q7tUrW_zggHlsuRxZCopgNXEo83FhDsZlEdJhp0JdrioA%3D%3D%22%5D%5D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'priority': 'u=1, i',
    'referer': 'https://temporarymail.com/ar/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'action': 'checkInbox',
    'value': ss,
}

response = requests.get('https://temporarymail.com/api/', params=params, cookies=cookies, headers=headers)

data3 = json.loads(response.text)
key = list(data3.keys())[0]
id = data3[key]['id']
print(id)

cookies = {
    '_ga_SNRFLG64RE': 'GS2.1.s1759401640$o1$g0$t1759401640$j60$l0$h0',
    '_ga': 'GA1.1.1328009023.1759401641',
    '__gads': 'ID=0a54f1cb8d531425:T=1759401642:RT=1759401642:S=ALNI_MbYLL1uGPJH4NtD_mY_-92He57Smw',
    '__gpi': 'UID=0000129354c9e48c:T=1759401642:RT=1759401642:S=ALNI_Mbdb_sNViG11dK2JNf_4YDI0mNNiw',
    '__eoi': 'ID=a567755043a133ec:T=1759401642:RT=1759401642:S=AA-AfjYY1RayGJ7IkfxpZVFMFE4b',
    'FCNEC': '%5B%5B%22AKsRol9AXgYS0dljjZmxXlt7WvLZ1gAB41W7Iegf1ChsxQoE8Cd5jP4ahCbREoosaFgAxVuhu0N_vAe4D-nIhA-0qvlfJyLSjzhIQjOkOTpYJX7GMl4B_Q7tUrW_zggHlsuRxZCopgNXEo83FhDsZlEdJhp0JdrioA%3D%3D%22%5D%5D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'priority': 'u=0, i',
    'referer': 'https://temporarymail.com/ar/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

params = {
    'i': id,
    'width': '0',
}

response = requests.get('https://temporarymail.com/view/', params=params, cookies=cookies, headers=headers)
code = response.text.split('<h3>')[1].split('</h3>')[0]
print(code)

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNyaGh0Y3VqdGhrZ2RmY3F5YmJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg1MDg4MTAsImV4cCI6MjAyNDA4NDgxMH0.bWOkpy_2dxno_AfRUNOwFhe4zgMQXhCyRYdjROFtePs',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNyaGh0Y3VqdGhrZ2RmY3F5YmJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg1MDg4MTAsImV4cCI6MjAyNDA4NDgxMH0.bWOkpy_2dxno_AfRUNOwFhe4zgMQXhCyRYdjROFtePs',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.chathub.gg',
    'priority': 'u=1, i',
    'referer': 'https://app.chathub.gg/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-client-info': 'supabase-ssr/0.7.0 createBrowserClient',
    'x-supabase-api-version': '2024-01-01',
}

json_data = {
    'email': email,
    'token': code,
    'type': 'email',
    'gotrue_meta_security': {},
}

respons = requests.post('https://srhhtcujthkgdfcqybbw.supabase.co/auth/v1/verify', headers=headers, json=json_data)

data4 = json.loads(respons.text)
ac = data4['access_token']
user = data4['user']['id']
rr = data4['refresh_token']

ah = {
    "access_token": ac,
    "token_type": "bearer",
    "expires_in": 3600,
    "expires_at": data4['expires_at'],
    "refresh_token": rr,
    "user": data4['user']
}
au = base64.b64encode(json.dumps(ah).encode()).decode()

text = input("text: ")
cookies1 = {
    'user-source': 'gas',
    '_gcl_au': '1.1.1321931192.1759391043',
    '_tt_enable_cookie': '1',
    '_ttp': '01K6HY1R0D3B4MDTANXDRQ38ZC_.tt.1',
    '_gcl_aw': 'GCL.1759391818.Cj0KCQjwovPGBhDxARIsAFhgkwThljj1iPfdf9SpTatMNcVcuoGn-eY5uNk9EWWBVLwouflZuBMTBs0aAhMjEALw_wcB',
    'ttcsid': '1759391047697::To4I6zfUVPbHFDOcVimu.1.1759391858105.0',
    'ttcsid_D1UR7DJC77U5O6T3RBIG': '1759391047696::F1v51HCVIFPc-DGMooOE.1.1759391858105.0',
    'sb-srhhtcujthkgdfcqybbw-auth-token-code-verifier': 'base64-IjI2YTU3NDE4ZWEyZWYwN2YyYWIxMTEyNTY2NDczNjNiZTdlODQzZDNmMjdkZjZlMWZkNjNhYWQ3MjAyOTZiOGU2NmRmMTczMTQ5YWZlZjA4NGI1ZmZlN2FlZmE0ZmVhY2I2NDU0M2UxNzI3ODUwNzki',
    'sb-srhhtcujthkgdfcqybbw-auth-token': f'base64-{au}',
    'ph_phc_QOZxlMIV2uRLEM3Zw64TN0GAwI0PJMqRABpoHJSrCJN_posthog': f'%7B%22distinct_id%22%3A%22{user}%22%2C%22%24sesid%22%3A%5B1759392044837%2C%220199a3e0-cbcd-7448-809d-ad031c092726%22%2C1759391042509%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22https%3A%2F%2Fwww.youtube.com%2F%22%2C%22u%22%3A%22https%3A%2F%2Fchathub.gg%2F%3Futm_source%3Dgas%26utm_medium%3Dcpc%26utm_campaign%3D22968115416%26gad_source%3D2%26gad_campaignid%3D22968115416%26gclid%3DCj0KCQjwovPGBhDxARIsAFhgkwThljj1iPfdf9SpTatMNcVcuoGn-eY5uNk9EWWBVLwouflZuBMTBs0aAhMjEALw_wcB%22%7D%7D',
}

headers1 = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://app.chathub.gg',
    'priority': 'u=1, i',
    'referer': 'https://app.chathub.gg/?utm_source=chathub.gg',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-app-id': 'web',
    'x-client-time': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
    'x-device-id': user,
    'x-model': a1,
}

json_data = {
    'model': a1,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

re = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a1}")
print(ree(re.text))
print("\n")

json_data = {
    'model': a2,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

res = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a2}")
print(ree(res.text))
print("\n")

json_data = {
    'model': a3,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

r = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a3}")
print(ree(r.text))
print("\n")

json_data = {
    'model': a4,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

p = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a4}")
print(ree(p.text))
print("\n")

json_data = {
    'model': a5,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

n = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a5}")
print(ree(n.text))
print("\n")





json_data = {
    'model': a6,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

x = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a6}")
print(ree(x.text))
print("\n")

json_data = {
    'model': a7,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

r = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a7}")
print(ree(r.text))
print("\n")

json_data = {
    'model': a8,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

r = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a8}")
print(ree(r.text))
print("\n")

json_data = {
    'model': a9,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

r = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a9}")
print(ree(r.text))
print("\n")

json_data = {
    'model': a10,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

r = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a10}")
print(ree(r.text))
print("\n")

json_data = {
    'model': a11,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

r = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a11}")
print(ree(r.text))
print("\n")

json_data = {
    'model': a12,
    'messages': [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': text,
                },
            ],
        },
    ],
    'fileIds': [],
    'tools': web_search,
}

r = requests.post('https://app.chathub.gg/api/v3/chat/completions', cookies=cookies1, headers=headers1, json=json_data)
print(f"{a12}")
print(ree(r.text))
print("\n")

print("DEV :  @vipQvip \n github=> - https://github.com/vipQvip - github tool=> - https://github.com/vipQvip/AL-AI-MODEL - \n")
