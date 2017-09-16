# 
# read all text messages from file and print the first 5
#  
import pandas as pd

filepath='C:\\dev\\learn\\udacity\\ml\homework-1\\'
filename='SMSSpamCollection'
filepathname=filepath + filename

myDateFrame = pd.read_table(filepathname, 
                            sep='\t', 
                            header=None, 
                            names=['tag', 'sms_message'])

myDateFrame['tag']=myDateFrame.tag.map({'ham':0, 'spam':1})

print(myDateFrame.shape)
print(myDateFrame.head())