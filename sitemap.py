# -*- coding: utf-8 -*-
import ftplib
import os
import csv
import sys


# read the csv file with ftp path and html file information and upload to server
def createSitemapEntries(i_fileName, i_siteMapFile):
    batchfile = open(i_fileName, 'rt')
    try:
        reader = csv.reader(batchfile)
        for row in reader:
            ocrProcessStatus = row[0]
            htmlfile = row[1]         
            rightsPermission = row[2]
            pdffileurl = row[3]            
            ftppath = row[4]
            
            htmlfileurl = "http://noolaham.net" + ftppath + "/" + htmlfile;              
            print "sitemap " + htmlfileurl + " - " + pdffileurl
            
            if rightsPermission == "Blocked":
                print "Skipping " + htmlfile + " Blocked."
                continue
                
            i_siteMapFile.write("<url>\n")
            i_siteMapFile.write("<loc>" + pdffileurl + "</loc>\n")
            i_siteMapFile.write("<changefreq>weekly</changefreq>\n")        
            i_siteMapFile.write("<priority>0.7</priority>\n")  
            i_siteMapFile.write("</url>\n")
            
            if ocrProcessStatus == "Failed":
                print "Skipping " + htmlfile + " OCR Failed."
                continue    
                
            i_siteMapFile.write("<url>\n")
            i_siteMapFile.write("<loc>" + htmlfileurl + "</loc>\n")
            i_siteMapFile.write("<changefreq>weekly</changefreq>\n")  
            i_siteMapFile.write("<priority>0.8</priority>\n") 
            i_siteMapFile.write("</url>\n")       
            
    
    finally:
        batchfile.close()
        


siteMapFile = open("sitemap.xml", "w")
siteMapFile.truncate()
siteMapFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
siteMapFile.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

for x in range(41, 51):        
    fileName = "batchdata_" + str(x)+ ".csv"
    file = os.path.join(r"C:\data\all", fileName)
    createSitemapEntries(file, siteMapFile)

siteMapFile.write("</urlset>")    
siteMapFile.close()