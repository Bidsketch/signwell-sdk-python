# DocumentTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FilesInner]**](FilesInner.md) | Document files can be uploaded by specifying a file URL or base64 string. Either &#x60;file_url&#x60; or &#x60;file_base64&#x60; must be present (not both). Valid file types are: .pdf, .doc, .docx, .pages, .ppt, .pptx, .key, .xls, .xlsx, .numbers, .jpg, .jpeg, .png, .tiff, .tif, .webp, .html, and .htm | 
**name** | **str** | The name of the template. | [optional] 
**subject** | **str** | Email subject for the signature request that recipients will see. Defaults to the default system subject or a template subject (if the document is created from a template). | [optional] 
**message** | **str** | Email message for the signature request that recipients will see. Defaults to the default system message or a template message (if the document is created from a template). | [optional] 
**placeholders** | [**List[PlaceholdersInner]**](PlaceholdersInner.md) | Placeholders are generally job roles that must complete and/or sign the document. For example, a placeholder might be “Client” or “Legal Department”. When a document is created from the template, you assign a person to each placeholder. | 
**copied_placeholders** | [**List[CopiedPlaceholdersInner]**](CopiedPlaceholdersInner.md) | Copied placeholders are emailed the final document once it has been completed by all recipients. | [optional] 
**draft** | **bool** | Whether the template can still be updated before it is ready for usage. If set to &#x60;false&#x60; the template is marked as &#x60;Available&#x60; and it will be ready for use. Defaults to &#x60;false&#x60;. | [optional] [default to False]
**expires_in** | **int** | Number of days before the signature request expires. Defaults to the account expiration setting or template expiration (if the document is created from a template). | [optional] 
**reminders** | **bool** | Whether to send signing reminders to recipients. Reminders are sent on day 3, day 6, and day 10 if set to &#x60;true&#x60;. Defaults to &#x60;true&#x60;. | [optional] [default to True]
**apply_signing_order** | **bool** | When set to &#x60;true&#x60; recipients will sign one at a time in the order of the &#x60;recipients&#x60; collection of this request. | [optional] [default to False]
**api_application_id** | **str** | Unique identifier for API Application settings to use. API Applications are optional and mainly used when isolating OAuth apps or for more control over embedded API settings | [optional] 
**text_tags** | **bool** | An alternative way (if you can’t use the recommended way) of placing fields in specific locations of your document by using special text tags. Useful when changing the content of your files changes the location of fields. See API documentation for “Text Tags” for details. Defaults to false. | [optional] [default to False]
**redirect_url** | **str** | A URL that recipients are redirected to after successfully signing a document. | [optional] 
**allow_decline** | **bool** | Whether to allow recipients the option to decline signing a document. If multiple signers are involved in a document, any single recipient can cancel the entire document signing process by declining to sign. | [optional] [default to True]
**allow_reassign** | **bool** | In some cases a signer is not the right person to sign and may need to reassign their signing responsibilities to another person. This feature allows them to reassign the document to someone else. | [optional] [default to True]
**decline_redirect_url** | **str** | A URL that recipients are redirected to if the document is declined. | [optional] 
**language** | **str** | Sets the language for the template and documents created from the template for all recipient side interactions including the document email and the document itself. Accepted languages: English, Français, Español, Deutsch, Polski, Português, Dansk, Nederlands, Italiano, Русский, Svenska, العربية, Ελληνικά, Türkçe, Slovenčina. Language should be sent in ISO 639-1 format: en, fr, es, de, pl, pt, da, nl, it, ru, sv, ar, el, tr, sk. | [optional] 
**metadata** | **Dict[str, str]** | Optional key-value data that can be associated with the document. If set, will be available every time the document data is returned. | [optional] 
**fields** | **List[List[TemplateFieldsInnerInner]]** | Document fields placed on a document for collecting data or signatures from recipients. At least one field must be present in the Create Document request if &#x60;draft&#x60; is &#x60;false&#x60; (unless adding a signature page by using &#x60;with_signature_page&#x60;). Field data should be sent as a 2-dimensional JSON array. One array of fields is needed for each file in the files array. An array of fields can be empty if you have a file that does not contain any fields. | [optional] 
**attachment_requests** | [**List[TemplateAttachmentRequestsInner]**](TemplateAttachmentRequestsInner.md) | Attachments that a recipient must upload to complete the signing process. Attachment requests are shown after all document fields have been completed. | [optional] 
**labels** | [**List[LabelRequest]**](LabelRequest.md) | Labels can be used to organize documents in a way that can make it easy to find using the document search in SignWell. A document can have multiple labels. | [optional] 
**checkbox_groups** | [**List[TemplateCheckboxGroupsInner]**](TemplateCheckboxGroupsInner.md) | Checkbox fields that are placed on a document can be grouped with selection requirements. At least 2 checkbox fields in an array of fields must be assigned to the same recipient. | [optional] 

## Example

```python
from signwell_sdk.models.document_template_request import DocumentTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateRequest from a JSON string
document_template_request_instance = DocumentTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateRequest.to_json())

# convert the object into a dict
document_template_request_dict = document_template_request_instance.to_dict()
# create an instance of DocumentTemplateRequest from a dict
document_template_request_from_dict = DocumentTemplateRequest.from_dict(document_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


