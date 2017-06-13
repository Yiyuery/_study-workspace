# -*- coding: utf-8 -*-

''''' 
Created on 2014-8-16 
@author: guaguastd 
rm@name: user_profile_get.py 
'''

# import login
import login
# import json
import json

# access to linkedin api
linkedin_api = login.linkedin_login()

# use api to access user profile
profiles = linkedin_api.get_profile()

# print the profiles
print(json.dumps(profiles, indent=1))
