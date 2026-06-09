# ValidationErrorResponse

Validation error response. The errors object contains field-specific error details with dynamic keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, object]** | Field-specific validation errors. Keys are field names (e.g., recipients, fields, files). Values can be strings, arrays of strings, or nested objects with further field-specific errors. | 

## Example

```python
from signwell_sdk.models.validation_error_response import ValidationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponse from a JSON string
validation_error_response_instance = ValidationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponse.to_json())

# convert the object into a dict
validation_error_response_dict = validation_error_response_instance.to_dict()
# create an instance of ValidationErrorResponse from a dict
validation_error_response_from_dict = ValidationErrorResponse.from_dict(validation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


