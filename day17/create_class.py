class user:
    def __init__(self,id,username):
        self.id=id
        self.username=username
        self.follower=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        self.following+=1
        
user1=user("001","angela")
user2=user("002","jack")
user2.follow(user1)
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)
