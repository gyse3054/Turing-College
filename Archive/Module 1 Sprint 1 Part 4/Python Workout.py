

def passwd_to_dict(file):
    users = {}
    with open(file) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):     
                user_info = line.split(':')          
                users[user_info[0]] = int(user_info[2])
    return users
 
print(passwd_to_dict('passwd.txt'))