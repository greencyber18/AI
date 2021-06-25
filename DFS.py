
def dfs(start, goal, adList):        
    frontier = [start]      #Start with a frontier that contains the initial state.
    exploredSet = []      #Start with an empty explored set.
    nodeInfo = {start: {"parent": "", "pathCost": 0}}
    
    
    print("\nSearching Sequence: ",end="")
    while True:  #Repeat
        if len(frontier) == 0:    #If the frontier is empty, then no solution.
            print("No Solution!")
            return 
        
        node = frontier.pop()    #Remove a node from the frontier.
        print(node,end=" --> ")
        
        if node == goal:         #If node contains goal state, print the solution.
            print("\n\nSolution Path: ",end = "");
            slnPath = []
            n = goal
            while(n!=""):
                slnPath.append(n)
                n = nodeInfo[n]["parent"]
            
            
            while(len(slnPath) != 0):        #Using Stack for Reverese Order Printing
                print(slnPath.pop(), end ="-->")
                
            return
        
        exploredSet.append(node) #Add the node to the explored set.
        
        for item in adList[node]: #Expand node 
            if item not in frontier and item not in exploredSet: #add resulting nodes to the frontier, 
                frontier.append(item)                            #if they  aren't already in the frontier or the explored set.
                nodeInfo[item] = {"parent": node}
                
    

        
        
                 
            
                 
#****************END of DFS Function***************************


adjacencyList = {'a': {'b': 1 , 'f':2},
                 'b': {'c': 1,'d': 5,'a':1},
                 'c': {'e': 5},
                 'd': {'f': 3},
                 'e': {},
                 'f':{'a': 10}}


'''
adjacencyList = {'a': {'b': 3, 'e': 5},
                 'b': {'c': 8,'d': 5,'e': 3},
                 'c': {},
                 'd': {'c': 2},
                 'e': {'d': 4}}
'''


dfs('a','e',adjacencyList)