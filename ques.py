import json

with open('user.json',"r") as data_file:    

    data = json.load(data_file)


users = data['users']


for user in data:

  counter = 0

#   print ("users full name is"  + users['firstName'] + ' ' + users['lastName'])

  while counter < len(users):

    print (["user"]["details"][counter]["age"])

    # print ( user['details'][counter])
#
    # print ("users city is " + user['details'][counter]['city'])