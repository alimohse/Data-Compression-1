def decompression( compressedData ):
    decompressedData =""
    for tag in compressedData:
        pos = tag[0]
        length = tag[1]
        nextChar= tag[2]
        if pos > 0:
            size = len(decompressedData)
            decompressedData += decompressedData[size - pos : size - pos + length]
        if nextChar!="Null":
            decompressedData += nextChar
    return decompressedData
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
        next_char = "Null"
        searchWindow = []
        startIndex = max(0, position - searchWindowSize)
        
        for i in range(startIndex, position):#start from startIdnex and ends at position
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
        if length < len(lookAheadWindow):
            next_char = lookAheadWindow[length]
        
        tags.append((start, length, next_char))
        
        position += length + 1
    
    return tags

print("Enter search window size:")
searchWindowSize=int(input()) 
print("Enter Look ahead window size:")
lookAheadWindowSize=int(input())
tags = LZ77(searchWindowSize, lookAheadWindowSize, s="ABAABABAABBBBBBBBBBBBA")
print("tags:")
print(tags)
print("decompressing...")
print(decompression(tags))
