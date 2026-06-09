# signwell_sdk.DocumentApi

All URIs are relative to *https://www.signwell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentApi.md#create_document) | **POST** /api/v1/documents | Create Document
[**create_document_from_template**](DocumentApi.md#create_document_from_template) | **POST** /api/v1/document_templates/documents | Create Document from Template
[**delete_document**](DocumentApi.md#delete_document) | **DELETE** /api/v1/documents/{id} | Delete Document
[**get_completed_pdf**](DocumentApi.md#get_completed_pdf) | **GET** /api/v1/documents/{id}/completed_pdf | Completed PDF
[**get_document**](DocumentApi.md#get_document) | **GET** /api/v1/documents/{id} | Get Document
[**list_documents**](DocumentApi.md#list_documents) | **GET** /api/v1/documents | List Documents
[**send_document**](DocumentApi.md#send_document) | **POST** /api/v1/documents/{id}/send | Update and Send Document
[**send_reminder**](DocumentApi.md#send_reminder) | **POST** /api/v1/documents/{id}/remind | Send Reminder
[**update_recipients**](DocumentApi.md#update_recipients) | **PATCH** /api/v1/documents/{id}/recipients | Update Recipients


# **create_document**
> DocumentResponse create_document(document_request)

Create Document

Creates and optionally sends a new document for signing. If `draft` is set to true the document will not be sent.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_request import DocumentRequest
from signwell_sdk.models.document_response import DocumentResponse
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    document_request = signwell_sdk.DocumentRequest() # DocumentRequest | 

    try:
        # Create Document
        api_response = api_instance.create_document(document_request)
        print("The response of DocumentApi->create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_request** | [**DocumentRequest**](DocumentRequest.md)|  | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

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

# **create_document_from_template**
> DocumentFromTemplateResponse create_document_from_template(document_from_template_request)

Create Document from Template

Creates and optionally sends a new document for signing. If `draft` is set to true the document will not be sent.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_from_template_request import DocumentFromTemplateRequest
from signwell_sdk.models.document_from_template_response import DocumentFromTemplateResponse
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    document_from_template_request = signwell_sdk.DocumentFromTemplateRequest() # DocumentFromTemplateRequest | 

    try:
        # Create Document from Template
        api_response = api_instance.create_document_from_template(document_from_template_request)
        print("The response of DocumentApi->create_document_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->create_document_from_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_from_template_request** | [**DocumentFromTemplateRequest**](DocumentFromTemplateRequest.md)|  | 

### Return type

[**DocumentFromTemplateResponse**](DocumentFromTemplateResponse.md)

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

# **delete_document**
> delete_document(id)

Delete Document

Deletes a document. Deleting a document will also cancel document signing (if in progress).  Supply the unique document ID from either a Create Document request or document page URL.

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
    api_instance = signwell_sdk.DocumentApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Document
        api_instance.delete_document(id)
    except Exception as e:
        print("Exception when calling DocumentApi->delete_document: %s\n" % e)
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

# **get_completed_pdf**
> CompletedPdfResponse get_completed_pdf(id, url_only=url_only, audit_page=audit_page, file_format=file_format)

Completed PDF

Gets a completed document PDF or ZIP file. Supply the unique document ID from either a document creation request or document page URL.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.completed_pdf_response import CompletedPdfResponse
from signwell_sdk.models.file_format import FileFormat
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    id = 'id_example' # str | 
    url_only = False # bool |  (optional) (default to False)
    audit_page = True # bool |  (optional) (default to True)
    file_format = signwell_sdk.FileFormat() # FileFormat |  (optional)

    try:
        # Completed PDF
        api_response = api_instance.get_completed_pdf(id, url_only=url_only, audit_page=audit_page, file_format=file_format)
        print("The response of DocumentApi->get_completed_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->get_completed_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **url_only** | **bool**|  | [optional] [default to False]
 **audit_page** | **bool**|  | [optional] [default to True]
 **file_format** | [**FileFormat**](.md)|  | [optional] 

### Return type

[**CompletedPdfResponse**](CompletedPdfResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful, returns the final completed PDF, or if url_only is set to true, a JSON object is returned. When url_only&#x3D;false (default), the response is the raw PDF or ZIP binary data. |  -  |
**404** | not_found |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentResponse get_document(id)

Get Document

Returns a document and all associated document data. Supply the unique document ID from either a document creation request or Document page URL.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_response import DocumentResponse
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Document
        api_response = api_instance.get_document(id)
        print("The response of DocumentApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

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

# **list_documents**
> DocumentListResponse list_documents(page=page, limit=limit)

List Documents

Returns a paginated list of documents for the authenticated account.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_list_response import DocumentListResponse
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Documents
        api_response = api_instance.list_documents(page=page, limit=limit)
        print("The response of DocumentApi->list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->list_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

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

# **send_document**
> DocumentResponse send_document(id, update_document_and_send_request)

Update and Send Document

Updates a draft document and sends it to be signed by recipients.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_response import DocumentResponse
from signwell_sdk.models.update_document_and_send_request import UpdateDocumentAndSendRequest
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    id = 'id_example' # str | 
    update_document_and_send_request = signwell_sdk.UpdateDocumentAndSendRequest() # UpdateDocumentAndSendRequest | 

    try:
        # Update and Send Document
        api_response = api_instance.send_document(id, update_document_and_send_request)
        print("The response of DocumentApi->send_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->send_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_document_and_send_request** | [**UpdateDocumentAndSendRequest**](UpdateDocumentAndSendRequest.md)|  | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**422** | unprocessable entity |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_reminder**
> send_reminder(id, send_reminder_request)

Send Reminder

Sends a reminder email to recipients that have not signed yet.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.send_reminder_request import SendReminderRequest
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    id = 'id_example' # str | 
    send_reminder_request = signwell_sdk.SendReminderRequest() # SendReminderRequest | 

    try:
        # Send Reminder
        api_instance.send_reminder(id, send_reminder_request)
    except Exception as e:
        print("Exception when calling DocumentApi->send_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **send_reminder_request** | [**SendReminderRequest**](SendReminderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**422** | unprocessable entity |  -  |
**404** | not found |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipients**
> DocumentResponse update_recipients(id, update_recipients_request)

Update Recipients

Updates one or more recipients on a document that has already been sent. Only recipients who have not started signing may be updated. Recipient IDs must be retrieved from the Get Document response. Allowed document statuses: sent, viewed, pending, bounced. For non-embedded documents, updated recipients will receive a new notification email. For embedded signing documents, email behavior follows each recipient's send_email setting.

### Example

* Api Key Authentication (api_key):

```python
import os
from pprint import pprint

import signwell_sdk
from signwell_sdk.models.document_response import DocumentResponse
from signwell_sdk.models.update_recipients_request import UpdateRecipientsRequest
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
    api_instance = signwell_sdk.DocumentApi(api_client)
    id = 'id_example' # str | 
    update_recipients_request = signwell_sdk.UpdateRecipientsRequest() # UpdateRecipientsRequest | 

    try:
        # Update Recipients
        api_response = api_instance.update_recipients(id, update_recipients_request)
        print("The response of DocumentApi->update_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->update_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_recipients_request** | [**UpdateRecipientsRequest**](UpdateRecipientsRequest.md)|  | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**409** | conflict - document not in eligible state |  -  |
**400** | bad request - invalid structure |  -  |
**422** | unprocessable entity - business rule violation |  -  |
**404** | not found |  -  |
**429** | rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

