# BulkSendListResponse

List of bulk sends with pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_sends** | [**List[BulkSendListItem]**](BulkSendListItem.md) |  | 
**current_page** | **int** |  | 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**total_count** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from signwell_sdk.models.bulk_send_list_response import BulkSendListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendListResponse from a JSON string
bulk_send_list_response_instance = BulkSendListResponse.from_json(json)
# print the JSON string representation of the object
print(BulkSendListResponse.to_json())

# convert the object into a dict
bulk_send_list_response_dict = bulk_send_list_response_instance.to_dict()
# create an instance of BulkSendListResponse from a dict
bulk_send_list_response_from_dict = BulkSendListResponse.from_dict(bulk_send_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


