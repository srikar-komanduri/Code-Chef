T=int(input())



for _ in range(T):
    scores=[]
    n=int(input())
    
    goals=list(map(int,input().split()))
    fouls=list(map(int,input().split()))
    #print(goals,fouls)
    #calculating scores
    for i in range(n):
        points=0
        temp=goals[i]*20-fouls[i]*10
        if temp>0:
            points+=temp
        else:
            points=0
        scores.append(points)
    print(max(scores))
        
    
        
        
    
        
