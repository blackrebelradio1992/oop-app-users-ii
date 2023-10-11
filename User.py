# your improved User class goes here# your User class goes here
class User:
    def __init__(self, userName, email, phoneNumber, city):
        self.userName = userName
        self.email = email
        self.phoneNumber = phoneNumber
        self.city = city
        self.post = [] 

    def __str__(self):
        return f"Your Username is {self.userName}, your email is {self.email}, Phone number is {self.phoneNumber} and your city is {self.city}"
    

    def create_post(self, title, message):
        post ={title: message}
        self.post.append(post)
    
    # def create_new_post(self):
    #     title = input("whats the post tile")
    #     message = input("type your post")
    #     post ={title: message}
    #     self.post.append(post)





jake = User("jake39", "jake39@mail.com", "312-123-4567",'Thunderdome')

john = User("jj45on", "johnDaDon@mail.com", 123-456-7890, "Valhalla")

print(jake)
print(john)

# Wow!  Literally overnight, your \<INSERT APPLICATION NAME\> app has really taken off!  You decide to add a new feature to your app: posts.

# In order to gain this new functionality, you'll have to modify your original `User` class.

# ## Requirements
# 1. Add a method to your `User` class that allows for creating a new user post.
# 2. Add any necessary instance properties to make step 1 work.  What data structure should you use?
# 3. Add a static variable that stores the posts from every user.  What data structure should you use?
# 4. Make sure that the the information stays in sync!

# ## Bonus
# Add a method that allows for deleting a post.  Again, make sure that your information stays in sync.
