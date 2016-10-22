# -*- coding: utf-8 -*-
import ftplib
import os
import csv
import sys

# Uploads the html file to the noolaham.net server
def uploadToServer(i_session, i_ftppath, i_htmldir, i_htmlfile):
     i_session.cwd(i_ftppath)
     os.chdir(i_htmldir)
     file = open(i_htmlfile,'rb')                  		# file to send
     i_session.storbinary('STOR ' + i_htmlfile, file)     	# send the file
     file.close()                                    	# close file and FTP
     return 
	 
htmldir = r"C:\Users\data"
session = ftplib.FTP('ftpserver','ftpusername','ftppwd')

# read the csv file with ftp path and html file information and upload to server
batchfile = open('batchdata.csv', 'rt')
try:
     reader = csv.reader(batchfile)
     for row in reader:
          ocrProcessStatus = row[0]
          ftppath = row[4]
          htmlfile = row[1]
          rightsPermission = row[2]
          if ocrProcessStatus == "Completed" or ocrProcessStatus == "Failed" or rightsPermission == "Blocked":
               print "Completed.  Skipping " + htmlfile
               continue
               
          print "uploading " + htmlfile + " to " + ftppath
          uploadToServer(session, ftppath, htmldir, htmlfile)		  
finally:
     batchfile.close()
	
session.quit()

