#DALVIK UA_GENERATE_CODE

#CODE BY MUHAMMAD HAMMAD
# MUGHAL ZADA
import platform
import random

import os
import random
def clear():
    os.system('clear')
    print(logo)
#sys.stdout.write('\x1b]2; MAFIA M16 \x07')
logo=("""\033[1;32m
\033[1;34m================\033[1;34m===========\033[1;34m====================
  \033[1;32m[+]Paid version and modified by Moh 
\033[1;34m================\033[1;34m===========\033[1;34m====================
  \033[1;32m██╗    ██╗██╗████████╗███████╗
  \033[1;32m██║    ██║██║╚══██╔══╝██╔════╝
  \033[1;32m██║ █╗ ██║██║   ██║   █████╗  
  \033[1;32m██║███╗██║██║   ██║   ██╔══╝  
  \033[1;32m╚███╔███╔╝██║   ██║   ███████╗      
  \033[1;32m ╚══╝╚══╝ ╚═╝   ╚═╝   ╚══════╝            
\033[1;34m================\033[1;34m===========\033[1;34m=================
 \033[1;32m[=]\033[1;37m DEVLOPER \033[1;31m: \033[1;32mMOH !               
 \033[1;32m[=]\033[1;37m FACEBOOK \033[1;31m: \033[1;32mMOH !               
 \033[1;32m[=]\033[1;37m STATE \033[1;31m   : \033[1;32mFREE.                   
 \033[1;32m[=]\033[1;37m TIPE\033[1;31m     : \033[1;32mVERESON V/0.0.2        
\033[1;34m================\033[1;34m===========\033[1;34m================""")

def menu():
        try:
                clear()
        
                x = ("sex")
                if x == ("sex"):
                        print(' \033[1;32m[1] \033[1;37mFile cloning\n \033[1;32m[2] \033[1;37mCrate File\n \033[1;32m[3] \033[1;37mUnblock Ip \n \033[1;32m[4] \033[1;37mCheak Apk \n \033[1;32m[5] \033[1;37mAdmin Contact \n \033[1;32m[0] \033[1;37mExit ')
                        linex()
                        xd=input('\033[1;32m [=] \033[1;37mCHOSE \033[1;31m:\033[1;32m  ')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;32m [=]\033[1;37m Put file example \033[1;31m:\033[1;32m /sdcard/File.txt ')
                                linex()
                                file = input('\033[1;32m [=]\033[1;37m Put file path\033[1;31m :\033[1;32m ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[1;32m [=]\033[1;37m File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()                                
                                print('\033[1;32m [1]\033[1;37m Method \033[1;31m[\033[1;32mNEW\033[1;31m]  \n\033[1;32m [2]\033[1;37m Method \033[1;31m[\033[1;32mOLD\033[1;31m] \n\033[1;32m [3]\033[1;37m Method \033[1;31m[\033[1;32mOLD\033[1;31m] \n\033[1;32m [4]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m] \n\033[1;32m [5]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m] \n\033[1;32m [6]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m]')
                                linex()
                                mthd=input('\033[1;32m [=]\033[1;37m CHOICE\033[1;31m :\033[1;37m ')
                                clear()                  
                                plist = []
                                print(f'\033[1;32m [=]\033[1;37m Password System');linex();print(f'\033[1;32m [1]\033[1;37m Auto Password Clone \n\033[1;32m [2]\033[1;37m Choice Password Clone ');linex()
                                ppp=input(f'\033[1;32m [=]\033[1;37m CHOICE \033[1;31m:\033[1;37m ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first first')
                                        plist.append('firstfirst')
                                        plist.append('last first')
                                        plist.append('lastfirst')
                                        plist.append('lastlast')
                                        plist.append('last last')
                                        plist.append('firstlast123')
                                        plist.append('firstlast123456')
                                        plist.append('firstlast123789')
                                        plist.append('first12')
                                        plist.append('first123')
                                        plist.append('first123456')
                                        plist.append('first123456789')
                                        plist.append('first 12')
                                        plist.append('first 123')
                                        plist.append('first 123456')
                                        plist.append('first 123456789')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\033[1;32m [=]\033[1;37m PASSWORD LIMIT \033[1;31m: \033[1;32m'))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\033[1;32m [=]\033[1;37m EXAMPLE \033[1;31m:\033[1;32m Firstlast \033[1;31m| \033[1;32mFirst 123\033[1;31m |\033[1;32m First123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;32m [=]\033[1;37m PASSWORD NO {i+1} \033[1;31m:\033[1;32m '))               
                                clear() 
                                print('\033[1;32m [=]\033[1;37m DO YOU WHANT SHOW CP [\033[1;32mY\033[1;37m/\033[1;31mN\033[1;37m] \033[1;31m:\033[1;32m ')
                                linex()
                                cx=input('\033[1;32m [=]\033[1;37m CHOOSE \033[1;31m:\033[1;32m ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;32m [=]\033[1;37m TOTAL FILE IDS \033[1;31m: \033[1;32m'+total_ids+f' ')                                        
                                        print('\033[1;32m [=]\033[1;37m METHOD CHOICE \033[1;31m: \033[1;32mM'+mthd+f' ')
                                        print("\033[1;32m [=]\033[1;37m IF NO RUSLT [\033[1;32mON\033[1;37m/\033[1;31mOFF\033[1;37m] \033[1;37mMODE AVION ")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist   
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)                                                                                                  
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)                                                                                                  
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(api4,ids,names,passlist)                                                                                                  
                                                elif mthd in ['5','05']:
                                                        crack_submit.submit(api5,ids,names,passlist)                                                                                                  
                                                
                                print('\033[1;37m')
                                linex()
                                print('\033[1;32m[=]\033[1;37m The process has completed')
                                print('\033[1;32m[=]\033[1;37m Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python POWER.py')
                        elif xd in ['2','02']:
                                os.system('python crate.py')                     
                        elif xd in ['3','03']:
                                os.system('python ip.py')                     
                        elif xd in ['4','04']:                       
                        	    import chek
                        elif xd in ['5','05']:
                        	    os.system('xdg-open https://t.me/uex_v')
                        elif xd in ['0','00']:
                        	    exit() 
                        
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
#----------------------USER-AGENT--------------------------#
for i in range(100):
        model_build = random.choice(["Samsung", "Kaios", "Realme", "Nokia", "infinix", "Oppo", "Qmobile"])
        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
        fbbv = str(random.randint(10000000, 99999999))
        fbrv = str(random.randint(10000000, 99999999))
        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
        density = random.uniform(1.0, 4.0)
        width = random.randint(720, 1440)
        height = random.randint(1280, 2560)
        network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
        network_carrier = random.choice(network_carriers)
        network_type = random.choice(["WiFi", "4G", "3G"])
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        fbcr = 'null'
        fban = random.choice(["FB4A"])
        fbpn = random.choice(["com.facebook.katana"])
        fbbd = 'lge'
        user_agent = f"\033[1;32m[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/lge;FBBD/{fbbd};FBPN/{fbpn};FBDV/LGE;FBSV/{fbsv};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
print(user_agent)
#----------------------UA--------------------------#
clear()
def generate_custom_user_agent():
    android_versions = ["Android 9", "Android 10", "Android 11", "Android 12"]
    selected_android_version = random.choice(android_versions)

    manufacturers = [
        "TECNO", "Samsung", "Xiaomi", 
       
    ]
    selected_manufacturer = random.choice(manufacturers)

    android_models = {
        "TECNO": ["KE5", "Model2", "Model3"],
        "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52"],
        "Xiaomi": ["Redmi Note 10", "POCO X3"],
        }

    selected_model = random.choice(android_models.get(selected_manufacturer, []))

    device_names = {
        "TECNO": "TecnoDevice",
        "Samsung": "SamsungDevice",
        "Xiaomi": "XiaomiDevice",
       
    }

    device_name = device_names.get(selected_manufacturer, "DefaultDevice")

    build_number = random.randint(1000, 9999)

    app_packages = ["com.facebook.katana", "com.facebook.ocra", "com.facebook.mlite"]
    selected_app_package = random.choice(app_packages)

    density_version = round(random.uniform(1.0, 3.0), 1)
    height_version = random.randint(500, 2000)
    width_version = random.randint(300, 1500)

    user_agent = (
        f"\033[1;32mDalvik/2.1.0 (Linux; U; {selected_android_version} Build/{build_number}; {selected_manufacturer} {selected_model})"
        f" [FBAN/{random.randint(100, 999)}.{random.randint(1, 9)}.{random.randint(0, 9)}.0;FBBV/{random.randint(100000000, 999999999)};FBRV/{random.randint(0, 9)};"
        f"{selected_app_package};FBLC/en_US;FBMF/{selected_manufacturer};FBBD/{selected_manufacturer};FBDV/{selected_model};"
        f"FBSV/{random.randint(8, 12)};FBCA/armeabi-v7a:armeabi;FBDM/{{density={density_version},width={width_version},height={height_version}}};FB_FW/{random.randint(1, 3)};]"
    )

    return user_agent

# Example usage
custom_user_agent = generate_custom_user_agent()
print(custom_user_agent)
#----------------------version--------------------------##DALVIK UA_GENERATE_CODE

#CODE BY MUHAMMAD HAMMAD
# MUGHAL ZADA
import platform
import random

import os
import random
def clear():
    os.system('clear')
    print(logo)
#sys.stdout.write('\x1b]2; MAFIA M16 \x07')
logo=("""\033[1;32m
\033[1;34m================\033[1;34m===========\033[1;34m====================
  \033[1;32m[+]Paid version and modified by Moh 
\033[1;34m================\033[1;34m===========\033[1;34m====================
  \033[1;32m██╗    ██╗██╗████████╗███████╗
  \033[1;32m██║    ██║██║╚══██╔══╝██╔════╝
  \033[1;32m██║ █╗ ██║██║   ██║   █████╗  
  \033[1;32m██║███╗██║██║   ██║   ██╔══╝  
  \033[1;32m╚███╔███╔╝██║   ██║   ███████╗      
  \033[1;32m ╚══╝╚══╝ ╚═╝   ╚═╝   ╚══════╝            
\033[1;34m================\033[1;34m===========\033[1;34m=================
 \033[1;32m[=]\033[1;37m DEVLOPER \033[1;31m: \033[1;32mMOH !               
 \033[1;32m[=]\033[1;37m FACEBOOK \033[1;31m: \033[1;32mMOH !               
 \033[1;32m[=]\033[1;37m STATE \033[1;31m   : \033[1;32mFREE.                   
 \033[1;32m[=]\033[1;37m TIPE\033[1;31m     : \033[1;32mVERESON V/0.0.2        
\033[1;34m================\033[1;34m===========\033[1;34m================""")

def menu():
        try:
                clear()
        
                x = ("sex")
                if x == ("sex"):
                        print(' \033[1;32m[1] \033[1;37mFile cloning\n \033[1;32m[2] \033[1;37mCrate File\n \033[1;32m[3] \033[1;37mUnblock Ip \n \033[1;32m[4] \033[1;37mCheak Apk \n \033[1;32m[5] \033[1;37mAdmin Contact \n \033[1;32m[0] \033[1;37mExit ')
                        linex()
                        xd=input('\033[1;32m [=] \033[1;37mCHOSE \033[1;31m:\033[1;32m  ')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;32m [=]\033[1;37m Put file example \033[1;31m:\033[1;32m /sdcard/File.txt ')
                                linex()
                                file = input('\033[1;32m [=]\033[1;37m Put file path\033[1;31m :\033[1;32m ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[1;32m [=]\033[1;37m File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()                                
                                print('\033[1;32m [1]\033[1;37m Method \033[1;31m[\033[1;32mNEW\033[1;31m]  \n\033[1;32m [2]\033[1;37m Method \033[1;31m[\033[1;32mOLD\033[1;31m] \n\033[1;32m [3]\033[1;37m Method \033[1;31m[\033[1;32mOLD\033[1;31m] \n\033[1;32m [4]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m] \n\033[1;32m [5]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m] \n\033[1;32m [6]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m]')
                                linex()
                                mthd=input('\033[1;32m [=]\033[1;37m CHOICE\033[1;31m :\033[1;37m ')
                                clear()                  
                                plist = []
                                print(f'\033[1;32m [=]\033[1;37m Password System');linex();print(f'\033[1;32m [1]\033[1;37m Auto Password Clone \n\033[1;32m [2]\033[1;37m Choice Password Clone ');linex()
                                ppp=input(f'\033[1;32m [=]\033[1;37m CHOICE \033[1;31m:\033[1;37m ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first first')
                                        plist.append('firstfirst')
                                        plist.append('last first')
                                        plist.append('lastfirst')
                                        plist.append('lastlast')
                                        plist.append('last last')
                                        plist.append('firstlast123')
                                        plist.append('firstlast123456')
                                        plist.append('firstlast123789')
                                        plist.append('first12')
                                        plist.append('first123')
                                        plist.append('first123456')
                                        plist.append('first123456789')
                                        plist.append('first 12')
                                        plist.append('first 123')
                                        plist.append('first 123456')
                                        plist.append('first 123456789')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\033[1;32m [=]\033[1;37m PASSWORD LIMIT \033[1;31m: \033[1;32m'))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\033[1;32m [=]\033[1;37m EXAMPLE \033[1;31m:\033[1;32m Firstlast \033[1;31m| \033[1;32mFirst 123\033[1;31m |\033[1;32m First123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;32m [=]\033[1;37m PASSWORD NO {i+1} \033[1;31m:\033[1;32m '))               
                                clear() 
                                print('\033[1;32m [=]\033[1;37m DO YOU WHANT SHOW CP [\033[1;32mY\033[1;37m/\033[1;31mN\033[1;37m] \033[1;31m:\033[1;32m ')
                                linex()
                                cx=input('\033[1;32m [=]\033[1;37m CHOOSE \033[1;31m:\033[1;32m ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;32m [=]\033[1;37m TOTAL FILE IDS \033[1;31m: \033[1;32m'+total_ids+f' ')                                        
                                        print('\033[1;32m [=]\033[1;37m METHOD CHOICE \033[1;31m: \033[1;32mM'+mthd+f' ')
                                        print("\033[1;32m [=]\033[1;37m IF NO RUSLT [\033[1;32mON\033[1;37m/\033[1;31mOFF\033[1;37m] \033[1;37mMODE AVION ")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist   
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)                                                                                                  
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)                                                                                                  
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(api4,ids,names,passlist)                                                                                                  
                                                elif mthd in ['5','05']:
                                                        crack_submit.submit(api5,ids,names,passlist)                                                                                                  
                                                
                                print('\033[1;37m')
                                linex()
                                print('\033[1;32m[=]\033[1;37m The process has completed')
                                print('\033[1;32m[=]\033[1;37m Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python POWER.py')
                        elif xd in ['2','02']:
                                os.system('python crate.py')                     
                        elif xd in ['3','03']:
                                os.system('python ip.py')                     
                        elif xd in ['4','04']:                       
                        	    import chek
                        elif xd in ['5','05']:
                        	    os.system('xdg-open https://t.me/uex_v')
                        elif xd in ['0','00']:
                        	    exit() 
                        
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
#----------------------USER-AGENT--------------------------#
for i in range(100):
        model_build = random.choice(["Samsung", "Kaios", "Realme", "Nokia", "infinix", "Oppo", "Qmobile"])
        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
        fbbv = str(random.randint(10000000, 99999999))
        fbrv = str(random.randint(10000000, 99999999))
        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
        density = random.uniform(1.0, 4.0)
        width = random.randint(720, 1440)
        height = random.randint(1280, 2560)
        network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
        network_carrier = random.choice(network_carriers)
        network_type = random.choice(["WiFi", "4G", "3G"])
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        fbcr = 'null'
        fban = random.choice(["FB4A"])
        fbpn = random.choice(["com.facebook.katana"])
        fbbd = 'lge'
        user_agent = f"\033[1;32m[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/lge;FBBD/{fbbd};FBPN/{fbpn};FBDV/LGE;FBSV/{fbsv};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
print(user_agent)
#----------------------UA--------------------------#
clear()
def generate_custom_user_agent():
    android_versions = ["Android 9", "Android 10", "Android 11", "Android 12"]
    selected_android_version = random.choice(android_versions)

    manufacturers = [
        "TECNO", "Samsung", "Xiaomi", 
       
    ]
    selected_manufacturer = random.choice(manufacturers)

    android_models = {
        "TECNO": ["KE5", "Model2", "Model3"],
        "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52"],
        "Xiaomi": ["Redmi Note 10", "POCO X3"],
        }

    selected_model = random.choice(android_models.get(selected_manufacturer, []))

    device_names = {
        "TECNO": "TecnoDevice",
        "Samsung": "SamsungDevice",
        "Xiaomi": "XiaomiDevice",
       
    }

    device_name = device_names.get(selected_manufacturer, "DefaultDevice")

    build_number = random.randint(1000, 9999)

    app_packages = ["com.facebook.katana", "com.facebook.ocra", "com.facebook.mlite"]
    selected_app_package = random.choice(app_packages)

    density_version = round(random.uniform(1.0, 3.0), 1)
    height_version = random.randint(500, 2000)
    width_version = random.randint(300, 1500)

    user_agent = (
        f"\033[1;32mDalvik/2.1.0 (Linux; U; {selected_android_version} Build/{build_number}; {selected_manufacturer} {selected_model})"
        f" [FBAN/{random.randint(100, 999)}.{random.randint(1, 9)}.{random.randint(0, 9)}.0;FBBV/{random.randint(100000000, 999999999)};FBRV/{random.randint(0, 9)};"
        f"{selected_app_package};FBLC/en_US;FBMF/{selected_manufacturer};FBBD/{selected_manufacturer};FBDV/{selected_model};"
        f"FBSV/{random.randint(8, 12)};FBCA/armeabi-v7a:armeabi;FBDM/{{density={density_version},width={width_version},height={height_version}}};FB_FW/{random.randint(1, 3)};]"
    )

    return user_agent

# Example usage
custom_user_agent = generate_custom_user_agent()
print(custom_user_agent)
#----------------------version--------------------------#
