# EmbeddedBrandingBranding

Only the properties actually set on the document. Every one is optional: an unset property is absent rather than null, because null is how a request clears one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_logo** | **str** | Write-only. Reports only that a logo was set, never its URL or Base64 payload. | [optional] 
**accent_color** | **str** | Hex, as #RRGGBB. | [optional] 
**button_label_color** | **str** | Hex, as #RRGGBB. | [optional] 
**link_color** | **str** | Hex, as #RRGGBB. | [optional] 
**button_border_radius** | **int** | Pixels, 0 to 25. | [optional] 

## Example

```python
from signwell_sdk.models.embedded_branding_branding import EmbeddedBrandingBranding

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedBrandingBranding from a JSON string
embedded_branding_branding_instance = EmbeddedBrandingBranding.from_json(json)
# print the JSON string representation of the object
print(EmbeddedBrandingBranding.to_json())

# convert the object into a dict
embedded_branding_branding_dict = embedded_branding_branding_instance.to_dict()
# create an instance of EmbeddedBrandingBranding from a dict
embedded_branding_branding_from_dict = EmbeddedBrandingBranding.from_dict(embedded_branding_branding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


