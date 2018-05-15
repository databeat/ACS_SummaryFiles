# ACS2016_5_E README

#### Developed by data.world

#### In partnership with the US Census Bureau


## 1.0 - The American Community Survey
The American Community Survey (ACS) is part of the U.S. Census Bureau's Decennial Census Program and is designed to provide current demographic, social, economic, and housing estimates throughout the decade. The ACS provides information on more than 40 topics, including educational attainment, language spoken at home, ability to speak English, the foreign-born, marital status, migration, and many more. Each year the survey randomly samples around 3.5 million addresses and produces statistics that cover 1-year and 5-year periods for geographic areas in the United States and Puerto Rico, ranging from neighborhoods to congressional districts to the entire nation. For more information about the ACS, please visit our main page at: [www.census.gov/acs](http://www.census.gov/acs). ACS data are published through a number of channels, including American FactFinder, QuickFacts, as well as the Census Bureau’s Application Programming Interface (API). This document will brief data users on the contents of the ACS Summary Files stored on data.world and explain how they can use them to obtain statistics.

## 2.0 - Description
The 2012-2016 American Community Survey 5-year estimates (datasets beginning with `ACS2016_5_E` in data.world) include results from both the American Community Survey (ACS) and the Puerto Rico Community Survey (PRCS). The statistics presented describe the entire data collection period, from January 1, 2012 to December 31, 2016. The 2012-2016 ACS 5-year data products include estimates of demographic, social, housing and economic characteristics for people living in housing units and group quarters.

## 3.0 - New Features
The ACS Summary File datasets on data.world provide new features not available anywhere else:

### 3.1 - Geo Coding
All estimates in the ACS Summary File datasets on data.world include multiple geographical codes to help users find the estimates and margins-of-error they are looking for. In addition to common geographic area names, the data also contain Federal Information Processing Standard (FIPS) codes for states, counties, and places, Core-Based Statistical Area (CBSA) codes for Metro- and Micropolitan Statistical Areas (MSAs), as well as full Census GEOID codes for every geographic entity in the data.

> How is this different than other ACS Summary Files?
> 
> Since the ACS Summary File Detailed Tables contain a large number of
> cells, the tables are typically stored in a series of files with only
> the data from the tables, without such information as the title of the
> tables, the description of the rows, and the names of the geographic
> areas. That information (or metadata) is in other files and templates
> that the user must typically merge with the data files to reproduce
> the tables. data.world has performed this geo coding for the user.

### 3.2 - SQL Queries and Joins
Data users can query the summary files with SQL using the data.world query tool. 

 - Select portions of the data by Topic Area, Table, Column, Summary Level, and Geography
 - Apply computations and summary statistics to the Summary File Estimates and Margins-of-Error in your queries
 - Join ACS Summary File data to your own geo-coded data files within your personal data.world datasets by selecting ACS estimates and joining on standard geographical codes like ZIP or FIPS codes
 - Export query results for offline analysis or create automatic, lightweight visualizations of the data using data.world's Chart Builder

## 4.0 - Survey Content
All of the content areas covered in the ACS are available on data.world:

* Ability to speak English
* Age
* Ancestry
* Citizenship status
* Class of worker
* Commuting
* Disability status
* Educational attainment
* Employment status
* Fertility
* Field of degree
* Food
* Foreign born
* Grandparents as caregivers
* Group quarters
* Health insurance coverage
* Hispanic or Latino origin
* Household
* Household relationship
* Housing characteristics
* Income & Earnings
* Industry
* Journey to work
* Language spoken at home
* Marital status & Marital history
* Migration/Residence 1 year ago
* Occupation
* Place of birth/Nativity
* Poverty
* Race
* School enrollment
* Sex
* Subfamilies
* Veteran status
* Work status
* Year of entry

## 5.0 - Dataset Structure

### 5.1 - Naming Convention
The ACS dataset names used on data.world give the user information about each summary file in a standard format. The name of each dataset indicates the data product (or survey), the data product's release year, the period covered by the release, the measure contained in the dataset, and the dataset's topic area:

**Example:**
**ACS2016\_5\_E\_ForeignBirth**
| Example       | Name           | Range or Type                                                 |
|---------------|----------------|---------------------------------------------------------------|
| ACS           | Data Product   | American Community Survey                                     |
| 2016          | Reference Year | ACS data year (last year of the period for multiyear periods) |
| 5             | Period Covered | 1=1-year, 5=5-year                                            |
| E             | Measure        | E=Estimates, M=Margins-of-Error                               |
| ForeignBirth  | Topic          | Census topic area (See Section 5.2)           |

Users can query and join data across multiple ACS summary files using the data.world query tool by specifying the pertinent dataset names in a `FROM` clause (See **Section 6.0 - How-To Examples** and/or the [data.world SQL tutorial](https://docs.data.world/documentation/sql/concepts/basic/intro.html) for more detail).

### 5.2 - Topic Areas
The 2016 ACS topic areas currently stored on data.world span the following datasets:

[ACS2016\_5\_E\_AgeSex](https://data.world/uscensusbureau/acs-2016-5-e-agesex)  
[ACS2016\_5\_E\_Ancestry](https://data.world/uscensusbureau/acs-2016-5-e-ancestry)  
[ACS2016\_5\_E\_Children](https://data.world/uscensusbureau/acs-2016-5-e-children)  
[ACS2016\_5\_E\_Disability](https://data.world/uscensusbureau/acs-2016-5-e-disability)  
[ACS2016\_5\_E\_Earnings](https://data.world/uscensusbureau/acs-2016-5-e-earnings)  
[ACS2016\_5\_E\_Education](https://data.world/uscensusbureau/acs-2016-5-e-education)  
[ACS2016\_5\_E\_EmploymentStatus](https://data.world/uscensusbureau/acs-2016-5-e-employmentstatus)  
[ACS2016\_5\_E\_Fertility](https://data.world/uscensusbureau/acs-2016-5-e-fertility)  
[ACS2016\_5\_E\_ForeignBirth](https://data.world/uscensusbureau/acs-2016-5-e-foreignbirth)  
[ACS2016\_5\_E\_Grandparents](https://data.world/uscensusbureau/acs-2016-5-e-grandparents)  
[ACS2016\_5\_E\_GroupQuarters](https://data.world/uscensusbureau/acs-2016-5-e-groupquarters)  
[ACS2016\_5\_E\_HealthInsurance](https://data.world/uscensusbureau/acs-2016-5-e-healthinsurance)  
[ACS2016\_5\_E\_HispanicOrigin](https://data.world/uscensusbureau/acs-2016-5-e-hispanicorigin)  
[ACS2016\_5\_E\_HouseholdsFamilies](https://data.world/uscensusbureau/acs-2016-5-e-householdsfamilies)  
[ACS2016\_5\_E\_Housing](https://data.world/uscensusbureau/acs-2016-5-e-housing)  
[ACS2016\_5\_E\_Imputations](https://data.world/uscensusbureau/acs-2016-5-e-imputations)  
[ACS2016\_5\_E\_Income](https://data.world/uscensusbureau/acs-2016-5-e-income)  
[ACS2016\_5\_E\_Industry](https://data.world/uscensusbureau/acs-2016-5-e-industry)  
[ACS2016\_5\_E\_JourneyToWork](https://data.world/uscensusbureau/acs-2016-5-e-journeytowork)  
[ACS2016\_5\_E\_Language](https://data.world/uscensusbureau/acs-2016-5-e-language)  
[ACS2016\_5\_E\_MaritalStatus](https://data.world/uscensusbureau/acs-2016-5-e-maritalstatus)  
[ACS2016\_5\_E\_PlaceOfBirth](https://data.world/uscensusbureau/acs-2016-5-e-placeofbirth)  
[ACS2016\_5\_E\_Poverty](https://data.world/uscensusbureau/acs-2016-5-e-poverty)  
[ACS2016\_5\_E\_QualityMeasures](https://data.world/uscensusbureau/acs-2016-5-e-qualitymeasures)  
[ACS2016\_5\_E\_Race](https://data.world/uscensusbureau/acs-2016-5-e-race)  
[ACS2016\_5\_E\_ResidenceLastYear](https://data.world/uscensusbureau/acs-2016-5-e-residencelastyear)  
[ACS2016\_5\_E\_SchoolEnrollment](https://data.world/uscensusbureau/acs-2016-5-e-schoolenrollment)  
[ACS2016\_5\_E\_TransferPrograms](https://data.world/uscensusbureau/acs-2016-5-e-transferprograms)  
[ACS2016\_5\_E\_Veterans](https://data.world/uscensusbureau/acs-2016-5-e-veterans)  

### 5.3 - Data Files
The files contained in each `ACS2016_5_E` dataset follow the same naming and geography format. Only the Census tables and columns within each file (and by association their metadata records) will differ.

Within each dataset users will find 58 files:

 - one readme file (this file)
	 - 00_README.md
 - two metadata files (table descriptions and column descriptions)
	 - 01_TableKey.csv
	 - 02_ColumnKey.csv
 - fifty-two state files: one for each of the 50 US states + Puerto Rico & DC
	 - AK.csv
	 - ...
	 - WY.csv
 - three USA files (large geos, all states, and ZCTA/ZIP codes)
	 - USA.csv
	 - USA\_All\_States.csv
	 - USA\_ZCTA.csv


### 5.4 - Summary Levels
The ACS Summary Files cover geographic areas based on “summary levels.” A summary level specifies the content and the hierarchical relationships of the geographic elements that are required to tabulate and summarize data. For example, summary level code “40” represents the U.S. states, Washington D.C., and Puerto Rico; while summary level code “50” represents counties and county equivalents within states.

Summary levels currently contained in the ACS Summary Files stored on data.world:
| SummaryLevel | Description                                          |
|--------------|------------------------------------------------------|
| 10           | Country (USA)                                        |
| 20           | Region                                               |
| 30           | Division                                             |
| 40           | U.S. states, Washington D.C., and Puerto Rico        |
| 50           | Counties and county equivalents                      |
| 160          | Place/City                                           |
| 320          | Metropolitan and Micropolitan Statistical Area (MSA) |
| 500          | Congressional District                               |
| 860          | ZCTA (ZIP Code Tabulation Area - akin to ZIP Code)   |

The following table compares summary levels of state-level files with USA-level files hosted on data.world:
| Each State, DC, and Puerto Rico | States and USA | United States      |
|---------------------------------|----------------|--------------------|
| 50 - County                     | 40 - State     | 10 - United States |
| 160 - Place/City                |                | 20 - Region        |
| 320 - MSA                       |                | 30 - Division      |
| 500 - Congressional District    |                | 860 - ZCTA/ZIP     |

With the exception of the **USA\_All\_States** files, the United States level does not contain tables for geographies that are always entirely within a state, such as counties and places; for those tables, go to the file for that state. ZIP Code Tabulation Areas are in the United States level, because some ZIP codes span more than one state.

### 5.5 - Geography
When specifying specific states, counties, MSAs, and/or cities/places in an SQL query, the query tool will accept either SummaryLevel, FIPS or CBSA codes, the common postal abbreviations for the states + DC, as well as full Area Names; there is also limited support for regular expressions using the `LIKE` keyword in a `WHERE` clause to find geographies by name or portions of names or full regex support using the [REGEX function](https://docs.data.world/documentation/sql/reference/functions/regex.html) in dwSQL.

Many resources are available to help users understand the ACS geographic terms and concepts. For additional information, please visit the Geography Reference page at http://www.census.gov/geo/reference/index.html and the Geography & ACS page at http://www.census.gov/programs-surveys/acs/geography-acs.html.

### 5.6 - Tables and Columns
ACS data is quite robust and has to be divided into pieces for users to find what they need. The data is separated first by TopicAreas then by Geographies then by Tables and finally by Columns. The Topic Areas and Geographies are fairly straightforward to determine based on the dataset names (Topic Areas) and the filenames (Geographies) within those datasets, however the Tables and Columns are more difficult to ascertain.

Census Tables are purely collections of Columns, and each file in an ACS dataset stored on data.world is a collection of all the Tables within a given Topic Area (plus Geo Codes). The Geo Codes, Tables, and Columns break down structurally as follows, using the TX.csv file from the [ACS2016\_5\_E\_ForeignBirth](https://data.world/uscensusbureau/acs-2016-5-e-foreignbirth) dataset as an example:

    TX.csv
    |-- Geo Codes
    |   |-- summarylevel
    |   |-- state
    |   |-- statefips
    |   |-- countyfips
    |   |-- placefips
    |   |-- cbsacode
    |   |-- congressdistrict
    |   |-- geoid
    |   |-- areaname
    |-- Tables
        |-- b05001
        |   |-- Columns
        |   |-- b05001_001
        |   |-- b05001_002
        |   |-- b05001_003
        |   |-- b05001_004
        |   |-- b05001_005
        |   |-- b05001_006
        |-- b05001pr
        |   |-- Columns
        |   |-- b05001pr_001
        |   |-- b05001pr_002
        |   |-- b05001pr_003
        |   |-- b05001pr_004
        |   |-- b05001pr_005
        |   |-- b05001pr_006
        |-- b05002
        |   |-- Columns
        |   |-- b05002_001
        |   |-- b05002_002
        |   |-- ...

In practice, the header row of all ACS summary files stored on data.world are either Geo Code labels or ColumnIDs, and it is the user's job to use these to slice the data down to the pieces they are looking for. Metadata records `01_TableKey.csv` and `02_ColumnKey.csv` have been included in every ACS dataset to help users find the data they need. 

**01_TableKey.csv**
`TableIDs` are typically six-character strings, almost always starting with a “B” or “C”, followed by a five-digit number (e.g., “b01001” or “c02003”). For tables that include data from Puerto Rico, the table number may include the letters “pr” at the end (e.g., “b05001pr” for “Nativity and Citizenship Status in Puerto Rico”). The `TableDescription` tells you what sort of categories the table’s columns contain.

**02_ColumnKey.csv**
`ColumnIDs` are typically ten-character strings that follow the TableID of which they are a part (e.g. "b05001\_001" and "b05001\_002" are the first two columns contained in table "b05001"). The `ColumnDescription` states the precise description of the population the column measures.

ColumnIDs like b01003\_001 and b05001\_006 provide a great shorthand, and can be good for experienced users, but most users are unfamiliar with ACS variable nomenclature. Therefore, it is recommended that users spend a bit of time exploring the `01_TableKey.csv` and `02_ColumnKey.csv` metadata records. These metadata records are included as machine-readable CSVs so the user can query them; string matching with the `LIKE` keyword in a `WHERE` clause can help users find the columns they need.

### 5.7 - An Important Note About "Identical" Column Descriptions
Some datasets may include columns with identical column descriptions, but users should note that all columns refer to distinct populations, and identical column descriptions **do not** indicate identical data. For example, the following table shows the metadata for all columns in table `b05004 - MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX`.

| TableID | ColumnID   | ColumnDescription                                                                                   |
|---------|------------|-----------------------------------------------------------------------------------------------------|
| b05004  | b05004_001 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population                           |
| b05004  | b05004_002 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Male                      |
| b05004  | b05004_003 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Female                    |
| b05004  | b05004_004 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Native:                   |
| b05004  | b05004_005 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Male                      |
| b05004  | b05004_006 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Female                    |
| b05004  | b05004_007 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Foreign born:             |
| b05004  | b05004_008 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Male                      |
| b05004  | b05004_009 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Female                    |
| b05004  | b05004_010 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Naturalized U.S. citizen: |
| b05004  | b05004_011 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Male                      |
| b05004  | b05004_012 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Female                    |
| b05004  | b05004_013 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Not a U.S. citizen:       |
| b05004  | b05004_014 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Male                      |
| b05004  | b05004_015 | MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX for Total Population%Female                    |

Users may be tempted to assume columns b05004_002, b05004_005, b05004_008, b05004_011, and b05004_014 are the same, but they are not. In addition, columns b05004_003, b05004_006, b05004_009, b05004_012, and b05004_015 all refer to distinct populations as well. The following structural view of the table/column breakdown helps clear this up:

```
b05004 - MEDIAN AGE BY NATIVITY AND CITIZENSHIP STATUS BY SEX
|-- b05004_001 - Total Population
    |-- b05004_002 - Male
    |-- b05004_003 - Female
    |-- b05004_004 - Native:
    |   |-- b05004_005 - (Native) Male
    |   |-- b05004_006 - (Native) Female
    |-- b05004_007 - Foreign born:
    |   |-- b05004_008 - (Foreign born) Male
    |   |-- b05004_009 - (Foreign born) Female
    |-- b05004_010 - Naturalized U.S. citizen:
    |   |-- b05004_011 - (Naturalized) Male
    |   |-- b05004_012 - (Naturalized) Female
    |-- b05004_013 - Not a U.S. citizen:
        |-- b05004_014 - (Non citizen) Male
        |-- b05004_015 - (Non citizen) Female
```

**IMPORTANT:** In general, column descriptions ending in colons (:) are "parents," and the colon denotes that the following columns in the table ("children") are subsets of the parent, as shown in the structure above. Percent signs (%) are also used throughout column descriptions to denote heirarchy and do not refer to actual percentages.

This is an idiosyncrasy of Census metadata notation that comes from the ACS source data. Users must pay attention to the structure of the table from which they are pulling in order to get the correct population estimates. 

## 6.0 - How-To Examples

### 6.1 - Exploratory Workflow
**QUESTION:** Suppose we would like to determine the number of native US citizens, naturalized US citizens, and non citizens in a particular ZCTA/ZIP code. For this example we'll use data.world's ZIP code 78731.

1) Since this question pertains to nativity and US citizenship, we will query the [ACS2016\_5\_E\_ForeignBirth](https://data.world/uscensusbureau/acs-2016-5-e-foreignbirth) dataset.

2) In the file list of the main dataset view, click the `01_TableKey.csv` file to get a full screen view of this metadata record. Alternatively, one can run the following SQL query in the data.world query tool:

```
SELECT * FROM 01_TableKey ORDER BY TableID
```

This tells users which Census Tables make up the current dataset, the number of Columns that make up each Table, and the TopicArea (you may need to scroll to the right to see all columns).

3) Using the `TableDescription` column, we see the table of interest for this particular question is the first: `TableID`  = b05001. 

| TableID | TableDescription                                     | NumColumns | TopicArea     |
|---------|------------------------------------------------------|------------|---------------|
| b05001  | NATIVITY AND CITIZENSHIP STATUS IN THE UNITED STATES | 6          | Foreign Birth |


We also see that the b05001 table contains 6 columns. Next we'll investigate what these columns are.

4) Next open the `02_ColumnKey.csv`. Or, run the following SQL query in the data.world query tool:

```
SELECT * FROM 02_ColumnKey ORDER BY ColumnID
```

This metadata record goes one level deeper than `01_TableKey.csv` and outlines all the columns in the current dataset. The columns are related to the tables by the alphanumeric TableID preceding the underscore '`_`' in the `ColumnID`. For example, all columns in the b05001 table begin with `b05001_`. Since there are 6 columns in table b05001, the columns are `b05001_001`, `b05001_002`, `b05001_003`, `b05001_004`, `b05001_005`, and `b05001_006`.

Remember from our question we are looking for columns pertaining to:

 - Native US citizens
 - Naturalized US citizens
 - Non citizens

So these columns in the b05001 table ought to do the trick:

| ColumnID   | ColumnDescription                                                                                                                       |
|------------| ----------------------------------------------------------------------------------------------------------------------------------------|
| b05001_002 | NATIVITY AND CITIZENSHIP STATUS IN THE UNITED STATES for Total Population In The United States: U.S. citizen, born in the United States |
| b05001_005 | NATIVITY AND CITIZENSHIP STATUS IN THE UNITED STATES for Total Population In The United States: U.S. citizen by naturalization          |
| b05001_006 | NATIVITY AND CITIZENSHIP STATUS IN THE UNITED STATES for Total Population In The United States: Not a U.S. citizen                      |


5) Now that we have the columns we're looking for, we need to narrow the data down to the geography we're interested in: ZCTA/ZIP 78731.

If you are not in the query tool already, return to the main dataset view and click `Launch workspace` and then click `Write SQL queries`. Run the following query in the sql tool:

```
SELECT zcta, b05001_002, b05001_005, b05001_006
  FROM usa_zcta
 WHERE zcta = '78731'
```


The query returns the following table:
| zcta  | b05001\_002 | b05001\_005 | b05001\_006 |
|-------|-------------|-------------|-------------|
| 78731 | 23482       | 1329        | 2004        |

**ANSWER:**
There are an estimated 23,482 Native US citizens, 1,329 Naturalized US citizens, and 2,004 Non citizens residing in 78731.

### 6.2 - Sample Queries

1) All tables contained in a dataset:

```
SELECT * FROM 01_TableKey ORDER BY TableID
```

2) All columns contained in a dataset:

```
SELECT * FROM 02_ColumnKey ORDER BY ColumnID
```

3) Number of Native and Naturalized US citizens as well as Non citizens for data.world's ZCTA/ZIP code 78731.

```
SELECT zcta, b05001_002, b05001_005, b05001_006
  FROM usa_zcta
 WHERE zcta = '78731'
```
	
4) Number of Native and Naturalized US citizens as well as Non citizens for all states.

```
SELECT summarylevel, state, statefips, areaname, b05001_002, b05001_005, b05001_006
  FROM usa_all_states
 ORDER BY areaname
```

5) Number of Native and Naturalized US citizens as well as Non citizens for any geographic area in Missouri whose name includes "Springfield."

```
SELECT summaryLevel, state, statefips, placefips, cbsacode, areaname, b05001_002, b05001_005, b05001_006
  FROM mo
 WHERE areaname LIKE '%Springfield%'
```

6) Multi-table Select query returning number of Native and Naturalized US citizens as well as Non citizens for any geographic areas in Illinois, Massachusetts, or Missouri whose name includes "Springfield."

```	
SELECT summaryLevel, state, statefips, placefips, cbsacode, areaname, b05001_002, b05001_005, b05001_006
  FROM [il, ma, mo]
 WHERE areaname LIKE '%Springfield%'
```

## 7.0 - Contact
If you have general questions or comments about the American Community Survey, you can submit a question online at [ask.census.gov](http://ask.census.gov).

For technical questions or comments about the ACS Summary Files stored on data.world please email: [census@data.world](mailto:census@data.world).

For questions regarding survey methodology and accuracy of the ACS Summary Files contact: [acso.users.support@census.gov](mailto:acso.users.support@census.gov). 

## 8.0 - References
The following references were used in developing this documentation:

 - [ACS - 2015 Core Tech Doc](http://www2.census.gov/programs-surveys/acs/summary_file/2015/documentation/tech_docs/2015_SummaryFile_Tech_Doc.pdf)
 - [Working with acs.R](http://eglenn.scripts.mit.edu/citystate/wp-content/uploads/2013/06/wpid-working_with_acs_R3.pdf)