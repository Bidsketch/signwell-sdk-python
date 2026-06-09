# DocumentFromTemplateResponseFieldsInnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | 
**y** | **float** |  | 
**page** | **int** |  | 
**recipient** | [**DocumentFromTemplateResponseFieldsInnerInnerRecipient**](DocumentFromTemplateResponseFieldsInnerInnerRecipient.md) |  | [optional] 
**api_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_format** | [**DateFormat**](DateFormat.md) |  | [optional] 
**fixed_width** | **bool** |  | [optional] 
**formula** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**lock_sign_date** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**type** | [**FieldType**](FieldType.md) |  | [optional] 
**validation** | [**TextValidation**](TextValidation.md) |  | [optional] 
**value** | [**DocumentResponseFieldsInnerInnerValue**](DocumentResponseFieldsInnerInnerValue.md) |  | [optional] 
**height** | **str** |  | [optional] 
**width** | **str** |  | [optional] 
**recipient_id** | **str** |  | [optional] 
**signing_elements_group_id** | **str** |  | [optional] 
**placeholder_name** | **str** |  | [optional] 
**options** | [**List[DocumentResponseFieldsInnerInnerOptionsInner]**](DocumentResponseFieldsInnerInnerOptionsInner.md) | Dropdown options (for dropdown/select fields) | [optional] 
**default_option** | **str** | Default selected option | [optional] 
**allow_other** | **bool** | Whether \&quot;Other\&quot; option is allowed | [optional] 

## Example

```python
from signwell_sdk.models.document_from_template_response_fields_inner_inner import DocumentFromTemplateResponseFieldsInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFromTemplateResponseFieldsInnerInner from a JSON string
document_from_template_response_fields_inner_inner_instance = DocumentFromTemplateResponseFieldsInnerInner.from_json(json)
# print the JSON string representation of the object
print(DocumentFromTemplateResponseFieldsInnerInner.to_json())

# convert the object into a dict
document_from_template_response_fields_inner_inner_dict = document_from_template_response_fields_inner_inner_instance.to_dict()
# create an instance of DocumentFromTemplateResponseFieldsInnerInner from a dict
document_from_template_response_fields_inner_inner_from_dict = DocumentFromTemplateResponseFieldsInnerInner.from_dict(document_from_template_response_fields_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


