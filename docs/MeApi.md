# signwell_sdk.MeApi

All URIs are relative to *https://www.signwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](MeApi.md#get_me) | **GET** /api/v1/me | Get credentials


# **get_me**
> MeResponse get_me()

Get credentials

Retrieves the account information associated with the API key being used.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.me_response import MeResponse
from signwell_sdk.rest import ApiException

# Defining the host is optional and defaults to https://www.signwell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = signwell_sdk.Configuration(
    host = "https://www.signwell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["SIGNWELL_API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with signwell_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signwell_sdk.MeApi(api_client)

    try:
        # Get credentials
        api_response = api_instance.get_me()
        print("The response of MeApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MeResponse**](MeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | unauthorized |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

