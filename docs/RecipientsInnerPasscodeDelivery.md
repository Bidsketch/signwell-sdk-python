# RecipientsInnerPasscodeDelivery

Passcode delivery settings. When enabled, the system delivers the passcode to the signer via email. Always on for 21 CFR Part 11 documents and cannot be disabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable passcode delivery for this recipient. Cannot be set to &#x60;false&#x60; on a 21 CFR Part 11 document: it returns a 422. | [optional] 
**methods** | **List[str]** | Delivery methods for the passcode. Currently supports: email. Defaults to [\&quot;email\&quot;] when omitted. | [optional] 
**expire_after_access** | **bool** | When enabled, the passcode is cleared after successful authentication. If passcode_delivery is also enabled, a new passcode is auto-generated on the next send request. Otherwise the recipient will no longer need a passcode. | [optional] 

## Example

```python
from signwell_sdk.models.recipients_inner_passcode_delivery import RecipientsInnerPasscodeDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientsInnerPasscodeDelivery from a JSON string
recipients_inner_passcode_delivery_instance = RecipientsInnerPasscodeDelivery.from_json(json)
# print the JSON string representation of the object
print(RecipientsInnerPasscodeDelivery.to_json())

# convert the object into a dict
recipients_inner_passcode_delivery_dict = recipients_inner_passcode_delivery_instance.to_dict()
# create an instance of RecipientsInnerPasscodeDelivery from a dict
recipients_inner_passcode_delivery_from_dict = RecipientsInnerPasscodeDelivery.from_dict(recipients_inner_passcode_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


