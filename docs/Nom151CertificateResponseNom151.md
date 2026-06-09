# Nom151CertificateResponseNom151


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Certificate status (pending, issued, failed) | 
**transaction_id** | **str** | RSA signature / Transaction ID | 
**hash** | **str** | Document digest (SHA-256 hash) | 
**folio** | **str** | Certificate number / Folio | 
**issued_at** | **datetime** | Certificate issuance timestamp | 
**provider** | **str** | Certificate provider (e.g., SeguriData) | 
**validation_url** | **str** | URL to validate the certificate | 
**constancia** | **str** | Base64-encoded certificate file | 

## Example

```python
from signwell_sdk.models.nom151_certificate_response_nom151 import Nom151CertificateResponseNom151

# TODO update the JSON string below
json = "{}"
# create an instance of Nom151CertificateResponseNom151 from a JSON string
nom151_certificate_response_nom151_instance = Nom151CertificateResponseNom151.from_json(json)
# print the JSON string representation of the object
print(Nom151CertificateResponseNom151.to_json())

# convert the object into a dict
nom151_certificate_response_nom151_dict = nom151_certificate_response_nom151_instance.to_dict()
# create an instance of Nom151CertificateResponseNom151 from a dict
nom151_certificate_response_nom151_from_dict = Nom151CertificateResponseNom151.from_dict(nom151_certificate_response_nom151_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


