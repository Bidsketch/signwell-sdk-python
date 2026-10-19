# EmbeddedBrandingRequest

Branding for this document's embedded requesting and signing experiences. Every property is optional and independent. A property you supply overrides the selected API Application; one you omit inherits from it, then from the SignWell default. `company_logo` has one extra step between those two: the account's Settings > Branding logo, which applies on paid plans only. The colors and the border radius have no account step — omitting one falls straight through to the SignWell default. On Update and Send Document the object is a patch: only the properties you send change, and a property sent as `null` clears your override so the value inherits again. Sending `branding` itself as `null` clears every property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_logo** | [**EmbeddedBrandingRequestCompanyLogo**](EmbeddedBrandingRequestCompanyLogo.md) |  | [optional] 
**accent_color** | **str** | Accent color for this document&#39;s embedded pages, as a 6-digit HEX value. Returned normalized to &#x60;#RRGGBB&#x60;. | [optional] 
**button_label_color** | **str** | Button label color for this document&#39;s embedded pages, as a 6-digit HEX value. Returned normalized to &#x60;#RRGGBB&#x60;. | [optional] 
**link_color** | **str** | Link color for this document&#39;s embedded pages, as a 6-digit HEX value. Returned normalized to &#x60;#RRGGBB&#x60;. | [optional] 
**button_border_radius** | **int** | Corner radius of buttons on this document&#39;s embedded pages, in pixels. Must be between 0 and 25. | [optional] 

## Example

```python
from signwell_sdk.models.embedded_branding_request import EmbeddedBrandingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedBrandingRequest from a JSON string
embedded_branding_request_instance = EmbeddedBrandingRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedBrandingRequest.to_json())

# convert the object into a dict
embedded_branding_request_dict = embedded_branding_request_instance.to_dict()
# create an instance of EmbeddedBrandingRequest from a dict
embedded_branding_request_from_dict = EmbeddedBrandingRequest.from_dict(embedded_branding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


