# BulkSendCsvTemplateResponse

Base64-encoded CSV template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** | Base64-encoded CSV content | 

## Example

```python
from signwell_sdk.models.bulk_send_csv_template_response import BulkSendCsvTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendCsvTemplateResponse from a JSON string
bulk_send_csv_template_response_instance = BulkSendCsvTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(BulkSendCsvTemplateResponse.to_json())

# convert the object into a dict
bulk_send_csv_template_response_dict = bulk_send_csv_template_response_instance.to_dict()
# create an instance of BulkSendCsvTemplateResponse from a dict
bulk_send_csv_template_response_from_dict = BulkSendCsvTemplateResponse.from_dict(bulk_send_csv_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


