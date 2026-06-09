# MeResponseUserPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_document** | **bool** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**smart_fields** | **bool** |  | [optional] 

## Example

```python
from signwell_sdk.models.me_response_user_preferences import MeResponseUserPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of MeResponseUserPreferences from a JSON string
me_response_user_preferences_instance = MeResponseUserPreferences.from_json(json)
# print the JSON string representation of the object
print(MeResponseUserPreferences.to_json())

# convert the object into a dict
me_response_user_preferences_dict = me_response_user_preferences_instance.to_dict()
# create an instance of MeResponseUserPreferences from a dict
me_response_user_preferences_from_dict = MeResponseUserPreferences.from_dict(me_response_user_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


