# UpdateRecipientsMapInnerPasscodeDelivery

Passcode delivery settings. Always on for 21 CFR Part 11 documents and cannot be disabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable passcode delivery. Cannot be set to &#x60;false&#x60; on a 21 CFR Part 11 document: it returns a 422. | [optional] 
**methods** | **List[str]** | Delivery methods. Defaults to [\&quot;email\&quot;]. | [optional] 
**expire_after_access** | **bool** | Clear passcode after successful authentication. If passcode_delivery is also enabled, a new passcode is auto-generated on the next send request. Otherwise the recipient will no longer need a passcode. | [optional] 

## Example

```python
from signwell_sdk.models.update_recipients_map_inner_passcode_delivery import UpdateRecipientsMapInnerPasscodeDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecipientsMapInnerPasscodeDelivery from a JSON string
update_recipients_map_inner_passcode_delivery_instance = UpdateRecipientsMapInnerPasscodeDelivery.from_json(json)
# print the JSON string representation of the object
print(UpdateRecipientsMapInnerPasscodeDelivery.to_json())

# convert the object into a dict
update_recipients_map_inner_passcode_delivery_dict = update_recipients_map_inner_passcode_delivery_instance.to_dict()
# create an instance of UpdateRecipientsMapInnerPasscodeDelivery from a dict
update_recipients_map_inner_passcode_delivery_from_dict = UpdateRecipientsMapInnerPasscodeDelivery.from_dict(update_recipients_map_inner_passcode_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


