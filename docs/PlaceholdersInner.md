# PlaceholdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier that you will give to each placeholder. We recommend numbering sequentially from 1 to X. IDs are required for associating recipients to fields and more. | 
**name** | **str** | Name of the placeholder. | 
**preassigned_recipient_name** | **str** | In some cases, it may be necessary to pre-fill the name and email for a placeholder because it will always be the same person for all documents created from this template. This sets the name. Every recipient on a 21 CFR Part 11 document needs a name, so leaving it unset means the name has to be supplied when the document is created. | [optional] 
**preassigned_recipient_email** | **str** | In some cases, it may be necessary to pre-fill the name and email for a placeholder because it will always be the same person for all documents created from this template. This sets the email. | [optional] 
**passcode_delivery** | [**PlaceholdersInnerPasscodeDelivery**](PlaceholdersInnerPasscodeDelivery.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.placeholders_inner import PlaceholdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceholdersInner from a JSON string
placeholders_inner_instance = PlaceholdersInner.from_json(json)
# print the JSON string representation of the object
print(PlaceholdersInner.to_json())

# convert the object into a dict
placeholders_inner_dict = placeholders_inner_instance.to_dict()
# create an instance of PlaceholdersInner from a dict
placeholders_inner_from_dict = PlaceholdersInner.from_dict(placeholders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


