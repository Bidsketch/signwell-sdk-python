# MeResponse

Account information associated with the API key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Membership ID | 
**role** | **str** | Role within the account (e.g. owner, admin, member) | 
**archived** | **bool** |  | [optional] 
**user** | [**MeResponseUser**](MeResponseUser.md) |  | 
**account** | [**AccountInfoResponse**](AccountInfoResponse.md) |  | 
**workspace** | [**AccountInfoResponse**](AccountInfoResponse.md) |  | 
**contact** | [**MeResponseContact**](MeResponseContact.md) |  | 

## Example

```python
from signwell_sdk.models.me_response import MeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeResponse from a JSON string
me_response_instance = MeResponse.from_json(json)
# print the JSON string representation of the object
print(MeResponse.to_json())

# convert the object into a dict
me_response_dict = me_response_instance.to_dict()
# create an instance of MeResponse from a dict
me_response_from_dict = MeResponse.from_dict(me_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


