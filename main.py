#!/usr/bin/env python
import yaml
import sys
import time


print('inserisci label:')
labelinput = input()
print('inserisci username:')
usernameinput = input()
print('inserisci password:')
passwordinput= input()
print('inserisci note:')
noteinput = input()



New = {'Details':{
   'id':  time.ctime(),
     'label' : labelinput,
     'username' :usernameinput,
     'password' : passwordinput,
     'note': noteinput,
     }

}






with open("data.yml", 'a') as yamlfile:
    data = yaml.dump(New, yamlfile)
    print("Write successful")


with open(r'data.yml') as file:

    base = yaml.load(file, Loader=yaml.FullLoader)

    print(base)
