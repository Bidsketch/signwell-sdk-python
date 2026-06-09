# AccountInfoResponse

Account or workspace information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**plan_tier** | **str** |  | 
**active_templates** | **int** |  | [optional] 
**can_create_template** | **bool** |  | [optional] 
**can_create_tracking_document** | **bool** |  | [optional] 
**can_create_completion_document** | **bool** |  | [optional] 
**active_users** | [**List[AccountInfoResponseActiveUsersInner]**](AccountInfoResponseActiveUsersInner.md) |  | [optional] 
**preferences** | [**AccountInfoResponsePreferences**](AccountInfoResponsePreferences.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.account_info_response import AccountInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoResponse from a JSON string
account_info_response_instance = AccountInfoResponse.from_json(json)
# print the JSON string representation of the object
print(AccountInfoResponse.to_json())

# convert the object into a dict
account_info_response_dict = account_info_response_instance.to_dict()
# create an instance of AccountInfoResponse from a dict
account_info_response_from_dict = AccountInfoResponse.from_dict(account_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


