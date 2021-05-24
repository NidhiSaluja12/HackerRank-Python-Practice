def Second_Lowest_Score(scores):
    output_names = []
    score_len = len(scores)
    lowest = second_lowest = float('inf')
    
    for i in range (score_len):
        lowest = min(lowest, scores[i])
        
    
        
    for i in range (score_len):
        if lowest != scores[i]:
           if second_lowest > scores[i]:
                second_lowest = scores[i]
                
    for i in range (score_len):
        if second_lowest == scores[i]:
            output_names.append(names[i])
            
    output_names.sort()
    for name in output_names:
        print(name)
            
        
    
    
L = []
scores = []
names = []
if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        L.append([name, score])
        scores.append(score)
        names.append(name)
        
result = Second_Lowest_Score(scores)


