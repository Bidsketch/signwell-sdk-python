# BulkSendResponseTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from signwell_sdk.models.bulk_send_response_templates_inner import BulkSendResponseTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendResponseTemplatesInner from a JSON string
bulk_send_response_templates_inner_instance = BulkSendResponseTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(BulkSendResponseTemplatesInner.to_json())

# convert the object into a dict
bulk_send_response_templates_inner_dict = bulk_send_response_templates_inner_instance.to_dict()
# create an instance of BulkSendResponseTemplatesInner from a dict
bulk_send_response_templates_inner_from_dict = BulkSendResponseTemplatesInner.from_dict(bulk_send_response_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


