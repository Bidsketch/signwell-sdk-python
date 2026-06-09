# DocumentFromTemplateResponseRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | 
**role** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**send_email** | **bool** |  | [optional] 
**send_email_delay** | **int** |  | [optional] 
**signing_order** | **int** |  | [optional] 
**signing_url** | **str** |  | [optional] 
**embedded_signing_url** | **str** |  | [optional] 
**bounced** | **bool** |  | [optional] 
**bounced_details** | **str** |  | [optional] 
**attachment_requests** | [**List[AttachmentRequestInfo]**](AttachmentRequestInfo.md) |  | [optional] 
**passcode** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**placeholder_name** | **str** |  | [optional] 

## Example

```python
from signwell_sdk.models.document_from_template_response_recipients_inner import DocumentFromTemplateResponseRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFromTemplateResponseRecipientsInner from a JSON string
document_from_template_response_recipients_inner_instance = DocumentFromTemplateResponseRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentFromTemplateResponseRecipientsInner.to_json())

# convert the object into a dict
document_from_template_response_recipients_inner_dict = document_from_template_response_recipients_inner_instance.to_dict()
# create an instance of DocumentFromTemplateResponseRecipientsInner from a dict
document_from_template_response_recipients_inner_from_dict = DocumentFromTemplateResponseRecipientsInner.from_dict(document_from_template_response_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


