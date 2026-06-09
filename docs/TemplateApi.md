# signwell_sdk.TemplateApi

All URIs are relative to *https://www.signwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplateApi.md#create_template) | **POST** /api/v1/document_templates | Create Template
[**delete_template**](TemplateApi.md#delete_template) | **DELETE** /api/v1/document_templates/{id} | Delete Template
[**get_template**](TemplateApi.md#get_template) | **GET** /api/v1/document_templates/{id} | Get Template
[**list_templates**](TemplateApi.md#list_templates) | **GET** /api/v1/document_templates | List Templates
[**update_template**](TemplateApi.md#update_template) | **PUT** /api/v1/document_templates/{id} | Update Template


# **create_template**
> DocumentTemplateResponse create_template(document_template_request)

Create Template

Creates a new template.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_template_request import DocumentTemplateRequest
from signwell_sdk.models.document_template_response import DocumentTemplateResponse
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
    api_instance = signwell_sdk.TemplateApi(api_client)
    document_template_request = signwell_sdk.DocumentTemplateRequest() # DocumentTemplateRequest | 

    try:
        # Create Template
        api_response = api_instance.create_template(document_template_request)
        print("The response of TemplateApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_template_request** | [**DocumentTemplateRequest**](DocumentTemplateRequest.md)|  | 

### Return type

[**DocumentTemplateResponse**](DocumentTemplateResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**400** | bad request |  -  |
**422** | unprocessable entity |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(id)

Delete Template

Deletes a template. Supply the unique template ID from either a Create Template request or template page URL.

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
    api_instance = signwell_sdk.TemplateApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Template
        api_instance.delete_template(id)
    except Exception as e:
        print("Exception when calling TemplateApi->delete_template: %s\n" % e)
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

# **get_template**
> DocumentTemplateResponse get_template(id)

Get Template

Returns a template and all associated template data. Supply the unique template ID from either a Create Template request or template page URL.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_template_response import DocumentTemplateResponse
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
    api_instance = signwell_sdk.TemplateApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Template
        api_response = api_instance.get_template(id)
        print("The response of TemplateApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DocumentTemplateResponse**](DocumentTemplateResponse.md)

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

# **list_templates**
> DocumentTemplateListResponse list_templates(page=page, limit=limit)

List Templates

Returns a paginated list of templates for the authenticated account.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_template_list_response import DocumentTemplateListResponse
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
    api_instance = signwell_sdk.TemplateApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Templates
        api_response = api_instance.list_templates(page=page, limit=limit)
        print("The response of TemplateApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**DocumentTemplateListResponse**](DocumentTemplateListResponse.md)

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

# **update_template**
> DocumentTemplateResponse update_template(id, document_template_update_request)

Update Template

Updates an existing template.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_template_response import DocumentTemplateResponse
from signwell_sdk.models.document_template_update_request import DocumentTemplateUpdateRequest
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
    api_instance = signwell_sdk.TemplateApi(api_client)
    id = 'id_example' # str | 
    document_template_update_request = signwell_sdk.DocumentTemplateUpdateRequest() # DocumentTemplateUpdateRequest | 

    try:
        # Update Template
        api_response = api_instance.update_template(id, document_template_update_request)
        print("The response of TemplateApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **document_template_update_request** | [**DocumentTemplateUpdateRequest**](DocumentTemplateUpdateRequest.md)|  | 

### Return type

[**DocumentTemplateResponse**](DocumentTemplateResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | bad request |  -  |
**422** | unprocessable entity |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

