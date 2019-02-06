from bs4 import BeautifulSoup
import re
import requests

def get_Htmltext(aim_Url):

    try:
        response = requests.get(aim_Url)
        response.encoding = "utf8"
        result = response.text
        return result

    except Exception as e:
        print("aim_Url requests error !")

def get_Reresult(re_Expretion,aim_Text):

    try:
        re_compile = re.compile(re_Expretion)
        result = re_compile.findall(aim_Text,re.S)
        return result

    except Exception as e:
        print("re_Result error Please change re_Expretion !")

def get_Selectresult(select_Expretion,html_Text):

    try:
        html_Text = html_Text
        soup = BeautifulSoup(html_Text,"lxml")
        select_result = soup.select(select_Expretion)
        return select_result
    except Exception as e:
        print("select_Expretion error Please change !")




