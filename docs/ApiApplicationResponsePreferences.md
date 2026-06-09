# ApiApplicationResponsePreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_text_color** | **str** |  | [optional] 
**buttons_border_radius** | **int** |  | [optional] 
**custom_logo_file** | **str** |  | [optional] 
**link_text_color** | **str** |  | [optional] 
**primary_color** | **str** |  | [optional] 

## Example

```python
from signwell_sdk.models.api_application_response_preferences import ApiApplicationResponsePreferences

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationResponsePreferences from a JSON string
api_application_response_preferences_instance = ApiApplicationResponsePreferences.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationResponsePreferences.to_json())

# convert the object into a dict
api_application_response_preferences_dict = api_application_response_preferences_instance.to_dict()
# create an instance of ApiApplicationResponsePreferences from a dict
api_application_response_preferences_from_dict = ApiApplicationResponsePreferences.from_dict(api_application_response_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


