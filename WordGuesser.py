import pandas
import os
import re

#initializes the data frames
starter = {
    "word": [], 
    "count": [],
    "percent": []
        };
wordData = pandas.DataFrame(starter)
inputWordData = pandas.DataFrame(starter)

curDataFrameWritingTo = wordData #the data frame we are currently using 

def main():
    #Defines what variables are global
    global curDataFrameWritingTo
    global inputWordData
    global wordData
    
    #populates the training data data frame
    addFolderAsWordData("trainingData")
    wordData = curDataFrameWritingTo
    
    #populates the input data data frame
    curDataFrameWritingTo = inputWordData
    addFolderAsWordData("inputData")
    inputWordData = curDataFrameWritingTo
    
    updatePercents(wordData)
    updatePercents(inputWordData)
    print(f"Training Word data:\n{wordData}\n\n\n\n")
    print(f"Input Word data:\n{inputWordData}\n\n\n\n")




#for any given data frame, this adds a column of a 'percent'
#based on how often the word is used in general, and returns
#the new data frame.
def updatePercents(dataFrame):
    
    #finds the total amount of words
    totalWords = 0
    for row in dataFrame.itertuples():
        totalWords += row.count

    #adds the percent value to each one
    for row in dataFrame.itertuples():
        dataFrame.at[row.Index, "percent"] = (row.count / totalWords) * 100
    
    
    

#********************INITIALIZING*********************************


#this function will take in a folder of files that it will
#then populate wordData, and create a percentage value for
#each word, representing how often it is used.
def addFolderAsWordData(folderName):
    for file in os.listdir(folderName): #for every file in the folder
        filePath = os.path.join(folderName, file) # makes one longer string for the path
        if os.path.isfile(filePath): #if it's a file
            addFile(open(filePath, "r")) #add the file to worddata
            

#adds a file to word data, line by line
def addFile(file):
    allLines = file.readlines()
    
    for line in allLines: #for each line
        addLine(line)

#adds a line to word data, word by word
def addLine(line):
    words = line.split() #makes an array of the words in the line
    for word in words:
        if (word.isalpha() == False):
            addWord(processWord(word))
        else:
            addWord(processWord(word))

#returns the word as a lowercase string with no non-letter componenets
def processWord(word):
    word = word.strip() #remove leading/trailing characters
    word = re.sub(r'[^a-zA-Z]', '', word) #removes any non letter symbols
    word = word.lower() #makes it all lowercase
    return word

#Will add a word to the dataframe wordData, 
#either by adding a new row (if it hasn't been added yet), 
#or incrementing the count associated with it
def addWord(word):
    global curDataFrameWritingTo
   
    sameWordBoolMask = curDataFrameWritingTo["word"] == word #makes a boolean mask of repeated words
    if (sameWordBoolMask.any()): #if the word already exists in the frame
        index = curDataFrameWritingTo.loc[sameWordBoolMask, "word"].index.astype(int) #gets the index of the word that is duplicated
        curDataFrameWritingTo.loc[index, "count"] += 1 #adds 1 to the count 
    
    else: #if this is the first time the word appears  
        newData = {"word": word, "count": int(1)} #make the new line a data object
        newLine = pandas.DataFrame(newData, index = [len(curDataFrameWritingTo)]) #makes a new dataframe with this line at the correct index
        curDataFrameWritingTo = pandas.concat([curDataFrameWritingTo, newLine], ignore_index=True) #connects it with the original, essentially adding a line


main()
