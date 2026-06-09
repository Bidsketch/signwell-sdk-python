# Nom151UrlResponse

NOM-151 download URL returned when url_only=true

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to download the certificate ZIP file | 

## Example

```python
from signwell_sdk.models.nom151_url_response import Nom151UrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Nom151UrlResponse from a JSON string
nom151_url_response_instance = Nom151UrlResponse.from_json(json)
# print the JSON string representation of the object
print(Nom151UrlResponse.to_json())

# convert the object into a dict
nom151_url_response_dict = nom151_url_response_instance.to_dict()
# create an instance of Nom151UrlResponse from a dict
nom151_url_response_from_dict = Nom151UrlResponse.from_dict(nom151_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


