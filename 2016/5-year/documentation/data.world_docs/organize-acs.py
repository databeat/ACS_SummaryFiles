## Untested

import http.client
import time

conn = http.client.HTTPSConnection("api.data.world")

headers = {
    'authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJwcm9kLXVzZXItY2xpZW50OnVzY2Vuc3VzYnVyZWF1IiwiaXNzIjoiYWdlbnQ6dXNjZW5zdXNidXJlYXU6OmUyNjJjMWI3LTljYWEtNDdiOC1iNWRlLWFhYjRhNmY3OWM3MSIsImlhdCI6MTQ4NDA4MzI2Miwicm9sZSI6WyJ1c2VyX2FwaV93cml0ZSIsInVzZXJfYXBpX3JlYWQiLCJ1c2VyX2FwaV9hZG1pbiJdLCJnZW5lcmFsLXB1cnBvc2UiOnRydWV9.YZy5DaGjzlwYAWP8eZtg9HKhGJEwZ2EQIHrllLcPEN1DgFhtMcqhJjwx9FjVMxEfrWYC88WqWOHf_JGpzBIfJw",
    'content-type': "application/json"
    }

datasets = ['acs-2016-5-m-imputations',
			'acs-2016-5-e-imputations',
			'acs-2016-5-m-qualitymeasures',
			'acs-2016-5-e-qualitymeasures',
			'acs-2016-5-m-healthinsurance',
			'acs-2016-5-e-healthinsurance',
			'acs-2016-5-m-groupquarters',
			'acs-2016-5-e-groupquarters',
			'acs-2016-5-m-housing',
			'acs-2016-5-e-housing',
			'acs-2016-5-m-industry',
			'acs-2016-5-e-industry',
			'acs-2016-5-m-employmentstatus',
			'acs-2016-5-e-employmentstatus',
			'acs-2016-5-m-transferprograms',
			'acs-2016-5-e-transferprograms',
			'acs-2016-5-m-veterans',
			'acs-2016-5-e-veterans',
			'acs-2016-5-m-earnings',
			'acs-2016-5-e-earnings',
			'acs-2016-5-m-income',
			'acs-2016-5-e-income',
			'acs-2016-5-m-disability',
			'acs-2016-5-e-disability',
			'acs-2016-5-m-poverty',
			'acs-2016-5-e-poverty',
			'acs-2016-5-m-language',
			'acs-2016-5-e-language',
			'acs-2016-5-m-education',
			'acs-2016-5-e-education',
			'acs-2016-5-m-schoolenrollment',
			'acs-2016-5-e-schoolenrollment',
			'acs-2016-5-m-fertility',
			'acs-2016-5-e-fertility',
			'acs-2016-5-m-maritalstatus',
			'acs-2016-5-e-maritalstatus',
			'acs-2016-5-m-householdsfamilies',
			'acs-2016-5-e-householdsfamilies',
			'acs-2016-5-m-grandparents',
			'acs-2016-5-e-grandparents',
			'acs-2016-5-m-children',
			'acs-2016-5-e-children',
			'acs-2016-5-m-journeytowork',
			'acs-2016-5-e-journeytowork',
			'acs-2016-5-m-residencelastyear',
			'acs-2016-5-e-residencelastyear',
			'acs-2016-5-m-placeofbirth',
			'acs-2016-5-e-placeofbirth',
			'acs-2016-5-m-foreignbirth',
			'acs-2016-5-e-foreignbirth',
			'acs-2016-5-m-ancestry',
			'acs-2016-5-e-ancestry',
			'acs-2016-5-m-hispanicorigin',
			'acs-2016-5-e-hispanicorigin',
			'acs-2016-5-m-race',
			'acs-2016-5-e-race',
			'acs-2016-5-m-agesex',
			'acs-2016-5-e-agesex' ]

payload = "{\"visibility\":\"Private\"}"

for ds in datasets:
	conn.request("PATCH", "/v0/datasets/uscensusbureau/{0}".format(ds), payload, headers)
	res = conn.getresponse()
	data = res.read()
	print(data.decode("utf-8"))
	time.sleep(1)

del payload

payload = "{\"visibility\":\"Open\"}"

for ds in datasets:
	conn.request("PATCH", "/v0/datasets/uscensusbureau/{0}".format(ds), payload, headers)
	res = conn.getresponse()
	data = res.read()
	print(data.decode("utf-8"))
	time.sleep(1)
