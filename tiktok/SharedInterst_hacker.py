from collections import defaultdict

def maxTokens(friends_nodes, friends_from, friends_to, friends_weight):
    # assigning set of friend_nodes to their shared weights
    #   Wieghts      nodes
    #     1         {1,2,3}  
    #     2         {1,2}
    #     3         {2,3,4}
    weights = defaultdict(set)
    for i in range(len(friends_from)):
        weights[friends_weight[i]].add(friends_from[i])
        weights[friends_weight[i]].add(friends_to[i])
    # print(weights)
    # make set of pairs for each weight 
    #    Wieghts      nodes
    #      1         (1,2),(2,3),(1,3)  
    #      2         (1,2)
    #      3         (2,3),(3,4),(2,4)
    # count no of pairs 
    # {(1,2):2, (2,3): 2, (1,3):1, (3,4):1, (2,4):1}
    
    count = defaultdict(int)
    for key, val in weights.items():
        for foo in list(itertools.combinations(val, 2)):
            count[foo]+=1 
        
    # print(count)
    for num in sorted(set
(count.values()), reverse=True):
        # print(num, )
        pairs = [k for k,v in count.items() if v == num]
        if len(pairs) >= 2:
            return max([a*b for a, b in pairs])
        

friends_nodes=4
friends_from =  [1, 1, 2, 2, 2]
friends_to =   [2, 2, 3, 3, 4]
friends_weight =  [1, 2, 1, 3, 3 ]

print(maxTokens(friends_nodes, friends_from, friends_to, friends_weight))
