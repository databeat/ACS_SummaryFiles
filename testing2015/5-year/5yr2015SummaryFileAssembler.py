#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:49:29 2016

@author: jonathanortiz
"""

import os
import csv
import xlrd


#################
""" Parameters """
# Provide a list of sequences from ACS_1yr_Seq_Table_Number_Lookup.xls
# Either provide your own list of sequences or simply comment out topic areas you do not need
'''
sequences = [
#            1, # Unweighted Count
            2, 3, # Age-Sex
            4, # Race
            5, # Hispanic Origin
            6, 7, # Ancestry
            8, 9, 10, 11, 12, # Foreign Birth
            13, 14, 15, # Place of Birth - Native
            16, 17, 18, 19, 20, 21, 22, # Residence Last Year - Migration
#            23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, # Journey to Work
#            34, # Children - Relationship
#            35, # Grand(Persons) - Age of HH Members
#            36, 37, # Households - Families
#            38, 39, # Marital Status
#            40, # Fertility
            41, 42, # School Enrollment
            43, 44, # Educational Attainment
            45, 46, 47, # Language
            48, 49, 50, 51, 52, 53, 54, 55, 56, # Poverty
#            57, 58, # Disability
            59, 60, 61, 62, 63, 64, 65, 66, # Income
            67, 68, 69, 70, 71, 72, # Earnings
#            73, 74, # Veteran Status
#            75, # Transfer Programs
            76, 77, 78, 79, # Employment Status
#            80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, # Industry-Occupation-Class of Worker
            103, 104, 105, 106, 107, 108, 109, 110, 111, 112, # Housing
#            113, # Group Quarters
            114, 115, 116, 117, # Health Insurance
#            118, # Quality Measures
#            119, 120, 121, 122, # Imputations
            ]
'''
sequences = [1, 2, 66, 67]

# Provide a list of geographies from 5yr_year_geo
'''
geos = ["al", "ak", "az", "ar", "ca", "co", "ct", "de", "fl", "ga", "hi", "id",
       "il", "in", "ia", "ks", "ky", "la", "me", "md", "ma", "mi", "mn", "ms",
       "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh", "ok",
       "or", "pa", "ri", "sc", "sd", "tn", "tx", "us", "ut", "vt", "va", "wa",
       "wv", "wi", "wy"]
'''
geos = ["ca", "dc", "wy"]

# Provide a choice of estimates, margins-of-error, or both
# Note: these codes must by uppercase to match those in the Sequence files
measures = ["E", "M"]

# Provide

# Note: Do not change topics dictionary. It is required to assemble the output directories
topics = {1: "Unweighted Count", 2: "Age-Sex", 3: "Age-Sex", 4: "Race", 5: "Hispanic Origin", 6: "Ancestry", 7: "Ancestry", 8: "Foreign Birth", 9: "Foreign Birth", 10: "Foreign Birth", 11: "Foreign Birth", 12: "Foreign Birth", 13: "Place of Birth - Native", 14: "Place of Birth - Native", 15: "Place of Birth - Native", 16: "Residence Last Year - Migration", 17: "Residence Last Year - Migration", 18: "Residence Last Year - Migration", 19: "Residence Last Year - Migration", 20: "Residence Last Year - Migration", 21: "Residence Last Year - Migration", 22: "Residence Last Year - Migration", 23: "Journey to Work", 24: "Journey to Work", 25: "Journey to Work", 26: "Journey to Work", 27: "Journey to Work", 28: "Journey to Work", 29: "Journey to Work", 30: "Journey to Work", 31: "Journey to Work", 32: "Journey to Work", 33: "Journey to Work", 34: "Children - Relationship", 35: "Grand(Persons) - Age of HH Members", 36: "Households - Families", 37: "Households - Families", 38: "Marital Status", 39: "Marital Status", 40: "Fertility", 41: "School Enrollment", 42: "School Enrollment", 43: "Educational Attainment", 44: "Educational Attainment", 45: "Language", 46: "Language", 47: "Language", 48: "Poverty", 49: "Poverty", 50: "Poverty", 51: "Poverty", 52: "Poverty", 53: "Poverty", 54: "Poverty", 55: "Poverty", 56: "Poverty", 57: "Disability", 58: "Disability", 59: "Income", 60: "Income", 61: "Income", 62: "Income", 63: "Income", 64: "Income", 65: "Income", 66: "Income", 67: "Earnings", 68: "Earnings", 69: "Earnings", 70: "Earnings", 71: "Earnings", 72: "Earnings", 73: "Veteran Status", 74: "Veteran Status", 75: "Transfer Programs", 76: "Employment Status", 77: "Employment Status", 78: "Employment Status", 79: "Employment Status", 80: "Industry-Occupation-Class of Worker", 81: "Industry-Occupation-Class of Worker", 82: "Industry-Occupation-Class of Worker", 83: "Industry-Occupation-Class of Worker", 84: "Industry-Occupation-Class of Worker", 85: "Industry-Occupation-Class of Worker", 86: "Industry-Occupation-Class of Worker", 87: "Industry-Occupation-Class of Worker", 88: "Industry-Occupation-Class of Worker", 89: "Industry-Occupation-Class of Worker", 90: "Industry-Occupation-Class of Worker", 91: "Industry-Occupation-Class of Worker", 92: "Industry-Occupation-Class of Worker", 93: "Industry-Occupation-Class of Worker", 94: "Industry-Occupation-Class of Worker", 95: "Industry-Occupation-Class of Worker", 96: "Industry-Occupation-Class of Worker", 97: "Industry-Occupation-Class of Worker", 98: "Industry-Occupation-Class of Worker", 99: "Industry-Occupation-Class of Worker", 100: "Industry-Occupation-Class of Worker", 101: "Industry-Occupation-Class of Worker", 102: "Industry-Occupation-Class of Worker", 103: "Housing", 104: "Housing", 105: "Housing", 106: "Housing", 107: "Housing", 108: "Housing", 109: "Housing", 110: "Housing", 111: "Housing", 112: "Housing", 113: "Group Quarters", 114: "Health Insurance", 115: "Health Insurance", 116: "Health Insurance", 117: "Health Insurance", 118: "Quality Measures", 119: "Imputations", 120: "Imputations", 121: "Imputations", 122: "Imputations"}

#################
""" Functions """
def getTopicAreas(seqs):
    topxSet = set()
    for seq in seqs:
        topxSet.add(topics[seq])
    topx = list(topxSet)
    return topx


def ensureDirs(topicAreas):
    for topic in topicAreas:
        d = os.getcwd() + "/output/" + topic + "/"
        if not os.path.exists(d):
            os.makedirs(d)


def getSeqHeader(seq):
    header = []
    inFileName = os.getcwd() + "/data/2015_5yr_Summary_FileTemplates/Seq" + str(seq) + ".xls"
    seqFile = xlrd.open_workbook(inFileName)
    sheet = seqFile.sheet_by_index(0)
    numCols = sheet.ncols
    for col in range(6,numCols):
        header.append(sheet.cell_value(0, col))
    header.insert(0, "GEOID")
    header.insert(1, "GEONAME")
    return header


def getSummaryData(seq, EorM, geo):
    data = []
    number = str(seq).zfill(4)
    inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20155" + geo + number + "000.txt"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            data.append(row[6:])
    return data


def getGeoCodes(geo):
    geoCodes = []
    inFileName = os.getcwd() + "/data/5yr_year_geo/" + geo + ".xls"
    wb = xlrd.open_workbook(inFileName)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    for i in range(1,rows):
        geoid = sheet.cell_value(i, 2)
        geoname = sheet.cell_value(i, 3)
        geoCodes.append([geoid, geoname])
    return geoCodes


def assemble(seq, EorM, geo, header, geoCodes, data):
    topic = topics[seq]
    number = str(seq).zfill(3)
    outFileName = os.getcwd() + "/output/" + topic + "/" + geo.upper() + "_" + topic + "_" + number + EorM.lower() + ".csv"
    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for row in data:
            index = data.index(row)
            g = geoCodes[index]
            row.insert(0, g[0])
            row.insert(1, g[1])
            writer.writerow(row)


def writeTableTitleKey(seqs):
    outFileName = os.getcwd() + "/output/!TableTitleKey.csv"
    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ["TableNumber" , "TableTitle"]
        writer.writerow(header)
        for seq in seqs:
            inFileName = os.getcwd() + "/data/2015_5yr_Summary_FileTemplates/Seq" + str(seq) + ".xls"
            seqFile = xlrd.open_workbook(inFileName)
            sheet = seqFile.sheet_by_index(0)
            numCols = sheet.ncols
            for col in range(6,numCols):
                titlePair = []
                titlePair.append(sheet.cell_value(0, col))
                titlePair.append(sheet.cell_value(1, col))
                writer.writerow(titlePair)

############
""" Main """

topicAreas = getTopicAreas(sequences)

ensureDirs(topicAreas)

for geo in geos:
    geoCodes = getGeoCodes(geo)
    for seq in sequences:
        header = getSeqHeader(seq)
        for EorM in measures:
            data = getSummaryData(seq, EorM, geo)
            assemble(seq, EorM, geo, header, geoCodes, data)

writeTableTitleKey(sequences)