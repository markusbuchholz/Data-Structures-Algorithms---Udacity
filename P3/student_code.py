#https://www.youtube.com/watch?v=eSOJ3ARN5FM&t=842s
#https://en.wikipedia.org/wiki/A*_search_algorithm

import numpy as np

class Vertex(object):


    def __init__(self, origin=None, position=None):
        self.origin = origin
        self.position = position
        
        self.f = 0
        self.g = 0
        self.h = 0
        
def calculate_distance(pos_1, pos_2):

    
    x1 = pos_1[0]
    y1 = pos_1[1]
    x2 = pos_2[0]
    y2 = pos_2[1]

   
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    return np.sqrt(delta_x**2 + delta_y**2)


def check_path(current_vertex, goal):
    shortest_path = []
    if current_vertex.position == goal:
        
        current = current_vertex
        while current is not None:
            shortest_path.insert(0,current.position)
            current = current.origin
        return shortest_path 
    
    return None


def find_k_min(open_list):
    
    value_min = 0
    k_min = ''
    
    for key in open_list.keys():
        if k_min == '':
            k_min = key
            value_min = open_list[k_min].f
        if open_list[key].f < value_min:
            value_min = open_list[key].f
            k_min = key

    return k_min



def shortest_path(M,start,goal):

    start_vertex = Vertex(None, start)
    start_vertex.g = 0
    start_vertex.h = 0
    start_vertex.f = 0
   
    end_vertex = Vertex(None, goal)
    end_vertex.g = 0 
    end_vertex.h = 0 
    end_vertex.f = 0

    open_list = dict()
    closed_list = set()

    open_list[start_vertex.position] = start_vertex
    
    #** WIKI:
    #** while openSet is not empty
    while len(open_list) > 0:
        

        #** current := the vertex in openSet having the lowest fScore[] value
        k_min = find_k_min(open_list)
        current_vertex = open_list[k_min]
        
        #** if current = goal
        #** return check_path(cameFrom, current)
        shortest_path = check_path(current_vertex, end_vertex.position)
        if shortest_path:
            return shortest_path
        
        #** closeSet.add(current)
        #** openSet.Remove(current)
        del open_list[current_vertex.position]
        closed_list.add(current_vertex.position)
    
        #** openSet.Remove(current)
        #**for each neighbor of current
        #**    // d(current,neighbor) is the weight of the edge from current to neighbor
        #**    // tentative_gScore is the distance from start to the neighbor through current
        #**    tentative_gScore := gScore[current] + d(current, neighbor)
        #**    if tentative_gScore < gScore[neighbor]
        #**        // This path to neighbor is better than any previous one. Record it!
        #**        cameFrom[neighbor] := current
        #**        gScore[neighbor] := tentative_gScore
        #**        fScore[neighbor] := gScore[neighbor] + h(neighbor)
        #**        if neighbor not in closeSet
        #**            openSet.add(neighbor)
        

        
        for neighbor in M.roads[current_vertex.position]: 

            neighbor_vertex = Vertex(current_vertex, neighbor)
            #do not analyse neighbor if on closed list
            if neighbor_vertex.position in closed_list:
                continue # return to beginning (top of loop) 
                    
            neighbor_vertex.g = current_vertex.g + calculate_distance(M.intersections[current_vertex.position], M.intersections[neighbor_vertex.position])
            neighbor_vertex.h = calculate_distance(M.intersections[neighbor_vertex.position], M.intersections[end_vertex.position])
            neighbor_vertex.f = neighbor_vertex.g + neighbor_vertex.h
            
            #check if new computed value is lower than existing. If so update  
            if neighbor_vertex.position in open_list:
                if neighbor_vertex.g > open_list[neighbor_vertex.position].g :
                    continue #go on the top because the new value is higher the existing - no update for this vertex

            open_list[neighbor_vertex.position]= neighbor_vertex # update

        
    return 