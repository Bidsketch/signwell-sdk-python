# BulkSendDocumentsResponse

Paginated list of documents in a bulk send

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**api_application_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**user_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**documents** | [**List[DocumentResponse]**](DocumentResponse.md) |  | 
**current_page** | **int** |  | 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**total_count** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from signwell_sdk.models.bulk_send_documents_response import BulkSendDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendDocumentsResponse from a JSON string
bulk_send_documents_response_instance = BulkSendDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkSendDocumentsResponse.to_json())

# convert the object into a dict
bulk_send_documents_response_dict = bulk_send_documents_response_instance.to_dict()
# create an instance of BulkSendDocumentsResponse from a dict
bulk_send_documents_response_from_dict = BulkSendDocumentsResponse.from_dict(bulk_send_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


