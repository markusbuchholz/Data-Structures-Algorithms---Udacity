# A RouteTrie will store our routes and their associated handlers

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.

import os

class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.is_path = False
        self.handler = handler
        self.children = {}

    def insert(self, partpath):
        # Insert the node as before
        self.children[partpath] = RouteTrieNode()


class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.handler = None
        self.root = RouteTrieNode(self.handler)
        

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for partpath in path:
            if partpath not in current_node.children:
                current_node.children[partpath] = RouteTrieNode(self.handler)
            current_node = current_node.children[partpath]
        
        current_node.is_path = True
        #current_node.is_handler = True 
        current_node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for partpath in path:
            #print("1----")
            if partpath in current_node.children:
                current_node = current_node.children[partpath]
            else:
                return None
                
            #else:
             #   print("2----")
              #  return None
        
        return current_node.handler



# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        #self.routerName = routerName
        self.routes = RouteTrie()
        self.handler = handler
        self.routes.insert("/", self.handler)
        

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(route)
        self.routes.insert(path, handler)



    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(route)
        handler = self.routes.find(path)
        return handler

    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions
        # so it should be placed in a function here
        part_ret = []
        partpath = route.split('/')
        for ijk in partpath:
            if ijk != '':
                part_ret.append(ijk)

        return part_ret




    def split_path2(self, route):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        router_path = route.split("/")
        return router_path



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") #, "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one