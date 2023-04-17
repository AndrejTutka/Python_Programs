def accept_login(users: dict,username: str,password: str) -> bool:
    if username in users:
        if password == users[username]:
            return True
        
    return False
    
    
    
users = {

  "user1" : "password1",

  "user2" : "password2",

  "user3" : "password3"

}



if accept_login(users, "user1", "password1") :

  print("login successful!")

else :

  print("login failed...")

