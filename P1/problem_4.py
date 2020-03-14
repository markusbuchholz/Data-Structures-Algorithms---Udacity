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



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    db_groups = group.get_groups()
  
    flag = False

    if user in group.get_users():
         return True

    for i in group.get_groups():
 
        
        if user in i.get_users():
 
            return True
        else:
            for j in i.get_groups():
                if j is not None:
                    test = is_user_in_group(user, j)

                    if test:
                        return True

    return None




if __name__ == '__main__':


    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    def test_1 ():# Normal Case:
        print('*************************************')
        print(is_user_in_group('parent_user', parent))
        # None
        print(is_user_in_group('child_user', parent))
        # None
        print(is_user_in_group('sub_child_user', parent))
        # True

    def test_2 ():# Edge Case 1:
        print('*************************************')
        print(is_user_in_group('', parent))
        # None
        print(is_user_in_group('', child))
    
    def test_3 ():# Edge Case 2:
        print('*************************************')
        print(is_user_in_group('user1', parent))
        #None
        print(is_user_in_group('user1', child))
        #None
 

    test_1()
    test_2()
    test_3()









