# BulkSendListItem

Bulk send summary in list responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**api_application_id** | **str** |  | [optional] 
**documents_count** | **int** |  | 
**documents_completed** | **int** |  | 
**documents_not_completed** | **int** |  | 
**created_at** | **datetime** |  | 
**user_id** | **str** |  | [optional] 
**status** | **str** |  | 
**template_ids** | **List[str]** |  | 

## Example

```python
from signwell_sdk.models.bulk_send_list_item import BulkSendListItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendListItem from a JSON string
bulk_send_list_item_instance = BulkSendListItem.from_json(json)
# print the JSON string representation of the object
print(BulkSendListItem.to_json())

# convert the object into a dict
bulk_send_list_item_dict = bulk_send_list_item_instance.to_dict()
# create an instance of BulkSendListItem from a dict
bulk_send_list_item_from_dict = BulkSendListItem.from_dict(bulk_send_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


