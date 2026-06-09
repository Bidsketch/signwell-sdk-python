# MeResponseUser

The authenticated user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**has_google_registration** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**preferences** | [**MeResponseUserPreferences**](MeResponseUserPreferences.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.me_response_user import MeResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of MeResponseUser from a JSON string
me_response_user_instance = MeResponseUser.from_json(json)
# print the JSON string representation of the object
print(MeResponseUser.to_json())

# convert the object into a dict
me_response_user_dict = me_response_user_instance.to_dict()
# create an instance of MeResponseUser from a dict
me_response_user_from_dict = MeResponseUser.from_dict(me_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


