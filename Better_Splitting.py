def split_string(source,splitlist):
    output = []
    atsplit = True 
    for char in source: 
        if char in splitlist:
            atsplit = True 
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1] + char
    return output

out = split_string("http://this.domain.com/here/there/everywhere.html","/")
print out
