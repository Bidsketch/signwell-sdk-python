# DocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cfr_part11** | **bool** | Whether 21 CFR Part 11 controls apply to this document. Read-only: the value is taken from the workspace setting when the document is created and never changes afterwards. | [optional] 
**cfr_part11_signing_mode** | **str** | The signing mode of a 21 CFR Part 11 document: streamlined (one final authentication) or per_signature (authentication at every signature and initials field). Null when Part 11 does not apply. | [optional] 
**test_mode** | **bool** |  | 
**id** | **str** |  | 
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
**recipients** | [**List[DocumentResponseRecipientsInner]**](DocumentResponseRecipientsInner.md) |  | [optional] 
**status** | **str** | Possible values: Draft, Created, Sending, Sent, Pending, Viewed, Completed, Manually completed, Declined, Canceled, Bounced, Blocked, Error, Expired | [optional] 
**reminders** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**embedded** | [**EmbeddedBranding**](EmbeddedBranding.md) |  | [optional] 
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
**template_id** | **str** |  | [optional] 
**template_ids** | **List[str]** |  | [optional] 
**embedded_signing_notifications** | **bool** |  | [optional] 
**attachment_requests** | [**List[DocumentResponseAttachmentRequestsInner]**](DocumentResponseAttachmentRequestsInner.md) |  | [optional] 
**files** | [**List[FileInfo]**](FileInfo.md) |  | [optional] 
**copied_contacts** | [**List[CopiedContactInfo]**](CopiedContactInfo.md) |  | [optional] 
**fields** | **List[List[DocumentResponseFieldsInnerInner]]** |  | [optional] 
**allow_decline** | **bool** |  | [optional] 
**allow_reassign** | **bool** |  | [optional] 
**labels** | [**List[LabelInfo]**](LabelInfo.md) |  | [optional] 
**checkbox_groups** | [**List[CheckboxGroupInfo]**](CheckboxGroupInfo.md) |  | [optional] 
**conditional_rules** | [**List[ConditionalRuleInfo]**](ConditionalRuleInfo.md) |  | [optional] 
**conditional_logic_decisions** | [**List[ConditionalLogicDecisionInfo]**](ConditionalLogicDecisionInfo.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.document_response import DocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResponse from a JSON string
document_response_instance = DocumentResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentResponse.to_json())

# convert the object into a dict
document_response_dict = document_response_instance.to_dict()
# create an instance of DocumentResponse from a dict
document_response_from_dict = DocumentResponse.from_dict(document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


