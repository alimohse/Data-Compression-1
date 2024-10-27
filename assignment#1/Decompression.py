def decompression( compressedData ):
    decompressedData =""
    for tag in compressedData:
        pos = tag[0]
        length = tag[1]
        nextChar= tag[2]
        if pos >0:
            size = len(decompressedData)
            decompressedData += decompressedData[size - pos : size - pos + length]
        decompressedData += nextChar
    return decompressedData

list = [ [0, 0, 'A'] , [0, 0, 'B'], [2, 2, 'B'], [5, 3, ' '] ]
originalData = decompression(list)
print(originalData)


