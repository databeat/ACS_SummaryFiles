#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:22:16 2017

@author: jonathanortiz
"""


import argparse
import os
import csv
import json
import xlrd
from sortedcontainers import SortedDict

#################
""" Functions """
def get_topic_areas(seqs):
    # takes a list of sequences and returns those aggregated sequences' topic areas. Note: removes duplicate topics.
    topics = {1: "UnweightedCount", 2: "AgeSex", 3: "AgeSex", 4: "Race", 5: "HispanicOrigin", 6: "Ancestry",
              7: "Ancestry", 8: "ForeignBirth", 9: "ForeignBirth", 10: "ForeignBirth", 11: "ForeignBirth",
              12: "ForeignBirth", 13: "PlaceOfBirth", 14: "PlaceOfBirth", 15: "PlaceOfBirth", 16: "ResidenceLastYear",
              17: "ResidenceLastYear", 18: "ResidenceLastYear", 19: "ResidenceLastYear", 20: "ResidenceLastYear",
              21: "ResidenceLastYear", 22: "ResidenceLastYear", 23: "JourneyToWork", 24: "JourneyToWork",
              25: "JourneyToWork", 26: "JourneyToWork", 27: "JourneyToWork", 28: "JourneyToWork", 29: "JourneyToWork",
              30: "JourneyToWork", 31: "JourneyToWork", 32: "JourneyToWork", 33: "JourneyToWork", 34: "Children",
              35: "Grandparents", 36: "HouseholdsFamilies", 37: "HouseholdsFamilies", 38: "MaritalStatus",
              39: "MaritalStatus", 40: "Fertility", 41: "SchoolEnrollment", 42: "SchoolEnrollment", 43: "Education",
              44: "Education", 45: "Language", 46: "Language", 47: "Language", 48: "Poverty", 49: "Poverty",
              50: "Poverty", 51: "Poverty", 52: "Poverty", 53: "Poverty", 54: "Poverty", 55: "Poverty", 56: "Poverty",
              57: "Disability", 58: "Disability", 59: "Income", 60: "Income", 61: "Income", 62: "Income", 63: "Income",
              64: "Income", 65: "Income", 66: "Income", 67: "Earnings", 68: "Earnings", 69: "Earnings", 70: "Earnings",
              71: "Earnings", 72: "Earnings", 73: "Veterans", 74: "Veterans", 75: "TransferPrograms",
              76: "EmploymentStatus", 77: "EmploymentStatus", 78: "EmploymentStatus", 79: "EmploymentStatus",
              80: "Industry", 81: "Industry", 82: "Industry", 83: "Industry", 84: "Industry", 85: "Industry",
              86: "Industry", 87: "Industry", 88: "Industry", 89: "Industry", 90: "Industry", 91: "Industry",
              92: "Industry", 93: "Industry", 94: "Industry", 95: "Industry", 96: "Industry", 97: "Industry",
              98: "Industry", 99: "Industry", 100: "Industry", 101: "Industry", 102: "Industry", 103: "Housing",
              104: "Housing", 105: "Housing", 106: "Housing", 107: "Housing", 108: "Housing", 109: "Housing",
              110: "Housing", 111: "Housing", 112: "Housing", 113: "GroupQuarters", 114: "HealthInsurance",
              115: "HealthInsurance", 116: "HealthInsurance", 117: "HealthInsurance", 118: "QualityMeasures",
              119: "Imputations", 120: "Imputations", 121: "Imputations", 122: "Imputations"}

    topxSet = set()
    for seq in seqs:
        topxSet.add(topics[seq])
    topx = list(topxSet)
    return topx


def get_sequences_within_topic(seqs, topic):
    # takes a list of sequences + a topic & returns only the sequences (from the list given) that make up that topic.
    # e.g. get_sequences_within_topic([2,3,66,67], "AgeSex") will return [2,3]
    topics = {1: "UnweightedCount", 2: "AgeSex", 3: "AgeSex", 4: "Race", 5: "HispanicOrigin", 6: "Ancestry",
              7: "Ancestry", 8: "ForeignBirth", 9: "ForeignBirth", 10: "ForeignBirth", 11: "ForeignBirth",
              12: "ForeignBirth", 13: "PlaceOfBirth", 14: "PlaceOfBirth", 15: "PlaceOfBirth", 16: "ResidenceLastYear",
              17: "ResidenceLastYear", 18: "ResidenceLastYear", 19: "ResidenceLastYear", 20: "ResidenceLastYear",
              21: "ResidenceLastYear", 22: "ResidenceLastYear", 23: "JourneyToWork", 24: "JourneyToWork",
              25: "JourneyToWork", 26: "JourneyToWork", 27: "JourneyToWork", 28: "JourneyToWork", 29: "JourneyToWork",
              30: "JourneyToWork", 31: "JourneyToWork", 32: "JourneyToWork", 33: "JourneyToWork", 34: "Children",
              35: "Grandparents", 36: "HouseholdsFamilies", 37: "HouseholdsFamilies", 38: "MaritalStatus",
              39: "MaritalStatus", 40: "Fertility", 41: "SchoolEnrollment", 42: "SchoolEnrollment", 43: "Education",
              44: "Education", 45: "Language", 46: "Language", 47: "Language", 48: "Poverty", 49: "Poverty",
              50: "Poverty", 51: "Poverty", 52: "Poverty", 53: "Poverty", 54: "Poverty", 55: "Poverty", 56: "Poverty",
              57: "Disability", 58: "Disability", 59: "Income", 60: "Income", 61: "Income", 62: "Income", 63: "Income",
              64: "Income", 65: "Income", 66: "Income", 67: "Earnings", 68: "Earnings", 69: "Earnings", 70: "Earnings",
              71: "Earnings", 72: "Earnings", 73: "Veterans", 74: "Veterans", 75: "TransferPrograms",
              76: "EmploymentStatus", 77: "EmploymentStatus", 78: "EmploymentStatus", 79: "EmploymentStatus",
              80: "Industry", 81: "Industry", 82: "Industry", 83: "Industry", 84: "Industry", 85: "Industry",
              86: "Industry", 87: "Industry", 88: "Industry", 89: "Industry", 90: "Industry", 91: "Industry",
              92: "Industry", 93: "Industry", 94: "Industry", 95: "Industry", 96: "Industry", 97: "Industry",
              98: "Industry", 99: "Industry", 100: "Industry", 101: "Industry", 102: "Industry", 103: "Housing",
              104: "Housing", 105: "Housing", 106: "Housing", 107: "Housing", 108: "Housing", 109: "Housing",
              110: "Housing", 111: "Housing", 112: "Housing", 113: "GroupQuarters", 114: "HealthInsurance",
              115: "HealthInsurance", 116: "HealthInsurance", 117: "HealthInsurance", 118: "QualityMeasures",
              119: "Imputations", 120: "Imputations", 121: "Imputations", 122: "Imputations"}

    likeSequences = []
    for seq in seqs:
        if topics[seq] == topic:
            likeSequences.append(seq)
    return likeSequences


def ensure_dirs(topicAreas, measures):
    # takes a list of topic areas, checks to see if output dirs exist for those topic areas, and, if not, makes the
    # output dirs
    for measure in measures:
        for topic in topicAreas:
            d = os.getcwd() + "/output/ACS2016_5_" + measure + "_" + topic + "/"
            if not os.path.exists(d):
                os.makedirs(d)


def get_sequence_header(seq):
    # takes a sequence number as an argument and returns the sequence header as a list
    header = []
    inFileName = os.getcwd() + "/data/2016_5yr_Summary_FileTemplates/Seq" + str(seq) + ".xls"
    seqFile = xlrd.open_workbook(inFileName)
    sheet = seqFile.sheet_by_index(0)
    numCols = sheet.ncols
    for col in range(6,numCols):
        header.append(sheet.cell_value(0, col))
    return header


def make_file_header_for_summary_level(alikeSeqs, summaryLevel):
    # takes a summary level and a list of "alike sequences," which can be found using the get_sequences_within_topic()
    # and batch_alike_sequences() functions, and returns a concatenated header. The header contains Geo Code column
    # labels for the given summary level and Census ColumnID column labels from each alike sequence. This function is
    # useful for writing files pertaining to a specific summary level, e.g. USA_All_States and USA_ZCTA files.

    topic = get_topic_areas(alikeSeqs)
    if len(topic) != 1:
        raise ValueError('The make_file_header_for_summary_level() function may only be passed sequences from the same topic area')

    summaryLevelGeoHeaders = {10: ["SummaryLevel", "US", "GEOID", "AreaName"],
                              20: ["SummaryLevel", "US", "Region", "GEOID", "AreaName"],
                              30: ["SummaryLevel", "US", "Division", "GEOID", "AreaName"],
                              40: ["SummaryLevel", "State", "StateFIPS", "GEOID", "AreaName"],
                              50: ["SummaryLevel", "State", "StateFIPS", "CountyFIPS", "GEOID", "AreaName"],
                              160: ["SummaryLevel", "State", "StateFIPS", "PlaceFIPS", "GEOID", "AreaName"],
                              320: ["SummaryLevel", "State", "StateFIPS", "CBSACode", "GEOID", "AreaName"],
                              500: ["SummaryLevel", "State", "StateFIPS", "District", "GEOID", "AreaName"],
                              860: ["SummaryLevel", "US", "ZCTA", "GEOID", "AreaName"]}

    if summaryLevel not in summaryLevelGeoHeaders:
        raise ValueError('The make_file_header_for_summary_level() was passed an invalid summary level. Valid options: 10, 20, 30, 40, 50, 160, 320, 500, 860.')

    header = summaryLevelGeoHeaders[summaryLevel]

    full_USA_only_industry_sequences = [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]

    for seq in alikeSeqs:
        if summaryLevel != 10 and seq in full_USA_only_industry_sequences:
            continue
        else:
            header += get_sequence_header(seq)

    return header


def make_file_header_for_geo(alikeSeqs, geoType):
    # takes a geo type (either "state" or "us") and a list of "alike sequences," which can be found using the
    # get_sequences_within_topic() and batch_alike_sequences() functions, and returns a concatenated header as a list.
    # The returned header contains Geo Code column labels for all pertinent summary levels for the given geo type and
    # Census ColumnID column labels from each alike sequence. This function is useful for writing files that contain
    # multiple summary levels, e.g. state files and USA files.

    topic = get_topic_areas(alikeSeqs)
    if len(topic) != 1:
        raise ValueError('The make_file_header_for_geo() function may only be passed sequences from the same topic area.')

    geoTypes = {
        "state": ["SummaryLevel", "State", "StateFIPS", "CountyFIPS", "PlaceFIPS", "CBSACode", "CongressDistrict",
                  "GEOID", "AreaName"],
        "us": ["SummaryLevel", "US", "CensusRegion", "CensusDivision", "GEOID", "AreaName"]}

    if geoType not in geoTypes:
        raise ValueError('The make_file_header_for_geo() was passed an invalid geo type. Valid options: "state" or "us".')

    header = geoTypes[geoType]

    full_USA_only_industry_sequences = [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]

    for seq in alikeSeqs:
        if geoType == "state" and seq in full_USA_only_industry_sequences:
            continue
        else:
            header += get_sequence_header(seq)

    return header


def get_summary_data_dict(seq, EorM, geo):
    # takes a sequence number, geography, and choice of either Estimate or Margin-of-Error ('e' or 'm') and returns
    # a dictionary of all summary file data, using 7 digit Logical Record Numbers (LOGRECNO) as the dictionary key
    summaryData = SortedDict({})
    number = str(seq).zfill(4)
    inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20165" + geo + number + "000.txt"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            summaryData[row[5]] = row[6:]
    return summaryData


def get_summary_data_list(seq, EorM, geo):
    # takes a sequence number, geography, and choice of either Estimate or Margin-of-Error ('e' or 'm')
    # and returns a list of its summary file data, without 7 digit Logical Record Numbers (LOGRECNO)
    summaryData = []
    number = str(seq).zfill(4)
    inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20165" + geo + number + "000.txt"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            summaryData.append(row[6:])
    return summaryData


def get_concatenated_summary_data_dict(alikeSeqs, EorM, geo):
    # takes a list of alike sequences, a choice of either Estimates or Margins-of-error ('e' or 'm'), and a geography
    # and returns a dictionary of concatenated summary file data from all alike sequences, using 7 digit Logical Record
    # Numbers (LOGRECNO) as the dictionary key; uses helper functions get_summary_data_dict() and get_summary_data_list()
    if len(alikeSeqs) == 1:
        summaryData = get_summary_data_dict(alikeSeqs[0], EorM, geo)
    elif len(alikeSeqs) > 1:
        summaryData = get_summary_data_dict(alikeSeqs[0], EorM, geo)
        for i in range(1, len(alikeSeqs)):
            currentSeqData = get_summary_data_list(alikeSeqs[i], EorM, geo)
            j = 0
            for entry in summaryData:
                summaryData[entry] += currentSeqData[j]
                j += 1
    return summaryData


def get_raw_geo_data(geo, sumLvls):
    # takes a geography and a list of summary levels and returns all raw geo data
    # for the given geography at the given summary levels
    sumLvlStrs = []
    for code in sumLvls:
        sumLvlStrs.append(str(code).zfill(3))
    geoCodes = []
    inFileName = os.getcwd() + "/data/5yr_year_geo/2016_ACS_Geography_Files/g20165" + geo + ".csv"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            if row[2] in sumLvlStrs:
                geoCodes.append(row)
    return geoCodes


def get_geo_codes(rawGeoData, sumLvl):
    # takes a summary level and raw geo data, which can be found using get_raw_geo_data(), and returns a dictionary of
    # cleaned geo codes for the given summary level, using 7 digit Logical Record Numbers (LOGRECNO) as the dictionary
    # keys. This function is useful when writing files pertaining to a single summary level, e.g. USA_All_States files
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
        raise ValueError('An invalid summary level was passed to the get_geo_codes() function. Valid options: 10, 20, 30, 40, 50, 160, 320, 500, 860')

    return cleanGeos


def get_all_geo_codes(geo):
    # takes a geo and returns a dictionary of cleaned geo codes for most-pertinent summary levels,
    # using 7 digit Logical Record Numbers (LOGRECNO) as the dictionary keys. This function is useful for writing files
    # pertaining to many summary levels, e.g. state and USA files.
    cleanGeos = SortedDict({})

    inFileName = os.getcwd() + "/data/5yr_year_geo/2016_ACS_Geography_Files/g20165" + geo + ".csv"
    with open(inFileName, 'r', newline='') as inFile:
        reader = csv.reader(inFile, delimiter=',', quotechar='"')
        for row in reader:
            if row[2] == '010':
                geoCache = [10, row[1], '', '', row[48], row[49]]
                cleanGeos[row[4]] = geoCache

            elif row[2] == '020':
                geoCache = [20, row[1], row[6], '', row[48], row[49]]
                cleanGeos[row[4]] = geoCache

            elif row[2] == '030':
                geoCache = [30, row[1], '', row[7], row[48], row[49]]
                cleanGeos[row[4]] = geoCache

            elif row[2] == '040':
                geoCache = [40, row[1], row[9], '', '', '', '', row[48], row[49]]
                cleanGeos[row[4]] = geoCache

            elif row[2] == '050':
                geoCache = [50, row[1], row[9], row[10], '', '', '', row[48], row[49]]
                cleanGeos[row[4]] = geoCache

            elif row[2] == '160':
                geoCache = [160, row[1], row[9], '', row[12], '', '', row[48], row[49]]
                cleanGeos[row[4]] = geoCache

            elif row[2] == '320':
                geoCache = [320, row[1], row[9], '', '', row[22], '', row[48], row[49]]
                cleanGeos[row[4]] = geoCache

            elif row[2] == '500':
                geoCache = [500, row[1], row[9], '', '', '', row[32], row[48], row[49]]
                cleanGeos[row[4]] = geoCache

    return cleanGeos


def batch_alike_sequences(seqs):
    # takes a list of sequences as input and returns a list of those sequences divided into batches based on their topic
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
    Computers = []
    Quality = []
    Imputations = []

    batches = [ Counts, AgeSex, Race, Hispanic, Ancestry, Foreign, Place, Residence, Journey, Children, Grands,
               Households, Marital, Fertility, School, Educational, Language, Poverty, Disability, Income, Earnings,
               Veteran, Transfer, Employment, Industry, Housing, Group, Health, Quality, Imputations ]

    topxDict = { 1: Counts, 2: AgeSex, 3: AgeSex, 4: Race, 5: Hispanic, 6: Ancestry, 7: Ancestry, 8: Foreign,
                 9: Foreign, 10: Foreign, 11: Foreign, 12: Foreign, 13: Place, 14: Place, 15: Place, 16: Residence,
                 17: Residence, 18: Residence, 19: Residence, 20: Residence, 21: Residence, 22: Residence, 23: Journey,
                 24: Journey, 25: Journey, 26: Journey, 27: Journey, 28: Journey, 29: Journey, 30: Journey, 31: Journey,
                 32: Journey, 33: Journey, 34: Children, 35: Grands, 36: Households, 37: Households, 38: Marital,
                 39: Marital, 40: Fertility, 41: School, 42: School, 43: Educational, 44: Educational, 45: Language,
                 46: Language, 47: Language, 48: Poverty, 49: Poverty, 50: Poverty, 51: Poverty, 52: Poverty,
                 53: Poverty, 54: Poverty, 55: Poverty, 56: Poverty, 57: Disability, 58: Disability, 59: Income,
                 60: Income, 61: Income, 62: Income, 63: Income, 64: Income, 65: Income, 66: Income, 67: Earnings,
                 68: Earnings, 69: Earnings, 70: Earnings, 71: Earnings, 72: Earnings, 73: Veteran, 74: Veteran,
                 75: Transfer, 76: Employment, 77: Employment, 78: Employment, 79: Employment, 80: Industry,
                 81: Industry, 82: Industry, 83: Industry, 84: Industry, 85: Industry, 86: Industry, 87: Industry,
                 88: Industry, 89: Industry, 90: Industry, 91: Industry, 92: Industry, 93: Industry, 94: Industry,
                 95: Industry, 96: Industry, 97: Industry, 98: Industry, 99: Industry, 100: Industry, 101: Industry,
                 102: Industry, 103: Housing, 104: Housing, 105: Housing, 106: Housing, 107: Housing, 108: Housing,
                 109: Housing, 110: Housing, 111: Housing, 112: Housing, 113: Group, 114: Health, 115: Health,
                 116: Health, 117: Health, 118: Quality, 119: Imputations, 120: Imputations, 121: Imputations,
                 122: Imputations }

    for seq in seqs:
        topxDict[seq].append(seq)

    return [var for var in batches if var]


def assemble_zcta_file(concatenatedData, geoCodes, header, alikeSeqs, geo, sumLvl, EorM):
    # takes a concatenated summary data dictionary, which can be found using the get_concatenated_summary_data_dict()
    # function, a list of alike sequences, a geography, a summary level, and a choice of either Estimates or Margins-
    # of-error ('e' or 'm') and writes out a geo-coded summary file csv. Use this assemble function to write out
    # USA_ZCTA.csv files.
    topic = get_topic_areas(alikeSeqs)
    if topic.__len__() != 1:
        raise ValueError('The assemble_zcta_file() function may only be passed sequences from the same topic area')

    if sumLvl == 860:
        sumLvlStr = "ZCTA"
    else:
        raise ValueError('An invalid summary level was passed to the assemble_zcta_file() function. Only summary level 860 may be passed.')

    if geo == 'us':
        outFileName = os.getcwd() + "/output/ACS2016_5_" + EorM + "_" + topic[0] + "/USA_" + sumLvlStr + ".csv"
    else:
        raise ValueError('An invalid geography was passed to the assemble_zcta_file() function. Only "us" may be passed.')

    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for entry in geoCodes:
            writer.writerow(geoCodes[entry] + concatenatedData[entry])


def assemble_state_or_usa_file(concatenatedData, geoCodes, header, alikeSeqs, geo, EorM):
    # takes a concatenated summary data dictionary, which can be found using the get_concatenated_summary_data_dict()
    # function, a list of alike sequences, a geography,  and a choice of either Estimates or Margins-of-error ('e' or
    # 'm') and writes out a geo-coded summary file csv. Use this assemble function to write out state and USA.csv files.
    topic = get_topic_areas(alikeSeqs)
    if topic.__len__() != 1:
        raise ValueError('The assemble() function may only be passed sequences from the same topic area')

    if geo == 'us':
        outFileName = os.getcwd() + "/output/ACS2016_5_" + EorM + "_" + topic[0] + "/USA.csv"
    else:
        outFileName = os.getcwd() + "/output/ACS2016_5_" + EorM + "_" + topic[0] + "/" + geo.upper() + ".csv"

    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for entry in geoCodes:
            writer.writerow(geoCodes[entry] + concatenatedData[entry])


def assemble_all_states_file(alikeSeqs, EorM):
    # takes a list of alike sequences and a choice of either Estimates or Margins-of-error ('e' or 'm') and writes out
    # a geo-coded summary file csv. Use this assemble function to write out USA_All_States.csv files.
    topic = get_topic_areas(alikeSeqs)
    if topic.__len__() != 1:
        raise ValueError('The assemble_all_states_file() function may only be passed sequences from the same topic area')

    sumLvl = 40
    outFileName = os.getcwd() + "/output/ACS2016_5_" + EorM + "_" + topic[0] + "/USA_All_States.csv"
    allStates = [  "al", "ak", "az", "ar", "ca", "co", "ct", "dc", "de", "fl", "ga", "hi", "id", "il", "in", "ia", "ks",
                "ky", "la", "me", "md", "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc",
                "nd", "oh", "ok", "or", "pa", "pr", "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy"]

    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(make_file_header_for_summary_level(alikeSeqs, sumLvl))

        for state in allStates:
            geoCodes = []
            stateRow = []
            inFileName = os.getcwd() + "/data/5yr_year_geo/2016_ACS_Geography_Files/g20165" + state + ".csv"
            with open(inFileName, 'r', newline='') as inFile:
                reader = csv.reader(inFile, delimiter=',', quotechar='"')
                rowOne = next(reader)
                geoCodes += [sumLvl, rowOne[1], rowOne[9], rowOne[48], rowOne[49]]

            summaryData = []
            if alikeSeqs.__len__() == 1:
                number = str(alikeSeqs[0]).zfill(4)
                inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20165" + state + number + "000.txt"
                with open(inFileName, 'r', newline='') as inFile:
                    reader = csv.reader(inFile, delimiter=',', quotechar='"')
                    row = next(reader)
                    summaryData += row[6:]
            elif alikeSeqs.__len__() > 1:
                for seq in alikeSeqs:
                    number = str(seq).zfill(4)
                    inFileName = os.getcwd() + "/data/All_Geographies_Not_Tracts_Block_Groups/" + EorM.lower() + "20165" + state + number + "000.txt"
                    with open(inFileName, 'r', newline='') as inFile:
                        reader = csv.reader(inFile, delimiter=',', quotechar='"')
                        row = next(reader)
                        summaryData += row[6:]

            stateRow += geoCodes + summaryData
            writer.writerow(stateRow)


def write_column_key(seqs, EorM):
    # takes a list of sequences and a choice of either Estimates or Margins-of-error ('e' or 'm') and writes out a
    # column key metadata csv pertaining to a specific summary file. This column key lists ColumnID and ColumnDescription
    # pairs for every estimate or margin-of-error column of its summary file.
    topic = get_topic_areas(seqs)
    outFileName = os.getcwd() + "/output/ACS2016_5_" + EorM + "_" + topic[0] + "/" + "02_ColumnKey.csv"
    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ["ColumnID" , "ColumnDescription", "TopicArea"]
        writer.writerow(header)
        for seq in seqs:
            inFileName = os.getcwd() + "/data/2016_5yr_Summary_FileTemplates/Seq" + str(seq) + ".xls"
            seqFile = xlrd.open_workbook(inFileName)
            sheet = seqFile.sheet_by_index(0)
            numCols = sheet.ncols
            for col in range(6,numCols):
                columnMetadata = []
                columnMetadata.append(str.lower(sheet.cell_value(0, col)))
                columnMetadata.append(sheet.cell_value(1, col))
                columnMetadata.append(topic[0])
                writer.writerow(columnMetadata)


def write_table_key(seqs, EorM):
    # takes a list of sequences and a choice of either Estimates or Margins-of-error ('e' or 'm') and writes out a
    # column key metadata csv pertaining to a specific summary file. This column key lists ColumnID and ColumnDescription
    # pairs for every estimate or margin-of-error column of its summary file.
    topic = get_topic_areas(seqs)
    outFileName = os.getcwd() + "/output/ACS2016_5_" + EorM + "_" + topic[0] + "/" + "01_TableKey.csv"
    with open(outFileName, 'w+', newline='') as outFile:
        writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ["TableID", "TableDescription", "NumColumns", "TopicArea"]
        writer.writerow(header)
        inFileName = os.getcwd() + "/documentation/user_tools/ACS_5yr_Seq_Table_Number_Lookup_CLEANED.xls"
        tableLookup = xlrd.open_workbook(inFileName)
        sheet = tableLookup.sheet_by_index(0)
        numRows = sheet.nrows
        for row in range(1, numRows):
            if sheet.cell_value(row, 2) in seqs:
                tableMetadata = []
                tableMetadata.append(str.lower(sheet.cell_value(row, 1)))
                tableMetadata.append(sheet.cell_value(row, 7))
                tableMetadata.append(sheet.cell_value(row, 5))
                tableMetadata.append(topic[0])
                writer.writerow(tableMetadata)


def write_json_columnkey(seqs, EorM):
    # does effectively the same thing as write_column_key() but the output format is JSON
    topic = get_topic_areas(seqs)
    outFileName = os.getcwd() + "/output/ACS2016_5_" + EorM + "_" + topic[0] + "/" + "03_ColumnKey.json"
    with open(outFileName, 'w') as outFile:
        outFile.write('[\n')
        i = 0
        for seq in seqs:
            i += 1
            inFileName = os.getcwd() + "/data/2016_5yr_Summary_FileTemplates/Seq" + str(seq) + ".xls"
            seqFile = xlrd.open_workbook(inFileName)
            sheet = seqFile.sheet_by_index(0)
            numCols = sheet.ncols
            for col in range(6,numCols):
                if col == numCols-1 and i == len(seqs):
                    columnMetadata = {"columnname": str.lower(sheet.cell_value(0, col)),"description":sheet.cell_value(1, col)}
                    json.dump(columnMetadata, outFile, sort_keys=True, indent=2)
                else:
                    columnMetadata = {"columnname": str.lower(sheet.cell_value(0, col)), "description": sheet.cell_value(1, col)}
                    json.dump(columnMetadata, outFile, sort_keys=True, indent=2)
                    outFile.write(',\n')
        outFile.write('\n]\n')

############
""" Main """

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Assemble large batches of ACS Summary Files")
    parser.add_argument("-m", "--measures", nargs='*', type=str, choices=["E", "M"], default="E",
                        help="A list of measures to include in the output (E=Population Estimates; M=Margins-of-Error)")
    parser.add_argument("-g", "--geos", nargs='*', type=str,
                        choices=['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi', 'id', 'il',
                                 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne',
                                 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'pr', 'ri', 'sc',
                                 'sd', 'tn', 'tx', 'us', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy', 'all'],
                        default=['all'],
                        help="Geos (states, territories) to include in the output. EITHER, simply use 'all' to include every state, DC, Puerto Rico, and the USA (e.g. \"-g all\"), OR, provide a list of desired geos from the following: lowercase two-character state postal abbreviations, 'dc' for Washington, D.C., 'pr' for Puerto Rico, and 'us' for USA (e.g. \"-g ak dc us wy\"). If the 'all' argument is passed at all (e.g. \"-g ak wy all\") the program assumes all geos should be used.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--topics", nargs='*', type=str,
                        choices=['UnweightedCount', 'AgeSex', 'Race', 'HispanicOrigin', 'Ancestry', 'ForeignBirth',
                                 'PlaceOfBirth', 'ResidenceLastYear', 'JourneyToWork', 'Children', 'Grandparents',
                                 'HouseholdsFamilies', 'MaritalStatus', 'Fertility', 'SchoolEnrollment', 'Education',
                                 'Language', 'Poverty', 'Disability', 'Income', 'Earnings', 'Veterans',
                                 'TransferPrograms', 'EmploymentStatus', 'Industry', 'Housing', 'GroupQuarters',
                                 'HealthInsurance', 'QualityMeasures', 'Imputations', 'all'],
                        default=['AgeSex','Race','HispanicOrigin','Ancestry','ForeignBirth','PlaceOfBirth',
                                 'ResidenceLastYear','SchoolEnrollment','Education','Language','Poverty','Income',
                                 'Earnings','EmploymentStatus','Housing','HealthInsurance'],
                        help="Topic areas to include in the output")
    group.add_argument("-s", "--sequences", nargs='*', type=int, choices=range(1, 123),
                       help="Sequences to include in the output (Caution: This argument overrides the default topic areas, and appropriate sequence numbers are required to use it. New users and those unfamiliar with ACS Summary File sequence template files are recommended to assemble files using the --topics -t argument instead of the --sequences -s argument.)")

#    parser.add_argument("-y" "--year", type=int, choices=[2015],
#                        help="Reference Year (2015 is currently the only valid option for year)")
    args = parser.parse_args()

    measures = args.measures

    if 'all' in args.geos:
        geos = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks',
                'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc',
                'nd', 'oh', 'ok', 'or', 'pa', 'pr', 'ri', 'sc', 'sd', 'tn', 'tx', 'us', 'ut', 'vt', 'va', 'wa', 'wv',
                'wi', 'wy']
    else:
        geos = args.geos

    if args.sequences:
        sequences = args.sequences
        topicAreas = get_topic_areas(sequences)
        ensure_dirs(topicAreas, measures)
        batches = batch_alike_sequences(sequences)
    elif args.topics:
        if 'all' in args.topics:
            topicAreas = ['UnweightedCount', 'AgeSex', 'Race', 'HispanicOrigin', 'Ancestry', 'ForeignBirth',
                          'PlaceOfBirth', 'ResidenceLastYear', 'JourneyToWork', 'Children', 'Grandparents',
                          'HouseholdsFamilies', 'MaritalStatus', 'Fertility', 'SchoolEnrollment', 'Education',
                          'Language', 'Poverty', 'Disability', 'Income', 'Earnings', 'Veterans', 'TransferPrograms',
                          'EmploymentStatus', 'Industry', 'Housing', 'GroupQuarters', 'HealthInsurance',
                          'QualityMeasures', 'Imputations']
        else:
            topicAreas = args.topics
        ensure_dirs(topicAreas, measures)
        batches = []
        topicsDict = {
            "UnweightedCount": [1],
            "AgeSex": [2, 3],
            "Race": [4],
            "HispanicOrigin": [5],
            "Ancestry": [6, 7],
            "ForeignBirth": [8, 9, 10, 11, 12],
            "PlaceOfBirth": [13, 14, 15],
            "ResidenceLastYear": [16, 17, 18, 19, 20, 21, 22],
            "JourneyToWork": [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
            "Children": [34],
            "Grandparents": [35],
            "HouseholdsFamilies": [36, 37],
            "MaritalStatus": [38, 39],
            "Fertility": [40],
            "SchoolEnrollment": [41, 42],
            "Education": [43, 44],
            "Language": [45, 46, 47],
            "Poverty": [48, 49, 50, 51, 52, 53, 54, 55, 56],
            "Disability": [57, 58],
            "Income": [59, 60, 61, 62, 63, 64, 65, 66],
            "Earnings": [67, 68, 69, 70, 71, 72],
            "Veterans": [73, 74],
            "TransferPrograms": [75],
            "EmploymentStatus": [76, 77, 78, 79],
            "Industry": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102],
            "Housing": [103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
            "GroupQuarters": [113],
            "HealthInsurance": [114, 115, 116, 117],
            "QualityMeasures": [118],
            "Imputations": [119, 120, 121, 122]
        }
        for topic in topicAreas:
            batches.append(topicsDict[topic])

    for area in geos:
        if area == 'us':
            print(area + ". Getting geo codes for non-zip geos.")
            allUSGeosNoZIPs = get_all_geo_codes(area)
            print(area + ". Getting geo codes for zips.")
            USGeosForZIPs = get_geo_codes(get_raw_geo_data(area,[860]),860)
            for batch in batches:
                print(area + ". Making file header")
                topRowForRolledUpFile = make_file_header_for_geo(batch,'us')
                print(area + ". Making file header for ZCTA file")
                topRowForZCTAFile = make_file_header_for_summary_level(batch,860)
                for measure in measures:
                    print("working on " + area + "_" + str(batch) + "_" + measure)
                    summaryDataDict = get_concatenated_summary_data_dict(batch,measure,area)
                    assemble_state_or_usa_file(summaryDataDict, allUSGeosNoZIPs, topRowForRolledUpFile, batch, area, measure)
                    assemble_zcta_file(summaryDataDict, USGeosForZIPs, topRowForZCTAFile, batch, area, 860, measure)
        else:
            print("State: " + area + ". Getting geo codes.")
            geoData = get_all_geo_codes(area)
            for batch in batches:
                print("Making file header.")
                topRow = make_file_header_for_geo(batch,'state')
                for measure in measures:
                    print("working on " + area + "_" + str(batch) + "_" + measure)
                    summaryDataDict = get_concatenated_summary_data_dict(batch,measure,area)
                    assemble_state_or_usa_file(summaryDataDict, geoData, topRow, batch, area, measure)

    # TO-DO: fix so that it doesn't automatically run this portion every time, even when only giving 1 state as an
    # argument, for instance
    for batch in batches:
        for measure in measures:
            print("working on all states files for " + str(batch) + "_" + measure)
            write_column_key(batch, measure)
            write_json_columnkey(batch, measure)
            write_table_key(batch, measure)
            assemble_all_states_file(batch, measure)
