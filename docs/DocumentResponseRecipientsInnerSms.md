# DocumentResponseRecipientsInnerSms

SMS delivery metadata. Only present when delivery_method includes SMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_masked** | **str** | Masked phone number; the full number never leaves the API. | [optional] 
**send_sms** | **bool** |  | [optional] 
**send_sms_delay** | **int** |  | [optional] 
**delivery_status** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**failed** | **bool** |  | [optional] 
**failed_details** | **str** |  | [optional] 

## Example

```python
from signwell_sdk.models.document_response_recipients_inner_sms import DocumentResponseRecipientsInnerSms

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResponseRecipientsInnerSms from a JSON string
document_response_recipients_inner_sms_instance = DocumentResponseRecipientsInnerSms.from_json(json)
# print the JSON string representation of the object
print(DocumentResponseRecipientsInnerSms.to_json())

# convert the object into a dict
document_response_recipients_inner_sms_dict = document_response_recipients_inner_sms_instance.to_dict()
# create an instance of DocumentResponseRecipientsInnerSms from a dict
document_response_recipients_inner_sms_from_dict = DocumentResponseRecipientsInnerSms.from_dict(document_response_recipients_inner_sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


