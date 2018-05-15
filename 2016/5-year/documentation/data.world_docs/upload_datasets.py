from collections import OrderedDict
import datadotworld as dw
import requests
import time
import json
import csv
import os

# Important variables

TOKEN = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJwcm9kLXVzZXItY2xpZW50OnVzY2Vuc3VzYnVyZWF1IiwiaXNzIjoiYWdlbnQ6dXNjZW5zdXNidXJlYXU6OmUyNjJjMWI3LTljYWEtNDdiOC1iNWRlLWFhYjRhNmY3OWM3MSIsImlhdCI6MTQ4NDA4MzI2Miwicm9sZSI6WyJ1c2VyX2FwaV9yZWFkIiwidXNlcl9hcGlfd3JpdGUiXSwiZ2VuZXJhbC1wdXJwb3NlIjp0cnVlfQ.P9pu3eLchtZu59zT56i2zYgGbFjrjZbEq-3g097qG5xm1kE9rCJ5_FsX5cWUu7HNbJOH9z_EX3BA43V5gN_KPQ'

CLIENT = dw.api_client()

DATASETS = OrderedDict()
#DATASETS['ACS_2016_5_M_Imputations'] = 'acs-2016-5-m-imputations'
DATASETS['ACS_2016_5_E_Imputations'] = 'acs-2016-5-e-imputations'
DATASETS['ACS_2016_5_M_QualityMeasures'] = 'acs-2016-5-m-qualitymeasures'
DATASETS['ACS_2016_5_E_QualityMeasures'] = 'acs-2016-5-e-qualitymeasures'
DATASETS['ACS_2016_5_M_HealthInsurance'] = 'acs-2016-5-m-healthinsurance'
DATASETS['ACS_2016_5_E_HealthInsurance'] = 'acs-2016-5-e-healthinsurance'
DATASETS['ACS_2016_5_M_GroupQuarters'] = 'acs-2016-5-m-groupquarters'
DATASETS['ACS_2016_5_E_GroupQuarters'] = 'acs-2016-5-e-groupquarters'
DATASETS['ACS_2016_5_M_Housing'] = 'acs-2016-5-m-housing'
DATASETS['ACS_2016_5_E_Housing'] = 'acs-2016-5-e-housing'
DATASETS['ACS_2016_5_M_Industry'] = 'acs-2016-5-m-industry'
DATASETS['ACS_2016_5_E_Industry'] = 'acs-2016-5-e-industry'
DATASETS['ACS_2016_5_M_EmploymentStatus'] = 'acs-2016-5-m-employmentstatus'
DATASETS['ACS_2016_5_E_EmploymentStatus'] = 'acs-2016-5-e-employmentstatus'
DATASETS['ACS_2016_5_M_TransferPrograms'] = 'acs-2016-5-m-transferprograms'
DATASETS['ACS_2016_5_E_TransferPrograms'] = 'acs-2016-5-e-transferprograms'
DATASETS['ACS_2016_5_M_Veterans'] = 'acs-2016-5-m-veterans'
DATASETS['ACS_2016_5_E_Veterans'] = 'acs-2016-5-e-veterans'
DATASETS['ACS_2016_5_M_Earnings'] = 'acs-2016-5-m-earnings'
DATASETS['ACS_2016_5_E_Earnings'] = 'acs-2016-5-e-earnings'
DATASETS['ACS_2016_5_M_Income'] = 'acs-2016-5-m-income'
DATASETS['ACS_2016_5_E_Income'] = 'acs-2016-5-e-income'
DATASETS['ACS_2016_5_M_Disability'] = 'acs-2016-5-m-disability'
DATASETS['ACS_2016_5_E_Disability'] = 'acs-2016-5-e-disability'
DATASETS['ACS_2016_5_M_Poverty'] = 'acs-2016-5-m-poverty'
DATASETS['ACS_2016_5_E_Poverty'] = 'acs-2016-5-e-poverty'
DATASETS['ACS_2016_5_M_Language'] = 'acs-2016-5-m-language'
DATASETS['ACS_2016_5_E_Language'] = 'acs-2016-5-e-language'
DATASETS['ACS_2016_5_M_Education'] = 'acs-2016-5-m-education'
DATASETS['ACS_2016_5_E_Education'] = 'acs-2016-5-e-education'
DATASETS['ACS_2016_5_M_SchoolEnrollment'] = 'acs-2016-5-m-schoolenrollment'
DATASETS['ACS_2016_5_E_SchoolEnrollment'] = 'acs-2016-5-e-schoolenrollment'
DATASETS['ACS_2016_5_M_Fertility'] = 'acs-2016-5-m-fertility'
DATASETS['ACS_2016_5_E_Fertility'] = 'acs-2016-5-e-fertility'
DATASETS['ACS_2016_5_M_MaritalStatus'] = 'acs-2016-5-m-maritalstatus'
DATASETS['ACS_2016_5_E_MaritalStatus'] = 'acs-2016-5-e-maritalstatus'
DATASETS['ACS_2016_5_M_HouseholdsFamilies'] = 'acs-2016-5-m-householdsfamilies'
DATASETS['ACS_2016_5_E_HouseholdsFamilies'] = 'acs-2016-5-e-householdsfamilies'
DATASETS['ACS_2016_5_M_Grandparents'] = 'acs-2016-5-m-grandparents'
DATASETS['ACS_2016_5_E_Grandparents'] = 'acs-2016-5-e-grandparents'
DATASETS['ACS_2016_5_M_Children'] = 'acs-2016-5-m-children'
DATASETS['ACS_2016_5_E_Children'] = 'acs-2016-5-e-children'
DATASETS['ACS_2016_5_M_JourneyToWork'] = 'acs-2016-5-m-journeytowork'
DATASETS['ACS_2016_5_E_JourneyToWork'] = 'acs-2016-5-e-journeytowork'
DATASETS['ACS_2016_5_M_ResidenceLastYear'] = 'acs-2016-5-m-residencelastyear'
DATASETS['ACS_2016_5_E_ResidenceLastYear'] = 'acs-2016-5-e-residencelastyear'
DATASETS['ACS_2016_5_M_PlaceOfBirth'] = 'acs-2016-5-m-placeofbirth'
DATASETS['ACS_2016_5_E_PlaceOfBirth'] = 'acs-2016-5-e-placeofbirth'
DATASETS['ACS_2016_5_M_ForeignBirth'] = 'acs-2016-5-m-foreignbirth'
DATASETS['ACS_2016_5_E_ForeignBirth'] = 'acs-2016-5-e-foreignbirth'
DATASETS['ACS_2016_5_M_Ancestry'] = 'acs-2016-5-m-ancestry'
DATASETS['ACS_2016_5_E_Ancestry'] = 'acs-2016-5-e-ancestry'
DATASETS['ACS_2016_5_M_HispanicOrigin'] = 'acs-2016-5-m-hispanicorigin'
DATASETS['ACS_2016_5_E_HispanicOrigin'] = 'acs-2016-5-e-hispanicorigin'
DATASETS['ACS_2016_5_M_Race'] = 'acs-2016-5-m-race'
DATASETS['ACS_2016_5_E_Race'] = 'acs-2016-5-e-race'
DATASETS['ACS_2016_5_M_AgeSex'] = 'acs-2016-5-m-agesex'
DATASETS['ACS_2016_5_E_AgeSex'] = 'acs-2016-5-e-agesex'


FILENAMES = [ '01_TableKey.csv', '02_ColumnKey.csv', 'AK.csv', 'AL.csv', 'AR.csv', 'AZ.csv', 'CA.csv', 'CO.csv', 'CT.csv', 'DC.csv', 'DE.csv', 'FL.csv', 'GA.csv', 'HI.csv', 'IA.csv', 'ID.csv', 'IL.csv', 'IN.csv', 'KS.csv', 'KY.csv', 'LA.csv', 'MA.csv', 'MD.csv', 'ME.csv', 'MI.csv', 'MN.csv', 'MO.csv', 'MS.csv', 'MT.csv', 'NC.csv', 'ND.csv', 'NE.csv', 'NH.csv', 'NJ.csv', 'NM.csv', 'NV.csv', 'NY.csv', 'OH.csv', 'OK.csv', 'OR.csv', 'PA.csv', 'PR.csv', 'RI.csv', 'SC.csv', 'SD.csv', 'TN.csv', 'TX.csv', 'USA.csv', 'USA_All_States.csv', 'USA_ZCTA.csv', 'UT.csv', 'VA.csv', 'VT.csv', 'WA.csv', 'WI.csv', 'WV.csv', 'WY.csv' ]

FILE_DESCRIPTIONS = {'00_README.md': {'description': 'ACS_2016_5_E README'}, '01_TableKey.csv': {'description': 'Metadata file detailing specific topics contained in this dataset'}, '02_ColumnKey.csv': {'description': 'Metadata file detailing Column ID and Column Description for all population estimate columns contained in this dataset'}, 'AK.csv': {'description': 'Alaska'}, 'AL.csv': {'description': 'Alabama'}, 'AR.csv': {'description': 'Arkansas'}, 'AZ.csv': {'description': 'Arizona'}, 'CA.csv': {'description': 'California'}, 'CO.csv': {'description': 'Colorado'}, 'CT.csv': {'description': 'Connecticut'}, 'DC.csv': {'description': 'Washington, D.C.'}, 'DE.csv': {'description': 'Delaware'}, 'FL.csv': {'description': 'Florida'}, 'GA.csv': {'description': 'Georgia'}, 'HI.csv': {'description': 'Hawaii'}, 'IA.csv': {'description': 'Iowa'}, 'ID.csv': {'description': 'Idaho'}, 'IL.csv': {'description': 'Illinois'}, 'IN.csv': {'description': 'Indiana'}, 'KS.csv': {'description': 'Kansas'}, 'KY.csv': {'description': 'Kentucky'}, 'LA.csv': {'description': 'Louisiana'}, 'MA.csv': {'description': 'Massachusetts'}, 'MD.csv': {'description': 'Maryland'}, 'ME.csv': {'description': 'Maine'}, 'MI.csv': {'description': 'Michigan'}, 'MN.csv': {'description': 'Minnesota'}, 'MO.csv': {'description': 'Missouri'}, 'MS.csv': {'description': 'Mississippi'}, 'MT.csv': {'description': 'Montana'}, 'NC.csv': {'description': 'North Carolina'}, 'ND.csv': {'description': 'North Dakota'}, 'NE.csv': {'description': 'Nebraska'}, 'NH.csv': {'description': 'New Hampshire'}, 'NJ.csv': {'description': 'New Jersey'}, 'NM.csv': {'description': 'New Mexico'}, 'NV.csv': {'description': 'Nevada'}, 'NY.csv': {'description': 'New York'}, 'OH.csv': {'description': 'Ohio'}, 'OK.csv': {'description': 'Oklahoma'}, 'OR.csv': {'description': 'Oregon'}, 'PA.csv': {'description': 'Pennsylvania'}, 'PR.csv': {'description': 'Puerto Rico'}, 'RI.csv': {'description': 'Rhode Island'}, 'SC.csv': {'description': 'South Carolina'}, 'SD.csv': {'description': 'South Dakota'}, 'TN.csv': {'description': 'Tennessee'}, 'TX.csv': {'description': 'Texas'}, 'USA.csv': {'description': 'Full USA and geographies larger than states'}, 'USA_All_States.csv': {'description': 'All states'}, 'USA_ZCTA.csv': {'description': 'ZIP Code Tabulation Areas (ZCTA/ZIP code)'}, 'UT.csv': {'description': 'Utah'}, 'VA.csv': {'description': 'Virginia'}, 'VT.csv': {'description': 'Vermont'}, 'WA.csv': {'description': 'Washington'}, 'WI.csv': {'description': 'Wisconsin'}, 'WV.csv': {'description': 'West Virginia'}, 'WY.csv': {'description': 'Wyoming'}}

## Functions

def main():
    # the main function
    
    # iterate through DATASETS; on each dataset
    for dataset in DATASETS:
        
        # create a private shell dataset
        print('Creating {}'.format(dataset))
        createDataset(dataset)

        # upload files
        print('Uploading files to {}'.format(dataset))
        uploadDatasetFiles(dataset)
        print('Files sent to {}'.format(dataset))
    
        # wait 30 seconds
        print('Sleeping 30sec')
        time.sleep(30)

        # check if the dataset is INPROGRESS, LOADED, ERROR
        print('Checking status')
        status = checkDatasetStatus(dataset)
        print('Status is {}'.format(status))

        # if it's not LOADED yet
        while status != 'LOADED':
            
            # wait another minute
            print('Waiting 60sec')
            time.sleep(60)

            # and check again
            print('Checking status again')
            status = checkDatasetStatus(dataset)
            print('Status is {}'.format(status))
            
            # if the dataset has status `ERROR`, raise an error an quit
            if status == 'ERROR':
                raise RuntimeError('There has been a failure while uploading files to the {} dataset'.format(dataset))
        
        # when it's LOADED
        else:
            print('Uploading metadata')
            # send up the dataset metadata
            uploadMetadata(dataset)

    print("Done!")


def createDataset(dataset_name):
    # this function takes a dataset_name and creates a dataset shell (with no files or metadata) in private mode

    url = "https://api.data.world/v0/datasets/uscensusbureau"
    payload = "{\n  \"title\": \"" + dataset_name +"\",\n  \"visibility\": \"PRIVATE\"\n}"
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(TOKEN)
        }
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def uploadDatasetFiles(dataset_name):
    # this function takes a dataset_name and uploads its files from disk

    dir_path = "/Users/jonathanortiz/code/ACS_SummaryFiles/2016/5-year/output/{}/".format(dataset_name)
    file_paths = [dir_path + file_name for file_name in FILENAMES]
    file_paths.append("/Users/jonathanortiz/code/ACS_SummaryFiles/2016/5-year/documentation/data.world_docs/00_README.md")

    CLIENT.upload_files('uscensusbureau/{}'.format(DATASETS[dataset_name]), file_paths, FILE_DESCRIPTIONS)


def checkDatasetStatus(dataset_name):
    # this function takes a dataset_name and returns the dataset status (e.g. INPROGRESS, LOADED, etc.)

    url = 'https://api.data.world/v0/datasets/uscensusbureau/{}'.format(DATASETS[dataset_name])
    headers = { 'authorization': 'Bearer {}'.format(TOKEN) }
    response = requests.request('GET', url, headers=headers)
    parsed_response = json.loads(response.text)

    return parsed_response['status']

def uploadMetadata(dataset_name):

    metadata_file = "/Users/jonathanortiz/code/ACS_SummaryFiles/2016/5-year/documentation/data.world_docs/metadata-resource.csv"
    
    with open(metadata_file, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] == dataset_name:
                metadata = row

    if dataset_name[11] == 'E':
        payload = "{\n  \"description\": \"US Census population estimates, " + metadata[2] + " (American Community Survey, 2012-2016)\",\n  \"summary\": \"# Get Started\\n\\nWelcome to the **American Community Survey (ACS) - " + metadata[2] + "** summary files. This dataset includes population estimates pertaining to the US Census **" + metadata[2] + "** topic area.\\n\\nNew users are strongly encouraged to review the `00_README.md` documentation before using this data source.\\n\\n## Summary File Dataset Structure\\n\\nEach ACS Dataset pertains to one specific Topic Area and is divided into 57 separate CSV files -\\n\\n* 1 for each of the US states, Puerto Rico, and Washington D.C (52 total)\\n* 3 USA files\\n* 2 metadata records\\n\\nUsers may download these files for offline analysis, but the real value of this new distribution format is in using the data.world query tool to join ACS estimates to users' own data.\\n\\n## Finding The Data You Need\\n\\nUsers must consider 3 inputs to find the data they are looking for in the summary files:\\n\\n 1. Topic Area\\n 2. Column IDs\\n 3. Summary Level or Geography\\n\\n### Topic Area\\ndata.world ACS Summary File datasets are already split across Topic Areas. This dataset focuses on the " + metadata[2] + " topic area. If you are looking for another topic area, go back to [data.world/uscensusbureau](https://data.world/uscensusbureau) to find the one you are looking for.\\n\\nFederated queries across multiple Topic Areas are possible with the data.world query tool. Please refer to the [data.world's SQL Tutorial](https://docs.data.world/documentation/sql/concepts/dw_specific/federated_queries.html) for more info.\\n\\n### Column IDs\\nColumn ID numbers are required to query the data using the data.world query tool. Experienced Census users will recognize these Column IDs from ACS data from other distribution channels like the Census API and ACS R package. Column IDs are opaque, coded column headers that offer a great shorthand for `SELECT`ing the estimates you need in a query, but new users will need to explore the metadata file `02_ColumnKey.csv` to determine the columns they need.\\n\\nThe `02_ColumnKey.csv` metadata file is included as a machine-readable CSV so users can query it with the data.world query tool as well.\\n\\n### Summary Level or Geography\\nAll rows in the data.world ACS Summary File datasets are pre-geocoded. Geography codes like standard State Postal Abbreviations, State FIPS, County FIPS, Place FIPS, CBSA, ZCTA/ZIP, and Census GEOID codes are included to facilitate easy joining to users' own datasets. Experienced users may use the same Summary Levels available on other channels like the American FactFinder website. For more information about Summary Levels, please refer to the `00_README.md` documentation.\\n\\nWith the exception of the **USA\\\\_All\\\\_States** files, the USA-level files do not contain geographies that are always entirely within a state, such as counties and places; for those data, go to the file for that state. ZIP Code Tabulation Areas are in the United States level (`USA_ZCTA.csv`), because some ZIP codes span more than one state.\\n\\nMulti-table Select queries across multiple state files are possible with the data.world query tool. Please refer to the [data.world's SQL Tutorial](https://docs.data.world/documentation/sql/concepts/dw_specific/multi-tables.html) for more info.\\n\\n### Tips and Notes\\n\\n* The `USA_All_States.csv` is provided for convenience so that users do not need to federate across all individual state files to return estimates for every state in the US.\\n* Make your queries as selective as possible. Less selective queries will take longer to run and some may not return results at all due to the query timeout limit of 60 seconds. If you receive a `Network Error` upon querying the data, your query likely timed out and you should try a smaller slice of the data.\\n* Most summary files are too wide to display in their entirety using data.world's fullscreen data table viewer. The data table viewer will stop displaying columns after the first 50. To view columns beyond the first 50, use the data.world query tool or download the file for offline analysis.\",\n  \"tags\": [ \"census\", \"census bureau\", \"us census\", \"acs\", \"american community survey\", \"united states\", \"us\", \"usa\", " + metadata[3] + " ],\n  \"license\": \"Public Domain\"\n}"
    else:
        payload = "{\n  \"description\": \"US Census margins of error for " + metadata[2] + " estimates (American Community Survey, 2012-2016)\",\n  \"summary\": \"## **Please note!** _This dataset contains margins of error for the following dataset [" + metadata[0] + "](https://data.world/uscensusbureau/" + metadata[1] + ")._\\n\\n# Get Started\\n\\nWelcome to the **American Community Survey (ACS) - " + metadata[2] + "** summary files. This dataset includes population estimates pertaining to the US Census **" + metadata[2] +"** topic area.\\n\\nNew users are strongly encouraged to review the `00_README.md` documentation before using this data source.\\n\\n## Summary File Dataset Structure\\n\\nEach ACS Dataset pertains to one specific Topic Area and is divided into 57 separate CSV files -\\n\\n* 1 for each of the US states, Puerto Rico, and Washington D.C (52 total)\\n* 3 USA files\\n* 2 metadata records\\n\\nUsers may download these files for offline analysis, but the real value of this new distribution format is in using the data.world query tool to join ACS estimates to users' own data.\\n\\n## Finding The Data You Need\\n\\nUsers must consider 3 inputs to find the data they are looking for in the summary files:\\n\\n 1. Topic Area\\n 2. Column IDs\\n 3. Summary Level or Geography\\n\\n### Topic Area\\ndata.world ACS Summary File datasets are already split across Topic Areas. This dataset focuses on the " + metadata[2] + " topic area. If you are looking for another topic area, go back to [data.world/uscensusbureau](https://data.world/uscensusbureau) to find the one you are looking for.\\n\\nFederated queries across multiple Topic Areas are possible with the data.world query tool. Please refer to the [data.world's SQL Tutorial](https://docs.data.world/documentation/sql/concepts/dw_specific/federated_queries.html) for more info.\\n\\n### Column IDs\\nColumn ID numbers are required to query the data using the data.world query tool. Experienced Census users will recognize these Column IDs from ACS data from other distribution channels like the Census API and ACS R package. Column IDs are opaque, coded column headers that offer a great shorthand for `SELECT`ing the estimates you need in a query, but new users will need to explore the metadata file `02_ColumnKey.csv` to determine the columns they need.\\n\\nThe `02_ColumnKey.csv` metadata file is included as a machine-readable CSV so users can query it with the data.world query tool as well.\\n\\n### Summary Level or Geography\\nAll rows in the data.world ACS Summary File datasets are pre-geocoded. Geography codes like standard State Postal Abbreviations, State FIPS, County FIPS, Place FIPS, CBSA, ZCTA/ZIP, and Census GEOID codes are included to facilitate easy joining to users' own datasets. Experienced users may use the same Summary Levels available on other channels like the American FactFinder website. For more information about Summary Levels, please refer to the `00_README.md` documentation.\\n\\nWith the exception of the **USA\\\\_All\\\\_States** files, the USA-level files do not contain geographies that are always entirely within a state, such as counties and places; for those data, go to the file for that state. ZIP Code Tabulation Areas are in the United States level (`USA_ZCTA.csv`), because some ZIP codes span more than one state.\\n\\nMulti-table Select queries across multiple state files are possible with the data.world query tool. Please refer to the [data.world's SQL Tutorial](https://docs.data.world/documentation/sql/concepts/dw_specific/multi-tables.html) for more info.\\n\\n### Tips and Notes\\n\\n* The `USA_All_States.csv` is provided for convenience so that users do not need to federate across all individual state files to return estimates for every state in the US.\\n* Make your queries as selective as possible. Less selective queries will take longer to run and some may not return results at all due to the query timeout limit of 60 seconds. If you receive a `Network Error` upon querying the data, your query likely timed out and you should try a smaller slice of the data.\\n* Most summary files are too wide to display in their entirety using data.world's fullscreen data table viewer. The data table viewer will stop displaying columns after the first 50. To view columns beyond the first 50, use the data.world query tool or download the file for offline analysis.\",\n  \"tags\": [ \"census\", \"census bureau\", \"us census\", \"acs\", \"american community survey\", \"united states\", \"us\", \"usa\", " + metadata[3] + " ],\n  \"license\": \"Public Domain\"\n}"

    url = "https://api.data.world/v0/datasets/uscensusbureau/{}".format(DATASETS[dataset_name])
    
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(TOKEN)
        }

    response = requests.request("PATCH", url, data=payload, headers=headers)

    print(response.text)

if __name__ == '__main__':
    main()
