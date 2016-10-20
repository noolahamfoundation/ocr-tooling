import os
import glob
import csv

folderPath = "/var/www/html/ocr/ocr-by-batch-number/OCT-2016-ocr-6/"
batchFileName = "batchdata.csv";
ocrResultFileName = "ocrresult_" + batchFileName;

# get all html files this is updated checkResult on sep18-2016
folderPattern = folderPath + "*.html"
ocrdFiles = [os.path.basename(x) for x in glob.glob(folderPattern)]

batchFile = open(folderPath + "/" + batchFileName)
fileReader = csv.reader(batchFile)

outputFile = open(folderPath + "/" + ocrResultFileName, 'wb')
fileWriter = csv.writer(outputFile)

for row in fileReader:
    ocrResult = "Failed"    
    if row[1] in ocrdFiles:
        ocrResult = "Success"
    fileWriter.writerow([ocrResult])
    print row[1] + " - " + ocrResult
batchFile.close()
outputFile.close()

        
