# UpdateRecipientsMapInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The recipient&#39;s unique identifier from the Get Document response. | 
**name** | **str** | Updated name for the recipient. | 
**email** | **str** | Updated email address for the recipient. | 
**subject** | **str** | Updated email subject for the signature request that this recipient will see. | [optional] 
**message** | **str** | Updated email message for the signature request that this recipient will see. | [optional] 
**passcode** | **str** | Updated passcode for the recipient. If set, the signer will be required to enter the passcode before viewing and completing the document. | [optional] 

## Example

```python
from signwell_sdk.models.update_recipients_map_inner import UpdateRecipientsMapInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecipientsMapInner from a JSON string
update_recipients_map_inner_instance = UpdateRecipientsMapInner.from_json(json)
# print the JSON string representation of the object
print(UpdateRecipientsMapInner.to_json())

# convert the object into a dict
update_recipients_map_inner_dict = update_recipients_map_inner_instance.to_dict()
# create an instance of UpdateRecipientsMapInner from a dict
update_recipients_map_inner_from_dict = UpdateRecipientsMapInner.from_dict(update_recipients_map_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


