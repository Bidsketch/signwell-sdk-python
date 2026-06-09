# DocumentTemplateResponsePlaceholdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**subject** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**preassigned_recipient_name** | **str** |  | [optional] 
**preassigned_recipient_email** | **str** |  | [optional] 
**signing_order** | **int** |  | [optional] 
**attachment_requests** | [**List[AttachmentRequestInfo]**](AttachmentRequestInfo.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.document_template_response_placeholders_inner import DocumentTemplateResponsePlaceholdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateResponsePlaceholdersInner from a JSON string
document_template_response_placeholders_inner_instance = DocumentTemplateResponsePlaceholdersInner.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateResponsePlaceholdersInner.to_json())

# convert the object into a dict
document_template_response_placeholders_inner_dict = document_template_response_placeholders_inner_instance.to_dict()
# create an instance of DocumentTemplateResponsePlaceholdersInner from a dict
document_template_response_placeholders_inner_from_dict = DocumentTemplateResponsePlaceholdersInner.from_dict(document_template_response_placeholders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


