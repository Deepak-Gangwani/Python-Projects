import pywhatkit
print("----------Welcome Automatic Message Sender System----------- ")

def start():
    try:
        num=input("press 'c' to continue or 'q' to quit---> ")
        for i in num:
            if i=='c':
                continue
            if i=='q':
                exit()
            else:
                print("You have entered wrong key plz write key again")
                return start()
        number=input("Enter the number whom you want to send the message-->")
        msg=input("Enter the message you want to send-->")
        hour=int(input("Enter the hour time in 24 form-->"))
        minute=int(input("Enter the minute-->")) 
        pywhatkit.sendwhatmsg(f"+91 {number}",f"{msg}",hour,minute)       
    except Exception as e:
        print(e)

start()
#pywhatkit.sendwhatmsg("+91 7414804516","Hello mom how are you",20,14)