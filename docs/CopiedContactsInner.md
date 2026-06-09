# CopiedContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the copied contact. | [optional] 
**email** | **str** | Email for the copied contact. | 

## Example

```python
from signwell_sdk.models.copied_contacts_inner import CopiedContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopiedContactsInner from a JSON string
copied_contacts_inner_instance = CopiedContactsInner.from_json(json)
# print the JSON string representation of the object
print(CopiedContactsInner.to_json())

# convert the object into a dict
copied_contacts_inner_dict = copied_contacts_inner_instance.to_dict()
# create an instance of CopiedContactsInner from a dict
copied_contacts_inner_from_dict = CopiedContactsInner.from_dict(copied_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


