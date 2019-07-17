import json
if __name__ == "__main__":
    me = {'name': 'Arch', 'occupation': 'student', 'email':'archwu0817@gmail.com', 
    'phone': 'xxx-xxx-8763', 'hobbies':['soccer', 'gaming']}
    
    with open('file', 'w') as a:
        a.write(str(me))
    with open('me.json', 'w') as file:
        json.dump(me, file)