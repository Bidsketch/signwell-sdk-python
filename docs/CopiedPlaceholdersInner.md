# CopiedPlaceholdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the placeholder. | 
**preassigned_recipient_name** | **str** | In some cases, it may be necessary to pre-fill the name and email for a placeholder because it will always be the same person for all documents created from this template. This sets the name. | [optional] 
**preassigned_recipient_email** | **str** | In some cases, it may be necessary to pre-fill the name and email for a placeholder because it will always be the same person for all documents created from this template. This sets the email. | [optional] 

## Example

```python
from signwell_sdk.models.copied_placeholders_inner import CopiedPlaceholdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopiedPlaceholdersInner from a JSON string
copied_placeholders_inner_instance = CopiedPlaceholdersInner.from_json(json)
# print the JSON string representation of the object
print(CopiedPlaceholdersInner.to_json())

# convert the object into a dict
copied_placeholders_inner_dict = copied_placeholders_inner_instance.to_dict()
# create an instance of CopiedPlaceholdersInner from a dict
copied_placeholders_inner_from_dict = CopiedPlaceholdersInner.from_dict(copied_placeholders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


