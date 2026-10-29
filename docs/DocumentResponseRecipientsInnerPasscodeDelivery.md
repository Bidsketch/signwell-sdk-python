# DocumentResponseRecipientsInnerPasscodeDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**methods** | **List[str]** |  | [optional] 
**expire_after_access** | **bool** |  | [optional] 

## Example

```python
from signwell_sdk.models.document_response_recipients_inner_passcode_delivery import DocumentResponseRecipientsInnerPasscodeDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResponseRecipientsInnerPasscodeDelivery from a JSON string
document_response_recipients_inner_passcode_delivery_instance = DocumentResponseRecipientsInnerPasscodeDelivery.from_json(json)
# print the JSON string representation of the object
print(DocumentResponseRecipientsInnerPasscodeDelivery.to_json())

# convert the object into a dict
document_response_recipients_inner_passcode_delivery_dict = document_response_recipients_inner_passcode_delivery_instance.to_dict()
# create an instance of DocumentResponseRecipientsInnerPasscodeDelivery from a dict
document_response_recipients_inner_passcode_delivery_from_dict = DocumentResponseRecipientsInnerPasscodeDelivery.from_dict(document_response_recipients_inner_passcode_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


