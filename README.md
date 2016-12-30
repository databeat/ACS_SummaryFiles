# ACS_SummaryFiles

## Summary
A project to develop a Python script for easily assembling large batches of American Community Survey (ACS) Summary Files.

## Get Started
1. Clone this repository to your local machine
1. Using the repository's existing file structure, download and store the required ACS input data [summary files](https://github.com/databeat/ACS_SummaryFiles/tree/master/2014/1-year/data/1_year_entire_sf) and [templates](https://github.com/databeat/ACS_SummaryFiles/tree/master/2014/1-year/data/1_year_Summary_FileTemplates) for guidance
1. Once all inputs are downloaded and extracted, open the 1yrSummaryFileAssembler.py file in a text editor
1. Provide lists of Sequences, Geographies, and Measures (Estimates, Margins-of-error, or both) in the Python script, or simply use those already provided
1. Run the script
1. Summary files are written to Output folder

## Notes
* This script is currently configured to run only on 2014 1-year ACS Summary File input data.
* This script imports the following Python modules: `os`, `csv`, `xlrd`, and `openpyxl`
