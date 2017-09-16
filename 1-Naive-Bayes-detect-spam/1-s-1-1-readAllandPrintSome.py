# 
# read all text messages from file and print the first 5
#  
import pandas as pd

filepath='C:\\dev\\learn\\udacity\\ml\\1-Naive-Bayes-detect-spam\data\\'
filename='SMSSpamCollection'
filepathname=filepath + filename

myDateFrame = pd.read_table(filepathname, 
                            sep='\t', 
                            header=None, 
                            names=['tag', 'sms_message'])

print(myDateFrame.head())