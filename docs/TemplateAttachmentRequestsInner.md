# TemplateAttachmentRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the requested attachment. | 
**placeholder_id** | **str** | Unique identifier of the recipient that will view the attachment request. | 
**required** | **bool** | Whether the recipient will need to upload the attachment to successfully complete/sign the document. Defaults to &#x60;true&#x60;. | [optional] [default to True]

## Example

```python
from signwell_sdk.models.template_attachment_requests_inner import TemplateAttachmentRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateAttachmentRequestsInner from a JSON string
template_attachment_requests_inner_instance = TemplateAttachmentRequestsInner.from_json(json)
# print the JSON string representation of the object
print(TemplateAttachmentRequestsInner.to_json())

# convert the object into a dict
template_attachment_requests_inner_dict = template_attachment_requests_inner_instance.to_dict()
# create an instance of TemplateAttachmentRequestsInner from a dict
template_attachment_requests_inner_from_dict = TemplateAttachmentRequestsInner.from_dict(template_attachment_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


