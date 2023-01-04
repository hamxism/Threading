#200901019

import threading

def Input_Thread():
    global i
    try:
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        i = input("Input one or more characters to form a string: ")
    except:
        print("Error occured in Input thread! Please try again.")
    
def Reverse_Thread():
    try:
        print("-----------------------------------------------------")
        print("Desired string after reverse thread: ", i[::-1])
    except:
        print("Error occured in Reverse thread! Please try again.")

def Capital_Thread():
     try:
         print("-----------------------------------------------------")
         print("Capitalized string: ", i.upper())
     except:
         print("Error occured in Capital thread! Please try again.")


def Shift_Thread():
    try:
        print("-----------------------------------------------------")
        new_string = ""
        for alphabets in i:
            new_string += chr(ord(alphabets) + 2)
            print("Shifted string: ", new_string)
    except:
            print("Error occured in Shift thread! Please try again.")
        

thread1 = threading.Thread(target=Input_Thread)
thread2 = threading.Thread(target=Reverse_Thread)
thread3 = threading.Thread(target=Capital_Thread)
thread4 = threading.Thread(target=Shift_Thread)


thread1.start()
thread1.join()


thread2.start()
thread3.start()
thread4.start()


thread2.join()
thread3.join()
thread4.join()