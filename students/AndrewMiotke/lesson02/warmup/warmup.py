import json

person_dictionary = {"name": "Andrew",
                     "occupation": "IT Support Specalist",
                     "email": "email@gmail.com",
                     "phone": 1112223333,
                     "hobbies": "programming",
        }


with open("file.json", "w") as file:
    file.write(str(person_dictionary))
