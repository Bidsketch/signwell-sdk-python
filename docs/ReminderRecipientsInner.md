# ReminderRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Recipient&#39;s name (required if multiple recipients share the same email). | [optional] 
**email** | **str** | Recipient&#39;s email address. | [optional] 

## Example

```python
from signwell_sdk.models.reminder_recipients_inner import ReminderRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderRecipientsInner from a JSON string
reminder_recipients_inner_instance = ReminderRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(ReminderRecipientsInner.to_json())

# convert the object into a dict
reminder_recipients_inner_dict = reminder_recipients_inner_instance.to_dict()
# create an instance of ReminderRecipientsInner from a dict
reminder_recipients_inner_from_dict = ReminderRecipientsInner.from_dict(reminder_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


