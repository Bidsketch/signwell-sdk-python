# CopiedContactInfo

Copied contact information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Contact ID | [optional] 
**name** | **str** | Contact name | [optional] 
**email** | **str** | Contact email | 

## Example

```python
from signwell_sdk.models.copied_contact_info import CopiedContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CopiedContactInfo from a JSON string
copied_contact_info_instance = CopiedContactInfo.from_json(json)
# print the JSON string representation of the object
print(CopiedContactInfo.to_json())

# convert the object into a dict
copied_contact_info_dict = copied_contact_info_instance.to_dict()
# create an instance of CopiedContactInfo from a dict
copied_contact_info_from_dict = CopiedContactInfo.from_dict(copied_contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


