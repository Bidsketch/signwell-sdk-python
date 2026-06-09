# MeResponseContact

The contact record for the authenticated user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**company_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**alt_phone_number** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**initials** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 

## Example

```python
from signwell_sdk.models.me_response_contact import MeResponseContact

# TODO update the JSON string below
json = "{}"
# create an instance of MeResponseContact from a JSON string
me_response_contact_instance = MeResponseContact.from_json(json)
# print the JSON string representation of the object
print(MeResponseContact.to_json())

# convert the object into a dict
me_response_contact_dict = me_response_contact_instance.to_dict()
# create an instance of MeResponseContact from a dict
me_response_contact_from_dict = MeResponseContact.from_dict(me_response_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


