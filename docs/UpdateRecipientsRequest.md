# UpdateRecipientsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[UpdateRecipientsMapInner]**](UpdateRecipientsMapInner.md) | List of recipients to update on the document. | 

## Example

```python
from signwell_sdk.models.update_recipients_request import UpdateRecipientsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecipientsRequest from a JSON string
update_recipients_request_instance = UpdateRecipientsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRecipientsRequest.to_json())

# convert the object into a dict
update_recipients_request_dict = update_recipients_request_instance.to_dict()
# create an instance of UpdateRecipientsRequest from a dict
update_recipients_request_from_dict = UpdateRecipientsRequest.from_dict(update_recipients_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


