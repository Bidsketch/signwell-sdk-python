# TemplateRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier that you will give to each recipient. We recommend numbering sequentially from 1 to X. IDs are required for associating recipients to fields and more. | 
**name** | **str** | Name of the recipient. | [optional] 
**email** | **str** | Email address for the recipient. | 
**placeholder_name** | **str** | The name of the placeholder you want this recipient assigned to. | [optional] 
**passcode** | **str** | If set, signers assigned with a passcode will be required to enter the passcode before they’re able to view and complete the document. | [optional] 
**subject** | **str** | Email subject for the signature request that the recipient will see. Overrides the general subject for the template. | [optional] 
**message** | **str** | Email message for the signature request that the recipient will see. Overrides the general message for the template. | [optional] 
**send_email** | **bool** | Applies on when &#x60;embedded_signing&#x60; is &#x60;true&#x60;. By default, recipients are not notified through email to sign when doing embedded signing. Setting this to &#x60;true&#x60;  will send a notification email to the recipient. Default is &#x60;false&#x60;. | [optional] [default to False]
**send_email_delay** | **int** | If &#x60;send_email&#x60; is &#x60;true&#x60; recipients will receive a new document notification immediately. In the case of embedded signing, you can delay this notification to only send if the document is not completed within a few minutes. The email notification will not go out if the document is completed before the delay time is over. Valid values are in minutes ranging from &#x60;0&#x60; to &#x60;60&#x60;. Defaults to &#x60;0&#x60;. | [optional] [default to 0]

## Example

```python
from signwell_sdk.models.template_recipients_inner import TemplateRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRecipientsInner from a JSON string
template_recipients_inner_instance = TemplateRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(TemplateRecipientsInner.to_json())

# convert the object into a dict
template_recipients_inner_dict = template_recipients_inner_instance.to_dict()
# create an instance of TemplateRecipientsInner from a dict
template_recipients_inner_from_dict = TemplateRecipientsInner.from_dict(template_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


