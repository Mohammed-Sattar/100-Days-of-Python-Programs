class User:
    def __init__(self, user_id, username):         # the self is the object that is being initialized 
        # I can also add as many parameters as required, these parameters will passed in when the object is initialized
        # when arguments have been passed to the parameters, they can be used to set the objects attributes
        # once parameters have been created in the init function, initializing an object requires arguments to be passed, otherwise error
        
        self.id = user_id
        self.name = username
        self.followers = 0      # creating an attribute with default value 0
        self.following = 0
        print("Creating a new user ...")

    def follow(self, user):        # when creating a function in a class, it all requires the self parameter to know which object 
                                    # is calling it  
        user.followers += 1
        self.following += 1

user_1 = User("000", "Papa")

# print(user_1.name)
# print(user_1.followers)

user_2 = User("001", "Yusuf")

user_1.follow(user_2)
print(f"{user_1.name}:")
print(user_1.followers)
print(user_1.following)
print(f"{user_2.name}:")
print(user_2.followers)
print(user_2.following)
