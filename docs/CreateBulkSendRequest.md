# CreateBulkSendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[str]** | Unique identifiers for a list of templates. | 
**bulk_send_csv** | **str** | A RFC 4648 base64 string of the template CSV file to be validated. | 
**skip_row_errors** | **bool** | Whether to skip errors in the rows. Defaults to &#x60;false&#x60;. | [optional] [default to False]
**api_application_id** | **str** | Unique identifier for API Application settings to use. API Applications are optional and mainly used when isolating OAuth apps or for more control over embedded API settings | [optional] 
**name** | **str** | The name of the Bulk Send. Will be used as the document name for each of the documents. | [optional] 
**subject** | **str** | Email subject for the signature request that recipients will see. Defaults to the default system subject or a template subject. | [optional] 
**message** | **str** | Email message for the signature request that recipients will see. Defaults to the default system message or a template message. | [optional] 
**apply_signing_order** | **bool** | When set to &#x60;true&#x60; recipients will sign one at a time in the order of the &#x60;recipients&#x60; collection of this request. | [optional] [default to False]
**custom_requester_name** | **str** | Sets the custom requester name for the document. When set, this is the name used for all email communications, signing notifications, and in the audit file. | [optional] 
**custom_requester_email** | **str** | Sets the custom requester email for the document. When set, this is the email used for all email communications, signing notifications, and in the audit file. | [optional] 

## Example

```python
from signwell_sdk.models.create_bulk_send_request import CreateBulkSendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkSendRequest from a JSON string
create_bulk_send_request_instance = CreateBulkSendRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBulkSendRequest.to_json())

# convert the object into a dict
create_bulk_send_request_dict = create_bulk_send_request_instance.to_dict()
# create an instance of CreateBulkSendRequest from a dict
create_bulk_send_request_from_dict = CreateBulkSendRequest.from_dict(create_bulk_send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


