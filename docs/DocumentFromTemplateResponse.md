# DocumentFromTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_mode** | **bool** |  | 
**id** | **str** |  | 
**template_id** | **str** |  | [optional] 
**template_ids** | **List[str]** |  | [optional] 
**api_application_id** | **str** |  | [optional] 
**requester_email_address** | **str** |  | [optional] 
**custom_requester_name** | **str** |  | [optional] 
**custom_requester_email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**recipients** | [**List[DocumentFromTemplateResponseRecipientsInner]**](DocumentFromTemplateResponseRecipientsInner.md) |  | [optional] 
**status** | **str** | Possible values: Draft, Created, Sending, Sent, Pending, Viewed, Completed, Manually completed, Declined, Canceled, Bounced, Blocked, Error, Expired | [optional] 
**reminders** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**embedded_signing** | **bool** |  | [optional] 
**embedded_edit_url** | **str** |  | [optional] 
**embedded_preview_url** | **str** |  | [optional] 
**apply_signing_order** | **bool** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**decline_redirect_url** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**decline_message** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**embedded_signing_notifications** | **bool** |  | [optional] 
**attachment_requests** | [**List[DocumentResponseAttachmentRequestsInner]**](DocumentResponseAttachmentRequestsInner.md) |  | [optional] 
**files** | [**List[FileInfo]**](FileInfo.md) |  | [optional] 
**copied_contacts** | [**List[CopiedContactInfo]**](CopiedContactInfo.md) |  | [optional] 
**fields** | **List[List[DocumentFromTemplateResponseFieldsInnerInner]]** |  | [optional] 
**allow_decline** | **bool** |  | [optional] 
**allow_reassign** | **bool** |  | [optional] 
**labels** | [**List[LabelInfo]**](LabelInfo.md) |  | [optional] 
**checkbox_groups** | [**List[CheckboxGroupInfo]**](CheckboxGroupInfo.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.document_from_template_response import DocumentFromTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFromTemplateResponse from a JSON string
document_from_template_response_instance = DocumentFromTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentFromTemplateResponse.to_json())

# convert the object into a dict
document_from_template_response_dict = document_from_template_response_instance.to_dict()
# create an instance of DocumentFromTemplateResponse from a dict
document_from_template_response_from_dict = DocumentFromTemplateResponse.from_dict(document_from_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


