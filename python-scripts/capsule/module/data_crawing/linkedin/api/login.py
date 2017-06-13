# -*- coding: utf-8 -*-

''''' 
Created on 2014-8-16 
@author: guaguastd 
@name: login.py 
'''

# twitter login
def linkedin_login():
    import linkedin
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    USER_TOKEN = ''
    USER_SECRET = ''

    RETURN_URL = ''  # developer does not need this

    # Instantiate the developer authentication class
    auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
        USER_TOKEN, USER_SECRET, RETURN_URL, permissions=linkedin.PERMISSIONS.enums.values())
    linkedin_api = linkedin.LinkedInApplication(auth)

    return linkedin_api
