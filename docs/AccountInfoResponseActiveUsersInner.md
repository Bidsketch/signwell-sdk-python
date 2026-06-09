# AccountInfoResponseActiveUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**has_google_registration** | **bool** |  | [optional] 

## Example

```python
from signwell_sdk.models.account_info_response_active_users_inner import AccountInfoResponseActiveUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoResponseActiveUsersInner from a JSON string
account_info_response_active_users_inner_instance = AccountInfoResponseActiveUsersInner.from_json(json)
# print the JSON string representation of the object
print(AccountInfoResponseActiveUsersInner.to_json())

# convert the object into a dict
account_info_response_active_users_inner_dict = account_info_response_active_users_inner_instance.to_dict()
# create an instance of AccountInfoResponseActiveUsersInner from a dict
account_info_response_active_users_inner_from_dict = AccountInfoResponseActiveUsersInner.from_dict(account_info_response_active_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


