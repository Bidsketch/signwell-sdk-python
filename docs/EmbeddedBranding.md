# EmbeddedBranding

The branding the caller set on THIS document, echoed back. Null when the caller set none: the document then renders with the API Application, workspace or system branding, and that resolved branding is deliberately not reported here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding** | [**EmbeddedBrandingBranding**](EmbeddedBrandingBranding.md) |  | 

## Example

```python
from signwell_sdk.models.embedded_branding import EmbeddedBranding

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedBranding from a JSON string
embedded_branding_instance = EmbeddedBranding.from_json(json)
# print the JSON string representation of the object
print(EmbeddedBranding.to_json())

# convert the object into a dict
embedded_branding_dict = embedded_branding_instance.to_dict()
# create an instance of EmbeddedBranding from a dict
embedded_branding_from_dict = EmbeddedBranding.from_dict(embedded_branding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


