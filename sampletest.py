from testapi import test_api

test_data = {"api":"http://api/to/be/tested",
            "method": "get",
            "auth": 0,  # 1 if auth is required, 0 for no authentication. Also, if no "auth" parameter is set, we take it as "auth": 0
#           "auth_details": ("user": "pass")   # if "auth": 1 
            "transaction": "s",        # s for single & m for many
            "data_set_count": 1,
            "params_per_url": 1,
            "url_params_count": 3,
            "url_params": [["1234567"], ["DD3464750"], ["3232323"]],
#            "parameters": [{},{}],    if parameters exists
            "results": [{u"status": u"Used"}, {u'Price': 1200, u'status': u'UnUsed'}, {u"status": u"Used"}]   # [{},{}], for more cases
            }

test_data1 = {"api":"http://api/to/be/tested/",
            "method": "get",
            "auth": 0,  
            "transaction": "s",     
#            "parameters": [{},{}],    if parameters exists            
            "params_per_url": 1,
            "url_params_count": 3,
            "url_params": [["1234567"], ["DD3464750"], ["3232323"]],
            "results": [{u"status": u"Used"}, {u'Price': 1200, u'status': u'UnUsed'}, {u"status": u"Used"}]   # [{},{}], for more cases
            }

test_api(test_data)
test_api(test_data2)
