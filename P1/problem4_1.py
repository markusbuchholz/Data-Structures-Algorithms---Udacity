class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


########################
def is_user_in_group2(user, group):

    if user in group.get_users():  # User found
        return True
    else:
        if len(group.get_groups()) == 0:  # Keep searching
            return False
        else:
            for sub_group in group.get_groups():
                found = is_user_in_group(user, sub_group)

                if found:
                    return True
    return False



#######################





def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
   # db = Group(parent)
    #db_groups = []
    db_groups = group.get_groups()
    #print(db_groups)
    flag = False

    if user in group.get_users():
         return True

    for i in group.get_groups():
        #print(i.name)
        
        if user in i.get_users():
            #print("ok")
    #         flag = True
            return True
        else:
            for j in i.get_groups():
                if j is not None:
                    test = is_user_in_group(user, j)

                    if test:
                        return True

    return None

    #         while i is not None:
    #             for j in j.get_groups():
    #                 is_user_in_group(user,j)
    
    # return False





        #if flag == True:
         #   break

          



    # for j in group.get_groups():
    #     print(i.name)
    #     for jj in range(len(ii)):
    #         if user in jj.get_users():
    #             print ("ok2")
    #             return True
    #         else: 
    #             is_user_in_group(user, ii)

    # return False

# Testing preparation
# Testing preparation
# Normal Cases:
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Normal Cases:
print('Normal cases:')
print(is_user_in_group('parent_user', parent))
# False
print(is_user_in_group('child_user', parent))
# False
print(is_user_in_group('sub_child_user', parent))
# True

# Edge Cases:
print('Edge cases:')
print(is_user_in_group('', parent))
# False
print(is_user_in_group('', child))
# False









# True
# True

# # Edge Cases:
# print('Edge Cases:')
# print(is_user_in_group(user='', group=parent))
# # False
# print(is_user_in_group(user='', group=child))
# # False



# parent = Group("parent")
# child = Group("child")
# child1 = Group("child1")
# child2 = Group("child2")
# child3 = Group("child3")
# sub_child = Group("subchild")

# sub_child_user = "sub_child_user"
# sub_child.add_user(sub_child_user)

# child.add_group(sub_child)
# parent.add_group(child)
# parent.add_group(child1)
# parent.add_group(child2)
# parent.add_group(child3)

# parent.add_user('user1')

# is_user_in_group('user1', parent)

