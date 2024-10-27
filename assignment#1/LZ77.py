def LZ77(searchWindowSize, lookAheadWindowSize, s):
    tags = []
    position = 0
    searchWindow = ""
    while position < len(s):
        lookAheadWindow = []
        for i in range(lookAheadWindowSize):
            if position + i < len(s):
                lookAheadWindow.append(s[position + i])
                
                
        length = 0
        start = 0
        next_char = ""
        
        if lookAheadWindow:
            next_char = lookAheadWindow[0]
            
        searchWindow = []
        startIndex = max(0, position - searchWindowSize)
        
        for i in range(startIndex, position):#start from startInex and ends at position
            searchWindow.append(s[i])
            
        for i in range(len(searchWindow)):
            maxMatchedlength = 0
            temp_position = 0  
            j = i  
            flag  =False 
            
            while (temp_position < len(lookAheadWindow) and 
                   j < len(searchWindow) and  
                   lookAheadWindow[temp_position] == searchWindow[j]):
                maxMatchedlength += 1
                flag = True
                temp_position += 1
                j += 1

            if maxMatchedlength >= length and flag:
                length = maxMatchedlength
                start = len(searchWindow) - i

        if length > 0 and length < len(lookAheadWindow):
            next_char = lookAheadWindow[length]
        
        tags.append((start, length, next_char))
        
        position += length + 1
    
    return tags


tags = LZ77(searchWindowSize=10, lookAheadWindowSize=5, s="ABAABABAABBBBBBBBBBBBA")
print(tags)
