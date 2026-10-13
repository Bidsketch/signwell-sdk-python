# UpdateAuthenticationRequestRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier that you will give to each recipient. We recommend numbering sequentially from 1 to X. IDs are required for associating recipients to fields and more. | 
**passcode** | **str** | Updated passcode for the recipient. If set, the signer will be required to enter the passcode before viewing and completing the document. On a 21 CFR Part 11 document SignWell generates the passcode, so a sender-defined passcode returns a 422. | [optional] 
**passcode_delivery** | [**UpdateRecipientsMapInnerPasscodeDelivery**](UpdateRecipientsMapInnerPasscodeDelivery.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.update_authentication_request_recipients_inner import UpdateAuthenticationRequestRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthenticationRequestRecipientsInner from a JSON string
update_authentication_request_recipients_inner_instance = UpdateAuthenticationRequestRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAuthenticationRequestRecipientsInner.to_json())

# convert the object into a dict
update_authentication_request_recipients_inner_dict = update_authentication_request_recipients_inner_instance.to_dict()
# create an instance of UpdateAuthenticationRequestRecipientsInner from a dict
update_authentication_request_recipients_inner_from_dict = UpdateAuthenticationRequestRecipientsInner.from_dict(update_authentication_request_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


