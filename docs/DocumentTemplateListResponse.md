# DocumentTemplateListResponse

List of templates with pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[DocumentTemplateResponse]**](DocumentTemplateResponse.md) |  | 
**current_page** | **int** |  | 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**total_count** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from signwell_sdk.models.document_template_list_response import DocumentTemplateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateListResponse from a JSON string
document_template_list_response_instance = DocumentTemplateListResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateListResponse.to_json())

# convert the object into a dict
document_template_list_response_dict = document_template_list_response_instance.to_dict()
# create an instance of DocumentTemplateListResponse from a dict
document_template_list_response_from_dict = DocumentTemplateListResponse.from_dict(document_template_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


