import json

with open('emails.json', 'r') as file:
    data = json.load(file)

for entry in data:
    email, flag = entry.split(';')
    if flag == '1':
        
        with open('emails_1.txt', 'a') as file1:  
            file1.write(email + '\n')
    elif flag == '0':
        
        with open('emails_0.txt', 'a') as file0:  
            file0.write(email + '\n')
    else:
        print(f"Invalid flag value '{flag}' for email: {email}")
