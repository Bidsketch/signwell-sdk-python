# ApiApplicationResponseOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | [optional] 
**name** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from signwell_sdk.models.api_application_response_owner import ApiApplicationResponseOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationResponseOwner from a JSON string
api_application_response_owner_instance = ApiApplicationResponseOwner.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationResponseOwner.to_json())

# convert the object into a dict
api_application_response_owner_dict = api_application_response_owner_instance.to_dict()
# create an instance of ApiApplicationResponseOwner from a dict
api_application_response_owner_from_dict = ApiApplicationResponseOwner.from_dict(api_application_response_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


