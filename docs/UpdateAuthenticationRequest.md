# UpdateAuthenticationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[UpdateAuthenticationRequestRecipientsInner]**](UpdateAuthenticationRequestRecipientsInner.md) | Recipients whose authentication settings should be updated. | 

## Example

```python
from signwell_sdk.models.update_authentication_request import UpdateAuthenticationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthenticationRequest from a JSON string
update_authentication_request_instance = UpdateAuthenticationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAuthenticationRequest.to_json())

# convert the object into a dict
update_authentication_request_dict = update_authentication_request_instance.to_dict()
# create an instance of UpdateAuthenticationRequest from a dict
update_authentication_request_from_dict = UpdateAuthenticationRequest.from_dict(update_authentication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


