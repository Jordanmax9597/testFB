import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
import os
print(" JOIN TELEGRAM ")
# os.system("xdg-open https://t.me/darksidehackerscommunity")

file_path_checkpoint = 'ANISH_REGISTERED_OK_CHECPOINT.txt'
try:
    with open(file_path_checkpoint, 'x') as file:
        file.write("")
except FileExistsError:
    print(f"The file {file_path_checkpoint} already exists.")

file_path = 'ANISH_REGISTERED_OK.txt'
try:
    with open(file_path, 'x') as file:
        file.write("")
except FileExistsError:
    print(f"The file {file_path} already exists.")

try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [Ã—] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)
logo4 = """\033[1;91m
\033[1;37m(\033[1;32m=\033[1;37m)\033[1;37m(\033[1;32m0.1\033[1;37m)
  ___   _   _ _____ _____ _   _
 / _ \ | \ | |_   _/  ___| | | |
/ /_\ \|  \| | | | \ `--.| |_| |
|  _  || . ` | | |  `--. \  _  |
| | | || |\  |_| |_/\__/ / | | |
\_| |_/\_| \_/\___/\____/\_| |_/
\033[1;37m-----------------------------------------------
\033[1;37m(\033[1;32m=\033[1;37m) Owner     : Anish God
\033[1;37m(\033[1;32m=\033[1;37m) Facebook  : facebook.com/...
\033[1;37m(\033[1;32m=\033[1;37m) Tool Type : Facebook Registration/Free Trial
\033[1;37m(\033[1;32m=\033[1;37m) Team      : Dark Side Coders Community
\033[1;37m----------------------------------------------- """

boy = ['Ali Khan', 'Rustam Khan', 'Dev Singh', 'Afzal Khan', 'Haider Khan', 'Suleman Khan', 'Nadeem Khan', 'Nazeer Malik', 'Nazeer bharat', 'Nazeer Rehmani', 'Safdar Malik', 'Intzar Khan', 'Saleem Malik', 'Abdullah Malik', 'Naseer jutt', 'Muzammil Malik', 'Fiaz Ahmad', 'Asghar Ali', 'Shabeer Ahmad', 'Irfan Ali', 'Ahmad Gujjar']
girl = ['Sajida Malik', 'Ayesha Khan', 'Nabeela Malik', 'Kinza Fatima', 'Arooj Khan', 'Muskan Khan', 'Ayesha Malik', 'Safina Malik', 'Nida Ali', 'Rimsha Ali']
ok = []
cp = []
def menu():
    os.system('clear')
    print (logo4)
    print ('')
    print (47*'-')
    print ('\033[1;37m [1] AUTO REGISTRATION ')
    print ('\033[1;37m [2] JOIN TELEGRAM ')
    print (47*'-')
    sel = input('SELECT : ')
    if sel in['1', '01']:
        create().start()
    elif sel in ['2', '02']:
        os.system('xdg-open https://t.me/darksidehackerscommunity')
        menu()
    else:
        print ('SELECT VALID OPTION')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] BOYS REGISTRATION ')
        print ('[2] GIRLS REGISTRATION ')
        print (47*'-')
        gen = input('SELECT : ')
        print (47*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('EXAMPLE : 1000, 2000, 5000, 10000')
        lim = int(input('LIMIT : '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        headers = {
     'authority': 'm.facebook.com/',
     'method': 'POST',
     'scheme': 'https',
     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     'accept-language': 'en-US,en;q=0.9',
     'cache-control': 'max-age=0',
     'dpr': '2', 'save-data': 'on',
     'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"vivo 1901"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'}

        headers1 = {
     'authority': 'mbasic.facebook.com/',
     'method': 'POST',
     'scheme': 'https',
     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     'accept-language': 'en-US,en;q=0.9',
     'cache-control': 'max-age=0',
     'dpr': '2', 'save-data': 'on',
     'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"vivo 1901"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'}

        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}(ANISH-GOD) {OO}{self.loop}/{str(lim)} OK:\033[1;92m{len(cp)} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id=07d08a48-bc7a-4822-a39b-23b9d93e8520'+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;92m (ANISH-OK - checkpoint) '+cok['c_user']+' | '+passw+'\033[1;92m ')
                    print(f"\r\r\033[1;96m (COOKIE) = "+coki)
                    open('ANISH_REGISTERED_OK_CHECPOINT.txt', 'a').write(f"{uid}|{ps}|{coki}\n")
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;92m (ANISH-OK) '+cok['c_user']+' | '+passw+'\033[1;92m ')
                                    print(f"\r\r\033[1;96m (COOKIE) = "+coki)
                                    open('ANISH_REGISTERED_OK.txt', 'a').write(f"{uid}|{ps}|{coki}\n")
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print('\r\r\033[38;5;40m (ANISH-OK) '+uid+' | '+pas)
                                    print(f"\r\r\033[1;96m (COOKIE) = "+coki)
                                    open('ANISH_REGISTERED_OK.txt', 'a').write(f"{uid}|{ps}|{coki}\n")
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('PROCESS HAS BEEN COMPLETED')
        print (47*'-')
        print ('\033[1;32mTOTAL IDs > OK/' +str(len(ok)) + ' CP/' + str(len(cp)))
        print (47*'-')
        input('back')
        menu()
menu()