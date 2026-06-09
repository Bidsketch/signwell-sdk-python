# SendReminderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[ReminderRecipientsInner]**](ReminderRecipientsInner.md) | Optional list if recipients within the document to send a reminder email to. If none are specified, all recipients that have not signed yet will receive a reminder email. | [optional] 

## Example

```python
from signwell_sdk.models.send_reminder_request import SendReminderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendReminderRequest from a JSON string
send_reminder_request_instance = SendReminderRequest.from_json(json)
# print the JSON string representation of the object
print(SendReminderRequest.to_json())

# convert the object into a dict
send_reminder_request_dict = send_reminder_request_instance.to_dict()
# create an instance of SendReminderRequest from a dict
send_reminder_request_from_dict = SendReminderRequest.from_dict(send_reminder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


