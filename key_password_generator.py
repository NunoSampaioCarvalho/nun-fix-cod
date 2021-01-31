import random
import string
import re
import smtplib
import json


def send_mail(user,pass_generated):
    
    port=587
    smtp_server='smtp.gmail.com'
    message=pass_generated
    file=open('info.json')
    data=json.load(file)  # Load json file with your info 
    sender_email = data['Email']
    password=data['Password']
    receiver_email=user
    
    with smtplib.SMTP(smtp_server,port) as smtp:
        
        smtp.starttls()
        smtp.login(sender_email,password)
        smtp.sendmail(sender_email, receiver_email, message)
  

def validate_mail(mail):
    
    check= False
    regex ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex,mail)):
        check=True
    return check

def validate_response(user_input,result):
   
    negative_vals=["No","no","on","nO","oN","NO","ON"]
    if(user_input in negative_vals):
        print("Okay bye")
    else:
        if(validate_mail(user_input)==True):
            print("Your email %s was validated \n " %user_input)
            send_mail(user_input,result)
        else:
            print("Sorry we cannot understand can you repeate please ? ") 
            answer=input()
            validate_response(answer,result)
               
def beautiful_print(key_pass):
    
    row = len(key_pass)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+key_pass+"|"'\n' + h
    print("The passord was generated: ")
    print(result)
    print("If you want to send this password to your mail adress, please insert bellow, else insert No.")
    cond=input()
    validate_response(cond,key_pass)
        

def sub_array_to_array(arr): # pass all subarrays to an array
    final_arr=[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            final_arr.append(arr[i][j])        
    return final_arr

def key_pass_generator(letters_lower,letters_upper,numbers):
    
    num_rand=random.randint(0,100)
    
    key_pass=[]
    final_str=" "
    key_pass.append(random.choices(letters_lower,weights=None,k=num_rand))
    key_pass.append(random.choices(letters_upper,weights=None,k=num_rand))
    key_pass.append(random.choices(numbers,weights=None,k=num_rand))
    key_pass=sub_array_to_array(key_pass)
    
    if (len(key_pass)>16 or len(key_pass)<8):
        return key_pass_generator(letters_lower,letters_upper,numbers)
    
    random.shuffle(key_pass)
    return final_str.join(key_pass).replace(" ", "")
    
def main():

    letters_lower=string.ascii_lowercase
    letters_upper=string.ascii_uppercase
    nums=string.digits
    key_pass=key_pass_generator(letters_lower,letters_upper,nums)
    beautiful_print(key_pass)

if __name__ == "__main__":
    main()      
        
