# AttachmentRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the requested attachment. | 
**recipient_id** | **str** | Unique identifier of the recipient that will view the attachment request. | 
**required** | **bool** | Whether the recipient will need to upload the attachment to successfully complete/sign the document. Defaults to &#x60;true&#x60;. | [optional] [default to True]

## Example

```python
from signwell_sdk.models.attachment_requests_inner import AttachmentRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRequestsInner from a JSON string
attachment_requests_inner_instance = AttachmentRequestsInner.from_json(json)
# print the JSON string representation of the object
print(AttachmentRequestsInner.to_json())

# convert the object into a dict
attachment_requests_inner_dict = attachment_requests_inner_instance.to_dict()
# create an instance of AttachmentRequestsInner from a dict
attachment_requests_inner_from_dict = AttachmentRequestsInner.from_dict(attachment_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


