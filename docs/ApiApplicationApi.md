# signwell_sdk.ApiApplicationApi

All URIs are relative to *https://www.signwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_application**](ApiApplicationApi.md#delete_api_application) | **DELETE** /api/v1/api_applications/{id} | Delete API Application
[**get_api_application**](ApiApplicationApi.md#get_api_application) | **GET** /api/v1/api_applications/{id} | Get API Application


# **delete_api_application**
> delete_api_application(id)

Delete API Application

Deletes an API Application from an account. Supply the unique Application ID from either the Create API Application response or the API Application edit page

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
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
    api_instance = signwell_sdk.ApiApplicationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete API Application
        api_instance.delete_api_application(id)
    except Exception as e:
        print("Exception when calling ApiApplicationApi->delete_api_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | no content |  -  |
**404** | not found |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_application**
> ApiApplicationResponse get_api_application(id)

Get API Application

Gets the details of a specific API Application within an account. Supply the unique Application ID from either the Create API Application response or the API Application edit page.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.api_application_response import ApiApplicationResponse
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
    api_instance = signwell_sdk.ApiApplicationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get API Application
        api_response = api_instance.get_api_application(id)
        print("The response of ApiApplicationApi->get_api_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApplicationApi->get_api_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiApplicationResponse**](ApiApplicationResponse.md)

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
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

