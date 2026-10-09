# EmbeddedRequest

Optional container for embedded settings. Purely additive: requests that omit it behave exactly as before, and the existing top-level `api_application_id`, `embedded_signing` and `embedded_signing_notifications` parameters are unchanged. Not supported on template endpoints, which return a `422` if it is present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding** | [**EmbeddedBrandingRequest**](EmbeddedBrandingRequest.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.embedded_request import EmbeddedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedRequest from a JSON string
embedded_request_instance = EmbeddedRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedRequest.to_json())

# convert the object into a dict
embedded_request_dict = embedded_request_instance.to_dict()
# create an instance of EmbeddedRequest from a dict
embedded_request_from_dict = EmbeddedRequest.from_dict(embedded_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


