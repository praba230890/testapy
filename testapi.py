import requests
import json

def test_api(test_data):
    api = get_api(test_data)
    method = test_data["method"]
#    cases = test_data["data_set_count"]
    auth_details = get_auth_details(test_data)
#    data_set_count = get_data_set_count(test_data)
#    parameters = [get_parameters(data_set_count, test_data)]
    parameters_per_url = get_parameters_per_url(test_data)
    url_parameters = get_url_parameters(parameters_per_url, test_data)
    results = get_results(url_parameters, test_data)
    
    for i in range(len(url_parameters)):
        request_api = api
        for parameter in url_parameters[i]:
            request_api += str(parameter)
        response = requests.get(request_api, auth=auth_details)
        if dict(response.json()) == results[i]:
            print "Success: For "+request_api+" : with parameter ["+str(url_parameters)+"] the expected result ["+str(results[i])+"] is achieved"
        else:
            print "Failed: For "+request_api+" : with parameter ["+str(url_parameters)+"] the expected result ["+str(results[i])+"] not achieved"

def get_parameters_per_url(test_data):
    if "params_per_url" in test_data:
        return test_data["params_per_url"]
    else:
        raise ValueError("ParamsPerUrlNotDefined")

def get_url_parameters(parameters_per_url, test_data):
    if "url_params" in test_data:
        for i in test_data["url_params"]:
            if len(i) == parameters_per_url:
                pass
            else:
                raise ValueError("UrlParamsDoesNotMatchNoOfUrlParams")
        return test_data["url_params"]
    else:
        raise ValueError("UrlParamsNotDefined")

def get_api(test_data):
    if "api" in test_data:
        return test_data["api"]
    else:
        raise ValueError("APINotDefined")

def get_parameters(data_set_count, test_data):
    if data_set_count > 1 and "parameters" in test_data:
        return test_data["parameters"]
    else:
        return None

def get_results(parameters, test_data):
    if "results" in test_data:
        if len(parameters) == len(test_data["results"]):
            return test_data["results"]
        else:
            raise ValueError("ResultsCountMismatchParametersCount")
    else:
        raise ValueError("ResultsNotDefined")

def get_data_set_count(test_data):
    if "data_set_count" in test_data:
        return test_data["data_set_count"]
    else:
        raise ValueError("DataSetCountNotDefined")

def get_auth_details(test_data):
    if "auth" in test_data:
        if test_data["auth"] == 0:
            return None
        if test_data["auth"] == 1 and "auth_details" in test_data:
            return test_data["auth_details"]
        elif test_data["auth"] == 1:
            raise ValueError("NoAuthDetails: given '1' for auth parameter but no auth_details found")
        else:
            raise ValueError("InvalidAuthParameter: give 0 for no authentication or 1 for authentication")
    else:
        return None      # if no "auth" parameter is set, we take it as "auth": 0
