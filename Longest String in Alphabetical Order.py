alphabet = "abcdefghijklmnopqrstuvwxyz"
s = "sdfdsfsdfs"
outputx = ''
length = len(s)
greatest_length = 0
for i in range(length):
    output = s[i]
    for b in range (i+1, length):
        if alphabet.index(s[b]) >= alphabet.index(s[b-1]):
            output += s[b]
            if len(output) > greatest_length:
                greatest_length = len(output)
                outputx = output
        elif i == 0 and alphabet.index(s[b]) < alphabet.index(s[b-1]):
            outputx = output
            break
        elif alphabet.index(s[b]) < alphabet.index(s[b-1]):
            break
print ("Longest string in alphabetical order is: " + outputx)




