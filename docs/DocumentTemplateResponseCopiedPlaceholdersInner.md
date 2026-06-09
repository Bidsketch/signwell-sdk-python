# DocumentTemplateResponseCopiedPlaceholdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**placeholder_id** | **str** |  | [optional] 
**name** | **str** |  | 
**subject** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**preassigned_recipient_name** | **str** |  | [optional] 
**preassigned_recipient_email** | **str** |  | [optional] 

## Example

```python
from signwell_sdk.models.document_template_response_copied_placeholders_inner import DocumentTemplateResponseCopiedPlaceholdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateResponseCopiedPlaceholdersInner from a JSON string
document_template_response_copied_placeholders_inner_instance = DocumentTemplateResponseCopiedPlaceholdersInner.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateResponseCopiedPlaceholdersInner.to_json())

# convert the object into a dict
document_template_response_copied_placeholders_inner_dict = document_template_response_copied_placeholders_inner_instance.to_dict()
# create an instance of DocumentTemplateResponseCopiedPlaceholdersInner from a dict
document_template_response_copied_placeholders_inner_from_dict = DocumentTemplateResponseCopiedPlaceholdersInner.from_dict(document_template_response_copied_placeholders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


