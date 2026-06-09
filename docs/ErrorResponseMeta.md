# ErrorResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error code identifier | 
**message** | **str** | Detailed error message | 
**messages** | **List[str]** | List of error messages | [optional] 

## Example

```python
from signwell_sdk.models.error_response_meta import ErrorResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseMeta from a JSON string
error_response_meta_instance = ErrorResponseMeta.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseMeta.to_json())

# convert the object into a dict
error_response_meta_dict = error_response_meta_instance.to_dict()
# create an instance of ErrorResponseMeta from a dict
error_response_meta_from_dict = ErrorResponseMeta.from_dict(error_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


