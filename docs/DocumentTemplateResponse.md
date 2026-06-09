# DocumentTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**placeholders** | [**List[DocumentTemplateResponsePlaceholdersInner]**](DocumentTemplateResponsePlaceholdersInner.md) |  | [optional] 
**copied_placeholders** | [**List[DocumentTemplateResponseCopiedPlaceholdersInner]**](DocumentTemplateResponseCopiedPlaceholdersInner.md) |  | [optional] 
**status** | **str** |  | [optional] 
**reminders** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**embedded_edit_url** | **str** |  | [optional] 
**template_link** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**apply_signing_order** | **bool** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**decline_redirect_url** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**files** | [**List[FileInfo]**](FileInfo.md) |  | [optional] 
**fields** | **List[List[DocumentResponseFieldsInnerInner]]** |  | [optional] 
**allow_decline** | **bool** |  | [optional] 
**allow_reassign** | **bool** |  | [optional] 
**labels** | [**List[LabelInfo]**](LabelInfo.md) |  | [optional] 
**checkbox_groups** | [**List[CheckboxGroupInfo]**](CheckboxGroupInfo.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.document_template_response import DocumentTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateResponse from a JSON string
document_template_response_instance = DocumentTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateResponse.to_json())

# convert the object into a dict
document_template_response_dict = document_template_response_instance.to_dict()
# create an instance of DocumentTemplateResponse from a dict
document_template_response_from_dict = DocumentTemplateResponse.from_dict(document_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


