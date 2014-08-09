import json
arrTweet=[]
scores = {} # initialize an empty dictionary
f = open('output3.txt','w')

def convertLinesToJson():
    f = open('output1.txt', 'r')
    with f as myfile:
         for line in myfile:
             arrTweet.append(json.loads(line))


def getTweetsInDict():
    afinnfile = open("AFINN-111.txt")
    
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        
        
def findTweets(k):
    for x in range(0,len(scores)):
        #f.write(scores.keys()[x]+'\n')
        if scores.keys()[x] in arrTweet[k]:
            #print('yes')
            f.write((scores.keys()[x] + '--' + str(scores.values()[x])))
        #else:
           # scr = scr + 0   
       
               
def main():
    convertLinesToJson()
    getTweetsInDict()
    print(len(arrTweet))
    for x in range(0,len(arrTweet)):
        #f.write(str(arrTweet[x]))
        f.write("tweet " + str(x) + '\n')
        f.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        #f.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        #f.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        findTweets(x)
    f.close()
  
              


if __name__ == '__main__':
    main()  
