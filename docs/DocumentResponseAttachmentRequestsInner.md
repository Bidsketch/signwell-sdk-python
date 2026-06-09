# DocumentResponseAttachmentRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**recipient_id** | **str** |  | 
**required** | **bool** |  | [optional] 

## Example

```python
from signwell_sdk.models.document_response_attachment_requests_inner import DocumentResponseAttachmentRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResponseAttachmentRequestsInner from a JSON string
document_response_attachment_requests_inner_instance = DocumentResponseAttachmentRequestsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentResponseAttachmentRequestsInner.to_json())

# convert the object into a dict
document_response_attachment_requests_inner_dict = document_response_attachment_requests_inner_instance.to_dict()
# create an instance of DocumentResponseAttachmentRequestsInner from a dict
document_response_attachment_requests_inner_from_dict = DocumentResponseAttachmentRequestsInner.from_dict(document_response_attachment_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


