1) use a list com[rehension in your code (see sandbox); see line 33 in external access service

2) Make a safe browing response, using the response you got from the requests package.
    * The payload will require two lists of url strings, one list for good, one list for bad.
    * safe_browsing_response = dacite.from_dict(contracts.SafeBrosingResponse, payload)