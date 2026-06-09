# signwell_sdk.BulkSendApi

All URIs are relative to *https://www.signwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_send**](BulkSendApi.md#create_bulk_send) | **POST** /api/v1/bulk_sends | Create Bulk Send
[**get_bulk_send**](BulkSendApi.md#get_bulk_send) | **GET** /api/v1/bulk_sends/{id} | Get Bulk Send
[**get_bulk_send_csv_template**](BulkSendApi.md#get_bulk_send_csv_template) | **GET** /api/v1/bulk_sends/csv_template | Get Bulk Send CSV Template
[**get_bulk_send_documents**](BulkSendApi.md#get_bulk_send_documents) | **GET** /api/v1/bulk_sends/{id}/documents | Get Bulk Send Documents
[**list_bulk_sends**](BulkSendApi.md#list_bulk_sends) | **GET** /api/v1/bulk_sends | List Bulk Sendings
[**validate_bulk_send_csv**](BulkSendApi.md#validate_bulk_send_csv) | **POST** /api/v1/bulk_sends/validate_csv | Validate Bulk Send CSV


# **create_bulk_send**
> BulkSendCreateResponse create_bulk_send(create_bulk_send_request)

Create Bulk Send

Creates a bulk send, and it validates the CSV file before creating the bulk send.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.bulk_send_create_response import BulkSendCreateResponse
from signwell_sdk.models.create_bulk_send_request import CreateBulkSendRequest
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
    api_instance = signwell_sdk.BulkSendApi(api_client)
    create_bulk_send_request = signwell_sdk.CreateBulkSendRequest() # CreateBulkSendRequest | 

    try:
        # Create Bulk Send
        api_response = api_instance.create_bulk_send(create_bulk_send_request)
        print("The response of BulkSendApi->create_bulk_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkSendApi->create_bulk_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bulk_send_request** | [**CreateBulkSendRequest**](CreateBulkSendRequest.md)|  | 

### Return type

[**BulkSendCreateResponse**](BulkSendCreateResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful |  -  |
**422** | unprocessable entity |  -  |
**401** | unauthorized |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_send**
> BulkSendResponse get_bulk_send(id)

Get Bulk Send

Returns information about the Bulk Send.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.bulk_send_response import BulkSendResponse
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
    api_instance = signwell_sdk.BulkSendApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Bulk Send
        api_response = api_instance.get_bulk_send(id)
        print("The response of BulkSendApi->get_bulk_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkSendApi->get_bulk_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BulkSendResponse**](BulkSendResponse.md)

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
**404** | not found |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_send_csv_template**
> bytearray get_bulk_send_csv_template(template_ids, var_base64=var_base64)

Get Bulk Send CSV Template

Fetches a CSV template that corresponds to the provided document template IDs. CSV templates are blank CSV files that have columns containing required and optional data that can be sent when creating a bulk send. Fields can be referenced by the field label. Example: [placeholder name]_[field label] could be something like customer_address or signer_company_name (if 'Customer' and 'Signer' were placeholder names for templates set up in SignWell).

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
    api_instance = signwell_sdk.BulkSendApi(api_client)
    template_ids = ['template_ids_example'] # List[str] | 
    var_base64 = True # bool |  (optional)

    try:
        # Get Bulk Send CSV Template
        api_response = api_instance.get_bulk_send_csv_template(template_ids, var_base64=var_base64)
        print("The response of BulkSendApi->get_bulk_send_csv_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkSendApi->get_bulk_send_csv_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_ids** | [**List[str]**](str.md)|  | 
 **var_base64** | **bool**|  | [optional] 

### Return type

**bytearray**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_send_documents**
> BulkSendDocumentsResponse get_bulk_send_documents(id, limit=limit, page=page)

Get Bulk Send Documents

Returns information about the Bulk Send.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.bulk_send_documents_response import BulkSendDocumentsResponse
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
    api_instance = signwell_sdk.BulkSendApi(api_client)
    id = 'id_example' # str | 
    limit = 10 # int |  (optional) (default to 10)
    page = 1 # int |  (optional) (default to 1)

    try:
        # Get Bulk Send Documents
        api_response = api_instance.get_bulk_send_documents(id, limit=limit, page=page)
        print("The response of BulkSendApi->get_bulk_send_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkSendApi->get_bulk_send_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**BulkSendDocumentsResponse**](BulkSendDocumentsResponse.md)

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
**404** | not found |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bulk_sends**
> BulkSendListResponse list_bulk_sends(user_email=user_email, limit=limit, page=page, api_application_id=api_application_id)

List Bulk Sendings

Returns information about the Bulk Send.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.bulk_send_list_response import BulkSendListResponse
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
    api_instance = signwell_sdk.BulkSendApi(api_client)
    user_email = 'user_email_example' # str |  (optional)
    limit = 10 # int |  (optional) (default to 10)
    page = 1 # int |  (optional) (default to 1)
    api_application_id = 'api_application_id_example' # str |  (optional)

    try:
        # List Bulk Sendings
        api_response = api_instance.list_bulk_sends(user_email=user_email, limit=limit, page=page, api_application_id=api_application_id)
        print("The response of BulkSendApi->list_bulk_sends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkSendApi->list_bulk_sends: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **page** | **int**|  | [optional] [default to 1]
 **api_application_id** | **str**|  | [optional] 

### Return type

[**BulkSendListResponse**](BulkSendListResponse.md)

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

# **validate_bulk_send_csv**
> BulkSendValidateCsvResponse validate_bulk_send_csv(bulk_send_csv_request)

Validate Bulk Send CSV

Validates a Bulk Send CSV file before creating the Bulk Send. It will check the structure of the CSV and the data it contains, and return any errors found.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.bulk_send_csv_request import BulkSendCsvRequest
from signwell_sdk.models.bulk_send_validate_csv_response import BulkSendValidateCsvResponse
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
    api_instance = signwell_sdk.BulkSendApi(api_client)
    bulk_send_csv_request = signwell_sdk.BulkSendCsvRequest() # BulkSendCsvRequest | 

    try:
        # Validate Bulk Send CSV
        api_response = api_instance.validate_bulk_send_csv(bulk_send_csv_request)
        print("The response of BulkSendApi->validate_bulk_send_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkSendApi->validate_bulk_send_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_send_csv_request** | [**BulkSendCsvRequest**](BulkSendCsvRequest.md)|  | 

### Return type

[**BulkSendValidateCsvResponse**](BulkSendValidateCsvResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**422** | unprocessable entity |  -  |
**401** | unauthorized |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

