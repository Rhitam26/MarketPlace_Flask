
from typing import Collection

import bcrypt

from market import mongo 

class Users():
    def __init__(self, username, email, password):
        self.username= username
        self.email= email
        self.password= password
        password1=str(self.password)
        print(self.password)
        bytesOfPassowrd= password1.encode('utf-8')
        db = mongo["DbUsers"]
        collection= db['users']
        self.salt= bcrypt.gensalt()
        collection.insert_one({'username':username, 'email':email, 'passwordhash':bcrypt.hashpw(bytesOfPassowrd, self.salt)})

        @property
        def password(self):
            return self.password1
        
        @password.setter
        def password(self, plainTextPassword):
            bytesOfPassword= plainTextPassword.encode('utf-8')
            self.password_hash = bcrypt.hashpw(bytesOfPassword, self.salt)

    
    def check_pasword_correction(self, attempedPassword):
        return bcrypt.checkpw(self.password_hash,attempedPassword)






