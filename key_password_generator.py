import random
import string

def beautiful_print(key_pass):
    row = len(key_pass)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+key_pass+"|"'\n' + h
    print(result)
 
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
        
