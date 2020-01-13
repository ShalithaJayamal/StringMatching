Dict = {'A':2, 'C':3, 'T':5, 'G':7};

#############################################################################################################
# Rabin Carp search
def search(T, P): #T is the text and P is the pattern
    #calculate hash value of the pattern first
    pHash = 1; #this is the hash value of the pattern



    n = 1; #power
    for c in P:
        pHash *= Dict[c]**n;
        n+=1;





    #first sub string
    subString = [];
    for i in range (0, len(P)):
        subString.append(T[i]);
    

    #calculating sub string hash for the first time
    subStringHash = 1; #this is the hash of the chosen substring
    subStringHash_ = 1; #this will be used to calculate the hash in next step. More information is in read me file
    n = 1;
    for c in subString:
        subStringHash *= Dict[c]**n;
        n += 1;

        subStringHash_ *= Dict[c]; #why this second hash is in read me file
    





    #checking if pattern is found in the very beginning
    if(pHash == subStringHash): #found
        return 0;







    #sub string's beginning and end indices
    a = 0;
    b = len(P);

    end = len(T)-1;
    while(b<=end):
        c = subString.pop(0);
        subString.append(T[b]);

        

        subStringHash = (subStringHash//subStringHash_)*(Dict[T[b]]**len(P));
        subStringHash_ = (subStringHash_//Dict[c])*Dict[T[b]];

        if(subStringHash == pHash): #found
            return b-len(P)+1;
        
        b += 1;
    
    #coming here means not found
    return -1;
#############################################################################################################

















Q = open("Query Database.txt", "r");
qLine = Q.readline().replace('\n', '');

while(">EOF" not in qLine and len(qLine) > 0):
    
    if(qLine[0] == '>'): #description line
        qDescription = qLine[1: len(qLine)];
        
        

        #now we have a description.
        print(qDescription);
        bFoundAtLeastOne = False;

        #now read the dna code corresponding to that description
        qDNA = "";
        qLine = Q.readline().replace('\n', '');
        while(len(qLine) == 70):
            qDNA += qLine;
            qLine = Q.readline().replace('\n', '');
        qDNA += qLine;

        #now we have a dna code
        #now read from DNA database and look for this dna code
        D = open("DNA Database.txt", "r");
        dLine = D.readline().replace('\n', '');
        
        while(">EOF" not in dLine and len(dLine) > 0):
            if(dLine[0] == '>'): #description line
                dDescription = dLine[1: len(dLine)];

                #now we have a dna description
                #now read the dna code corresponding to that description
                dDNA = "";
                dLine = D.readline().replace('\n', '');
                while(len(dLine) == 70):
                    dDNA += dLine;
                    dLine = D.readline().replace('\n', '');
                dDNA += dLine;

                #now we have DNA code
                #look for the qDNA in dDNA
                index = search(dDNA, qDNA);
                if(index != -1):
                    print("[", dDescription, "] at offset ", index);
                    bFoundAtLeastOne = True;
                


            dLine = D.readline().replace('\n', '');
        D.close();
    if(bFoundAtLeastOne == False):
        print("NOT FOUND");
    qLine = Q.readline().replace('\n', '');

Q.close();