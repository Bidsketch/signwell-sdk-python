# Nom151CertificateResponse

NOM-151 certificate data returned when object_only=true

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nom151** | [**Nom151CertificateResponseNom151**](Nom151CertificateResponseNom151.md) |  | 

## Example

```python
from signwell_sdk.models.nom151_certificate_response import Nom151CertificateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Nom151CertificateResponse from a JSON string
nom151_certificate_response_instance = Nom151CertificateResponse.from_json(json)
# print the JSON string representation of the object
print(Nom151CertificateResponse.to_json())

# convert the object into a dict
nom151_certificate_response_dict = nom151_certificate_response_instance.to_dict()
# create an instance of Nom151CertificateResponse from a dict
nom151_certificate_response_from_dict = Nom151CertificateResponse.from_dict(nom151_certificate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


