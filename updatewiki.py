# -*- coding: utf-8 -*-
import urllib
import ftplib
import os
import csv
import sys
from wikitools import wiki
from wikitools import api

def getNoolahamToken(i_site, i_api):
     params = {'action':'query', 'prop':'info','intoken':'edit','titles':'1'}
     req = i_api.APIRequest(i_site, params)
     response = req.query(False)
     token = response['query']['pages']['-1']['edittoken']
     return token
	 
def updateWikiPage(i_site, i_api, i_token, i_titlePage, i_updateText):
     params = {'action':'edit', 'title':i_titlePage, 'token':i_token, 'section':'1', 'sectiontitle': 'வாசிக்க', 'appendtext':i_updateText}
     request = i_api.APIRequest(i_site, params)
     result = request.query()
     print result
     return	 
	 
	 
# create a Wiki object
site = wiki.Wiki("http://wiki.api.php") 

# login - required for read-restricted wikis
if not site.login("User ", "userpwd", verify=True):
    print("Login failed")

#Get Token (needed to edit wiki)
token = getNoolahamToken(site, api)

#Read through each entry and update wiki
batchfile = open('batchdata.csv', 'rt')
try:
     reader = csv.reader(batchfile)
     for row in reader:
          ocrProcessStatus = row[0]
          rightsPermission = row[2]
          wikiPageTitle = row[7]
          htmlfile = row[1]
          
          if ocrProcessStatus == "Completed" or ocrProcessStatus == "Failed" or rightsPermission == "Blocked":
               print "Completed.  Skipping " + htmlfile
               continue
               
          noolahamOCRLink = "http://noolaham.net" + row[4] + "/" + htmlfile
          updateText = "\n<!--ocr_link-->* [" + noolahamOCRLink + " " + wikiPageTitle + " (எழுத்துணரியாக்கம்)]<!--ocr_link-->\n"		  
          print "Updaing wiki page " + wikiPageTitle + " with link to " + noolahamOCRLink
          updateWikiPage(site, api, token, wikiPageTitle, updateText)		  		  
finally:
     batchfile.close()
	 