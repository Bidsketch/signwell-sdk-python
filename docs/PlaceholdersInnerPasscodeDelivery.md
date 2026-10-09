# PlaceholdersInnerPasscodeDelivery

Passcode delivery (OTP) settings for this placeholder. When enabled, documents created from this template inherit these settings for the corresponding recipient. While 21 CFR Part 11 is enabled for the workspace, a placeholder cannot disable passcode delivery: it returns a 422.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable passcode delivery for this recipient. Cannot be set to &#x60;false&#x60; on a 21 CFR Part 11 document: it returns a 422. | [optional] 
**methods** | **List[str]** | Delivery methods for the passcode. Currently supports: email. Defaults to [\&quot;email\&quot;] when omitted. | [optional] 
**expire_after_access** | **bool** | Whether the passcode expires after the recipient accesses the document. Inherited by documents created from this template. | [optional] 

## Example

```python
from signwell_sdk.models.placeholders_inner_passcode_delivery import PlaceholdersInnerPasscodeDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceholdersInnerPasscodeDelivery from a JSON string
placeholders_inner_passcode_delivery_instance = PlaceholdersInnerPasscodeDelivery.from_json(json)
# print the JSON string representation of the object
print(PlaceholdersInnerPasscodeDelivery.to_json())

# convert the object into a dict
placeholders_inner_passcode_delivery_dict = placeholders_inner_passcode_delivery_instance.to_dict()
# create an instance of PlaceholdersInnerPasscodeDelivery from a dict
placeholders_inner_passcode_delivery_from_dict = PlaceholdersInnerPasscodeDelivery.from_dict(placeholders_inner_passcode_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


