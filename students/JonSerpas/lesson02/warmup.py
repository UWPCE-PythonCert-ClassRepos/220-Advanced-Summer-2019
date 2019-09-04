# Create a a dict with info about you (name, occ, email, phone)
# Write that dict to a file somewhere on the local machine

about_me = {'name': 'Jon',
            'age': '36',
            'occupation': 'sec engr',
            'eyes': 'blue'}

with open('about_me_file.txt', 'w+') as file:
    for k, v in about_me.items():
        file.write("{} {}\n".format(k, v))
    file.close()
