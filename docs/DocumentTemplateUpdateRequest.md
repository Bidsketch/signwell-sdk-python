# DocumentTemplateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the template. | [optional] 
**subject** | **str** | Email subject for the signature request that recipients will see. Defaults to the default system subject or a template subject (if the document is created from a template). | [optional] 
**message** | **str** | Email message for the signature request that recipients will see. Defaults to the default system message or a template message (if the document is created from a template). | [optional] 
**draft** | **bool** | Whether the template can still be updated before it is ready for usage. If set to &#x60;false&#x60; the template is marked as &#x60;Available&#x60; and it will be ready for use. Defaults to &#x60;false&#x60;. | [optional] [default to False]
**expires_in** | **int** | Number of days before the signature request expires. Defaults to the account expiration setting or template expiration (if the document is created from a template). | [optional] 
**reminders** | **bool** | Whether to send signing reminders to recipients. Reminders are sent on day 3, day 6, and day 10 if set to &#x60;true&#x60;. Defaults to &#x60;true&#x60;. | [optional] [default to True]
**apply_signing_order** | **bool** | When set to &#x60;true&#x60; recipients will sign one at a time in the order of the &#x60;recipients&#x60; collection of this request. | [optional] [default to False]
**api_application_id** | **str** | Unique identifier for API Application settings to use. API Applications are optional and mainly used when isolating OAuth apps or for more control over embedded API settings | [optional] 
**redirect_url** | **str** | A URL that recipients are redirected to after successfully signing a document. | [optional] 
**allow_decline** | **bool** | Whether to allow recipients the option to decline signing a document. If multiple signers are involved in a document, any single recipient can cancel the entire document signing process by declining to sign. | [optional] [default to True]
**allow_reassign** | **bool** | In some cases a signer is not the right person to sign and may need to reassign their signing responsibilities to another person. This feature allows them to reassign the document to someone else. | [optional] [default to True]
**decline_redirect_url** | **str** | A URL that recipients are redirected to if the document is declined. | [optional] 
**metadata** | **Dict[str, str]** | Optional key-value data that can be associated with the document. If set, will be available every time the document data is returned. | [optional] 
**labels** | [**List[LabelRequest]**](LabelRequest.md) | Labels can be used to organize documents in a way that can make it easy to find using the document search in SignWell. A document can have multiple labels. Updating labels on a document will replace any existing labels for that document. | [optional] 
**checkbox_groups** | [**List[TemplateCheckboxGroupsInner]**](TemplateCheckboxGroupsInner.md) | Checkbox fields that are placed on a document can be grouped with selection requirements. At least 2 checkbox fields in an array of fields must be assigned to the same recipient. | [optional] 

## Example

```python
from signwell_sdk.models.document_template_update_request import DocumentTemplateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateUpdateRequest from a JSON string
document_template_update_request_instance = DocumentTemplateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateUpdateRequest.to_json())

# convert the object into a dict
document_template_update_request_dict = document_template_update_request_instance.to_dict()
# create an instance of DocumentTemplateUpdateRequest from a dict
document_template_update_request_from_dict = DocumentTemplateUpdateRequest.from_dict(document_template_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


