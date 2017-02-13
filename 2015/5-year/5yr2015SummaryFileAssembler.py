#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:49:29 2016

@author: jonathanortiz
"""


import os
import csv
import xlrd
from sortedcontainers import SortedDict


#################
""" Parameters """
# Provide a list of sequences from ACS_1yr_Seq_Table_Number_Lookup.xls
# Either provide your own list of sequences or simply comment out topic areas you do not need

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


# Provide a list of geographies from 5yr_year_geo
'''geos = ["al", "ak", "az", "ar", "ca", "co", "ct", "dc", "de", "fl", "ga", "hi",
        "id", "il", "in", "ia", "ks", "ky", "la", "me", "md", "ma", "mi", "mn",
        "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh",
        "ok", "or", "pa", "ri", "sc", "sd", "tn", "tx", "us", "ut", "vt", "va",
        "wa", "wv", "wi", "wy"]'''
geos = ['us']
# Provide a choice of estimates, margins-of-error, or both
# Note: these codes must by uppercase to match those in the Sequence files
measures = ["E"]

# Provide a choice of US Census Summary Level Codes
# Either provide your own list of summary levels or simply comment out topic areas you do not need
# Note: the only current and valid input options are 40, 50, 160, 320, and 500
countrySummaryLevels = [
                        10, # Country (US only)
                        20, # Region (US only)
                        30, # Division (US only)
                        860, # ZCTA (ZIP code) (US only)
                       ]

stateSummaryLevels = [
                        40, # State
                        50, # County (States only)
                        160, # Place/City (States only)
                        320, # Metropolitan and Micropolitan Statistical Area (MSA) (States only)
                        500, # Congressional District (States only)
                     ]

# Note: Do not change topics or summaryLevelGeoHeaders dictionaries. These are required to assemble the output directories and files.
topics = { 1: "UnweightedCount", 2: "AgeSex", 3: "AgeSex", 4: "Race", 5: "HispanicOrigin", 6: "Ancestry", 7: "Ancestry", 8: "ForeignBirth", 9: "ForeignBirth", 10: "ForeignBirth", 11: "ForeignBirth", 12: "ForeignBirth", 13: "PlaceofBirth", 14: "PlaceofBirth", 15: "PlaceofBirth", 16: "ResidenceLastYear", 17: "ResidenceLastYear", 18: "ResidenceLastYear", 19: "ResidenceLastYear", 20: "ResidenceLastYear", 21: "ResidenceLastYear", 22: "ResidenceLastYear", 23: "JourneytoWork", 24: "JourneytoWork", 25: "JourneytoWork", 26: "JourneytoWork", 27: "JourneytoWork", 28: "JourneytoWork", 29: "JourneytoWork", 30: "JourneytoWork", 31: "JourneytoWork", 32: "JourneytoWork", 33: "JourneytoWork", 34: "Children", 35: "Grandparents", 36: "HouseholdsFamilies", 37: "HouseholdsFamilies", 38: "MaritalStatus", 39: "MaritalStatus", 40: "Fertility", 41: "School", 42: "School", 43: "Education", 44: "Education", 45: "Language", 46: "Language", 47: "Language", 48: "Poverty", 49: "Poverty", 50: "Poverty", 51: "Poverty", 52: "Poverty", 53: "Poverty", 54: "Poverty", 55: "Poverty", 56: "Poverty", 57: "Disability", 58: "Disability", 59: "Income", 60: "Income", 61: "Income", 62: "Income", 63: "Income", 64: "Income", 65: "Income", 66: "Income", 67: "Earnings", 68: "Earnings", 69: "Earnings", 70: "Earnings", 71: "Earnings", 72: "Earnings", 73: "Veterans", 74: "Veterans", 75: "TransferPrograms", 76: "Employment", 77: "Employment", 78: "Employment", 79: "Employment", 80: "Industry", 81: "Industry", 82: "Industry", 83: "Industry", 84: "Industry", 85: "Industry", 86: "Industry", 87: "Industry", 88: "Industry", 89: "Industry", 90: "Industry", 91: "Industry", 92: "Industry", 93: "Industry", 94: "Industry", 95: "Industry", 96: "Industry", 97: "Industry", 98: "Industry", 99: "Industry", 100: "Industry", 101: "Industry", 102: "Industry", 103: "Housing", 104: "Housing", 105: "Housing", 106: "Housing", 107: "Housing", 108: "Housing", 109: "Housing", 110: "Housing", 111: "Housing", 112: "Housing", 113: "GroupQuarters", 114: "HealthInsurance", 115: "HealthInsurance", 116: "HealthInsurance", 117: "HealthInsurance", 118: "QualityMeasures", 119: "Imputations", 120: "Imputations", 121: "Imputations", 122: "Imputations" }
summaryLevelGeoHeaders = { 10: [ "SummaryLevel", "US", "GEOID", "AreaName" ], 20: [ "SummaryLevel", "US", "Region", "GEOID", "AreaName" ], 30: [ "SummaryLevel", "US", "Division", "GEOID", "AreaName" ], 40: [ "SummaryLevel", "State", "StateFIPS", "GEOID", "AreaName" ], 50: [ "SummaryLevel", "State", "StateFIPS", "CountyFIPS", "GEOID", "AreaName" ], 160: [ "SummaryLevel", "State", "StateFIPS", "PlaceFIPS", "GEOID", "AreaName" ], 320: [ "SummaryLevel", "State", "StateFIPS", "CBSACode", "GEOID", "AreaName" ], 500: [ "SummaryLevel", "State", "StateFIPS", "District", "GEOID", "AreaName" ], 860: [ "SummaryLevel", "US", "ZCTA", "GEOID", "AreaName"] }

#################
""" Functions """
# takes a list of sequences and returns those aggregated sequences' topic areas
def getTopicAreas(seqs):
    topxSet = set()
    for seq in seqs:
        topxSet.add(topics[seq])
    topx = list(topxSet)
    return topx


# takes a list of sequences + a topic & returns only the sequences (from the list given) that make up that topic
def getSequencesWithinTopic(seqs, topic):
    likeSequences = []
    for seq in seqs:
        if topics[seq] == topic:
            likeSequences.append(seq)
    return likeSequences


# takes a list of topic areas, checks to see if output dirs exist for those topic areas, and, if not, makes the output dirs
def ensureDirs(topicAreas, measures):
    for measure in measures:
        for topic in topicAreas:
            d = os.getcwd() + "/output/ACS2015_5_" + measure + "_" + topic + "/"
            if not os.path.exists(d):
                os.makedirs(d)


# takes a sequence number as an argument and returns the sequence header as a list
def getSeqHeader(seq):
    header = []
    inFileName = os.getcwd() + "/data/2015_5yr_Summary_FileTemplates/Seq" + str(seq) + ".xls"
    seqFile = xlrd.open_workbook(inFileName)
    sheet = seqFile.sheet_by_index(0)
    numCols = sheet.ncols
    for col in range(6,numCols):
        header.append(sheet.cell_value(0, col))
    return header


# takes a list of "alike sequences," which can be found using the getSequencesWithinTopic() function, &
# a summary level and returns a concatenated header with Geo Code column labels for the given summary level
# and Census Table ID column labels from each like sequence
def makeSummaryFileHeader(alikeSeqs, summaryLevel):
    header = []
    header += summaryLevelGeoHeaders[summaryLevel]
    for seq in alikeSeqs:
        header += getSeqHeader(seq)
    return header


# takes a sequence number, geography, and choice of either Estimate or Margin-of-Error file and returns
# a dictionary of all summary file data, using 7 digit Logical Record Numbers (LOGRECNO) as the dictionary key
def getSummaryDataDict(seq, EorM, geo):
    summaryData = SortedDict({})
    number = str(seq).zfill(4)
    inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20155" + geo + number + "000.txt"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            summaryData[row[5]] = row[6:]
    return summaryData


# takes a sequence number, geography, and choice of either Estimate or Margin-of-Error file
# and returns a list of its summary file data, without 7 digit Logical Record Numbers (LOGRECNO)
def getSummaryDataList(seq, EorM, geo):
    summaryData = []
    number = str(seq).zfill(4)
    inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20155" + geo + number + "000.txt"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            summaryData.append(row[6:])
    return summaryData


# take a list of alike sequences, a choice of either Estimates or Margins-of-error, and a geography and
# returns a dictionary of concatenated summary file data from all alike sequences,
# using 7 digit Logical Record Numbers (LOGRECNO) as the dictionary key
def getConcatenatedSummaryDataDict(alikeSeqs, EorM, geo):
    if alikeSeqs.__len__() == 1:
        summaryData = getSummaryDataDict(alikeSeqs[0], EorM, geo)
    elif alikeSeqs.__len__() > 1:
        summaryData = getSummaryDataDict(alikeSeqs[0], EorM, geo)
        for i in range(1, alikeSeqs.__len__()):
            currentSeqData = getSummaryDataList(alikeSeqs[i], EorM, geo)
            j = 0
            for entry in summaryData:
                summaryData[entry] += currentSeqData[j]
                j += 1
    return summaryData


# takes a geography and a list of summary levels and returns all raw geo data
# for the given geography at the given summary levels
def getRawGeoData(geo, sumLvls):
    sumLvlStrs = []
    for code in sumLvls:
        sumLvlStrs.append(str(code).zfill(3))
    geoCodes = []
    inFileName = os.getcwd() + "/data/5yr_year_geo/2015_ACS_Geography_Files/g20155" + geo + ".csv"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            if row[2] in sumLvlStrs:
                geoCodes.append(row)
    return geoCodes


# takes raw geo data & a summary level and returns a dictionary of cleaned geo codes for the given summary level,
# using 7 digit Logical Record Numbers (LOGRECNO) as the dictionary keys
def getGeoCodes(rawGeoData, sumLvl):
    cleanGeos = SortedDict({})
    paddedSumLvl = str(sumLvl).zfill(3)

    if sumLvl == 10:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [10, row[1], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 20:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [20, row[1], row[6], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 30:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [30, row[1], row[7], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 40:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [40, row[1], row[9], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 50:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [50, row[1], row[9], row[10], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 160:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [160, row[1], row[9], row[12], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 320:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [320, row[1], row[9], row[22], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 500:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [500, row[1], row[9], row[32], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    elif sumLvl == 860:
        for row in rawGeoData:
            if row[2] == paddedSumLvl:
                geoCache = [860, row[1], row[37], row[48], row[49]]
                cleanGeos[row[4]] = geoCache
            else:
                continue

    else:
        raise ValueError('An invalid summary level was passed to the getGeoCodes() function')

    return cleanGeos


# takes a list of sequences as input and returns a list of those sequences divided into batches based on their topic
def batchAlikeSequences(seqs):
    batches = []
    Counts = []
    AgeSex = []
    Race = []
    Hispanic = []
    Ancestry = []
    Foreign = []
    Place = []
    Residence = []
    Journey = []
    Children = []
    Grands = []
    Households = []
    Marital = []
    Fertility = []
    School = []
    Educational = []
    Language = []
    Poverty = []
    Disability = []
    Income = []
    Earnings = []
    Veteran = []
    Transfer = []
    Employment = []
    Industry = []
    Housing = []
    Group = []
    Health = []
    Quality = []
    Imputations = []

    for seq in seqs:
        if seq in [1]:
            Counts.append(seq)
        elif seq in [2, 3]:
            AgeSex.append(seq)
        elif seq in [4]:
            Race.append(seq)
        elif seq in [5]:
            Hispanic.append(seq)
        elif seq in [6, 7]:
            Ancestry.append(seq)
        elif seq in [8, 9, 10, 11, 12]:
            Foreign.append(seq)
        elif seq in [13, 14, 15]:
            Place.append(seq)
        elif seq in [16, 17, 18, 19, 20, 21, 22]:
            Residence.append(seq)
        elif seq in [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]:
            Journey.append(seq)
        elif seq in [34]:
            Children.append(seq)
        elif seq in [35]:
            Grands.append(seq)
        elif seq in [36, 37]:
            Households.append(seq)
        elif seq in [38, 39]:
            Marital.append(seq)
        elif seq in [40]:
            Fertility.append(seq)
        elif seq in [41, 42]:
            School.append(seq)
        elif seq in [43, 44]:
            Educational.append(seq)
        elif seq in [45, 46, 47]:
            Language.append(seq)
        elif seq in [48, 49, 50, 51, 52, 53, 54, 55, 56]:
            Poverty.append(seq)
        elif seq in [57, 58]:
            Disability.append(seq)
        elif seq in [59, 60, 61, 62, 63, 64, 65, 66]:
            Income.append(seq)
        elif seq in [67, 68, 69, 70, 71, 72]:
            Earnings.append(seq)
        elif seq in [73, 74]:
            Veteran.append(seq)
        elif seq in [75]:
            Transfer.append(seq)
        elif seq in [76, 77, 78, 79]:
            Employment.append(seq)
        elif seq in [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]:
            Industry.append(seq)
        elif seq in [103, 104, 105, 106, 107, 108, 109, 110, 111, 112]:
            Housing.append(seq)
        elif seq in [113]:
            Group.append(seq)
        elif seq in [114, 115, 116, 117]:
            Health.append(seq)
        elif seq in [118]:
            Quality.append(seq)
        elif seq in [119, 120, 121, 122]:
            Imputations.append(seq)

    batches.append(Counts)
    batches.append(AgeSex)
    batches.append(Race)
    batches.append(Hispanic)
    batches.append(Ancestry)
    batches.append(Foreign)
    batches.append(Place)
    batches.append(Residence)
    batches.append(Journey)
    batches.append(Children)
    batches.append(Grands)
    batches.append(Households)
    batches.append(Marital)
    batches.append(Fertility)
    batches.append(School)
    batches.append(Educational)
    batches.append(Language)
    batches.append(Poverty)
    batches.append(Disability)
    batches.append(Income)
    batches.append(Earnings)
    batches.append(Veteran)
    batches.append(Transfer)
    batches.append(Employment)
    batches.append(Industry)
    batches.append(Housing)
    batches.append(Group)
    batches.append(Health)
    batches.append(Quality)
    batches.append(Imputations)

    batches = [var for var in batches if var]

    return batches


# takes a concatenated summary data dictionary, which can be found using the getConcatenatedSummaryDataDict() function,
# a list of alike sequences, a geography, a summary level, and a choice of either Estimates or Margins-of-error and
# writes out a geo-coded summary file csv
def assemble(concatenatedData, geoCodes, header, alikeSeqs, geo, sumLvl, EorM):
    topic = getTopicAreas(alikeSeqs)
    if topic.__len__() != 1:
        raise ValueError('The assemble() function may only be passed sequences from the same topic area')

    if sumLvl == 10:
        sumLvlStr = "Country"
    elif sumLvl == 20:
        sumLvlStr = "Region"
    elif sumLvl == 30:
        sumLvlStr = "Division"
    elif sumLvl == 40:
        sumLvlStr = "State"
    elif sumLvl == 50:
        sumLvlStr = "County"
    elif sumLvl == 160:
        sumLvlStr = "Place"
    elif sumLvl == 320:
        sumLvlStr = "MSA"
    elif sumLvl == 500:
        sumLvlStr = "Congress_District"
    elif sumLvl == 860:
        sumLvlStr = "ZCTA"
    else:
        raise ValueError('An invalid summary level was passed to the assemble() function')

    outFileName = os.getcwd() + "/output/ACS2015_5_" + EorM + "_" + topic[0] + "/" + geo.upper() + "_" + sumLvlStr + ".csv"

    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for entry in geoCodes:
            writer.writerow(geoCodes[entry] + concatenatedData[entry])


#
def assembleAllStatesFile(alikeSeqs, EorM):
    topic = getTopicAreas(alikeSeqs)
    if topic.__len__() != 1:
        raise ValueError('The assembleAllStatesFile() function may only be passed sequences from the same topic area')

    sumLvl = 40
    outFileName = os.getcwd() + "/output/ACS2015_5_" + EorM + "_" + topic[0] + "/US_All_States.csv"
    allStates = [  "al", "ak", "az", "ar", "ca", "co", "ct", "dc", "de", "fl", "ga", "hi", "id", "il", "in", "ia", "ks",
                "ky", "la", "me", "md", "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc",
                "nd", "oh", "ok", "or", "pa", "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy"]

    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(makeSummaryFileHeader(alikeSeqs, sumLvl))

        for state in allStates:
            geoCodes = []
            stateRow = []
            inFileName = os.getcwd() + "/data/5yr_year_geo/2015_ACS_Geography_Files/g20155" + state + ".csv"
            with open(inFileName, 'r', newline='') as inFile:
                reader = csv.reader(inFile, delimiter=',', quotechar='"')
                rowOne = next(reader)
                geoCodes += [sumLvl, rowOne[1], rowOne[9], rowOne[48], rowOne[49]]

            summaryData = []
            if alikeSeqs.__len__() == 1:
                number = str(alikeSeqs[0]).zfill(4)
                inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20155" + state + number + "000.txt"
                with open(inFileName, 'r', newline='') as inFile:
                    reader = csv.reader(inFile, delimiter=',', quotechar='"')
                    row = next(reader)
                    summaryData += row[6:]
            elif alikeSeqs.__len__() > 1:
                for seq in alikeSeqs:
                    number = str(seq).zfill(4)
                    inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20155" + state + number + "000.txt"
                    with open(inFileName, 'r', newline='') as inFile:
                        reader = csv.reader(inFile, delimiter=',', quotechar='"')
                        row = next(reader)
                        summaryData += row[6:]

            stateRow += geoCodes + summaryData
            writer.writerow(stateRow)


#
def writeTableTitleKey(seqs, EorM):
    topic = getTopicAreas(seqs)
    outFileName = os.getcwd() + "/output/ACS2015_5_" + EorM + "_" + topic[0] + "/" + "00_TableTitleKey.csv"
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
ensureDirs(topicAreas, measures)

batches = batchAlikeSequences(sequences)

for area in geos:
    if area == 'us':
        rawData = getRawGeoData(area,countrySummaryLevels)
        for sumLevel in countrySummaryLevels:
            geoCoding = getGeoCodes(rawData, sumLevel)
            for batch in batches:
                topRow = makeSummaryFileHeader(batch, sumLevel)
                for measure in measures:
                    summaryDataDict = getConcatenatedSummaryDataDict(batch,measure,area)
                    assemble(summaryDataDict, geoCoding, topRow, batch, area, sumLevel, measure)
    else:
        rawData = getRawGeoData(area,stateSummaryLevels)
        for sumLevel in stateSummaryLevels:
            geoCoding = getGeoCodes(rawData, sumLevel)
            for batch in batches:
                topRow = makeSummaryFileHeader(batch, sumLevel)
                for measure in measures:
                    summaryDataDict = getConcatenatedSummaryDataDict(batch,measure,area)
                    assemble(summaryDataDict, geoCoding, topRow, batch, area, sumLevel, measure)

for batch in batches:
    for measure in measures:
        writeTableTitleKey(batch, measure)
        assembleAllStatesFile(batch, measure)
