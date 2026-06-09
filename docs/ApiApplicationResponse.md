# ApiApplicationResponse

API application details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**callback_urls** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**owner** | [**ApiApplicationResponseOwner**](ApiApplicationResponseOwner.md) |  | [optional] 
**preferences** | [**ApiApplicationResponsePreferences**](ApiApplicationResponsePreferences.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.api_application_response import ApiApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationResponse from a JSON string
api_application_response_instance = ApiApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationResponse.to_json())

# convert the object into a dict
api_application_response_dict = api_application_response_instance.to_dict()
# create an instance of ApiApplicationResponse from a dict
api_application_response_from_dict = ApiApplicationResponse.from_dict(api_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


