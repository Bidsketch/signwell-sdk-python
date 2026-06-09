# signwell_sdk.RegionalApi

All URIs are relative to *https://www.signwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nom151_certificate**](RegionalApi.md#get_nom151_certificate) | **GET** /api/v1/documents/{id}/nom151_certificate | MX – NOM-151 Certificate


# **get_nom151_certificate**
> Nom151UrlResponse get_nom151_certificate(id, url_only=url_only, object_only=object_only)

MX – NOM-151 Certificate

Download NOM-151 certificate for a completed document. Returns a ZIP file, download URL, or raw certificate data based on query parameters.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.nom151_url_response import Nom151UrlResponse
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
    api_instance = signwell_sdk.RegionalApi(api_client)
    id = 'id_example' # str | 
    url_only = False # bool | If true, returns JSON with download URL instead of downloading the file (optional) (default to False)
    object_only = False # bool |  (optional) (default to False)

    try:
        # MX – NOM-151 Certificate
        api_response = api_instance.get_nom151_certificate(id, url_only=url_only, object_only=object_only)
        print("The response of RegionalApi->get_nom151_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalApi->get_nom151_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **url_only** | **bool**| If true, returns JSON with download URL instead of downloading the file | [optional] [default to False]
 **object_only** | **bool**|  | [optional] [default to False]

### Return type

[**Nom151UrlResponse**](Nom151UrlResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**404** | not_found |  -  |
**422** | unprocessable_entity |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

