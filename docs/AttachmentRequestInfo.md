# AttachmentRequestInfo

Attachment request information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the attachment request | 
**url** | **str** | URL of the uploaded attachment (when available) | [optional] 
**required** | **bool** | Whether the attachment is required | 

## Example

```python
from signwell_sdk.models.attachment_request_info import AttachmentRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRequestInfo from a JSON string
attachment_request_info_instance = AttachmentRequestInfo.from_json(json)
# print the JSON string representation of the object
print(AttachmentRequestInfo.to_json())

# convert the object into a dict
attachment_request_info_dict = attachment_request_info_instance.to_dict()
# create an instance of AttachmentRequestInfo from a dict
attachment_request_info_from_dict = AttachmentRequestInfo.from_dict(attachment_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


