#this functions checks if two strings are similar
#wild card is implemented in this function
def match(a, b):
    if(len(a) != len(b)):
        return False;
    else:
        for i in range(0, len(a)):
            if(a[i] != b[i] and b[i] != '_'):
                return False;
    
    return True;


#this function searches for all the locations in T where P occurs and returns all those locations in a list
def search(T, P):
    found = [];

    i = 0;

    while(i <= len(T)-len(P)):
        subString = T[i:i+len(P)];

        if(match(subString, P)):
            found.append(i);

        i += 1;

    return found;


#Test cases
print(search("xyzCATpqr", "CAT"));
print(search("xyzCATpqr", "C_T"));

print(search("cogwrgaccag", "cog"));    #at the beginning
print(search("cogwrgaccag", "cag"));    #at the end
print(search("cogwrgaccag", "c_g"));    #both at the beginning and at the end
print(search("cogwrgaccag", "c__g"));   #ccag at the end


print(search("cogwrgaccag", "pqr"));    #not found. empty list
print(search("cogwrgaccag", "p_r"));    #not found. empty list


print(search("cogwrgaccag", ""));       #empty character is found everywhere
print(search("", ""));                  #empty character is only at the beginning of another empty character
print(search("", "abc"));               #not found


print(search("winter is coming", "_ _")); #spaces

print(search("Hello World", "_"));      #every character is _