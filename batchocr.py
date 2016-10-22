#!/usr/bin/python
# -*- coding: utf-8 -*-

#version 22102016v1

import ftplib
import os
import csv
import sys
import os.path
import cgi
import urllib

def createConfigFile(i_fileName, i_pdfUrl, i_numColumns, i_title):
    configFile = open(i_fileName, "w")
    configFile.truncate()
    configFile.write("[settings]\n\n")
    configFile.write("file_url = " + i_pdfUrl + "\n")
    configFile.write("columns = " + i_numColumns + "\n")
    configFile.write("wiki_username = Natkeeran\n")
    configFile.write("wiki_password = testing\n")
    configFile.write("wikisource_language_code = ta\n")
    configFile.write("keep_temp_folder_in_google_drive = yes\n")
    configFile.write("edit_summary = Tamil OCR text from Google\n") 
    configFile.write("title = " + i_title + "\n") 
    configFile.close()

    
# read the csv file with ftp path and html file information and upload to server

ocrResultList = []

batchfile = open('batchdata.csv', 'rt')
try:
     reader = csv.reader(batchfile)
     for row in reader:
          noolahamNumber = row[5]
          ocrProcessStatus = row[0]
          rightsPermission = row[2]
          pdfurl = row[3]
          title = row[7]
          columnNum = ""
          if(len(row) >= 10):
              columnNum = row[9]
          title = title.rstrip()
          if ocrProcessStatus == "Success" or ocrProcessStatus == "Completed" or rightsPermission == "Blocked":
               print ocrProcessStatus + " Skipping " + pdfurl
               continue

          print "do_ocr " + pdfurl 
          actualColumnNum = "2"
          if not (columnNum == ""):
               actualColumnNum = columnNum
          createConfigFile("config.ini", pdfurl, actualColumnNum, title)          
          os.system("python do_ocr.py")
          ocrResultList.append(noolahamNumber)
finally:
     batchfile.close()

print "\n The following pdfs were completed: "     
print ocrResultList
   
	
