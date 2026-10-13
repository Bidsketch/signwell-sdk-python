# BulkSendCsvRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[str]** | Specify one or more templates to generate a single blank CSV file that will contain available columns for your recipient data. The template_ids[] parameter is an array of template IDs (e.g.,&#x60;/?template_ids[]&#x3D;5a67dbd7-928a-4ea0-a7e2-e476a0eb045f&amp;template_ids[]&#x3D;d7315111-c671-4b15-8354-c9a19bbaefa0&#x60;). Each ID should be a separate parameter in the query string. | 
**bulk_send_csv** | **str** | A RFC 4648 base64 string of the template CSV file to be validated. While 21 CFR Part 11 is enabled, every recipient needs a name: the CSV must carry a name column next to each placeholder email column (for example &#x60;signer_name&#x60; alongside &#x60;signer_email&#x60;), and each row must fill that name in wherever it carries the matching email, otherwise it returns a 422. A row that leaves both the email and the name blank sends nothing to that placeholder, so no name is needed there. | 

## Example

```python
from signwell_sdk.models.bulk_send_csv_request import BulkSendCsvRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendCsvRequest from a JSON string
bulk_send_csv_request_instance = BulkSendCsvRequest.from_json(json)
# print the JSON string representation of the object
print(BulkSendCsvRequest.to_json())

# convert the object into a dict
bulk_send_csv_request_dict = bulk_send_csv_request_instance.to_dict()
# create an instance of BulkSendCsvRequest from a dict
bulk_send_csv_request_from_dict = BulkSendCsvRequest.from_dict(bulk_send_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


