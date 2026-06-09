# BulkSendCreateResponse

Bulk send creation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**template_ids** | **List[str]** |  | 
**api_application_id** | **str** |  | [optional] 
**documents_count** | **int** |  | 
**created_at** | **datetime** |  | 
**user_id** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from signwell_sdk.models.bulk_send_create_response import BulkSendCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendCreateResponse from a JSON string
bulk_send_create_response_instance = BulkSendCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BulkSendCreateResponse.to_json())

# convert the object into a dict
bulk_send_create_response_dict = bulk_send_create_response_instance.to_dict()
# create an instance of BulkSendCreateResponse from a dict
bulk_send_create_response_from_dict = BulkSendCreateResponse.from_dict(bulk_send_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


