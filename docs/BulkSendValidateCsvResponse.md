# BulkSendValidateCsvResponse

Validated bulk send CSV response with defaults applied

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_send_csv** | **str** | Base64-encoded CSV content | 
**template_ids** | **List[str]** |  | 
**skip_row_errors** | **bool** |  | [optional] 
**api_application_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**apply_signing_order** | **bool** |  | [optional] 

## Example

```python
from signwell_sdk.models.bulk_send_validate_csv_response import BulkSendValidateCsvResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSendValidateCsvResponse from a JSON string
bulk_send_validate_csv_response_instance = BulkSendValidateCsvResponse.from_json(json)
# print the JSON string representation of the object
print(BulkSendValidateCsvResponse.to_json())

# convert the object into a dict
bulk_send_validate_csv_response_dict = bulk_send_validate_csv_response_instance.to_dict()
# create an instance of BulkSendValidateCsvResponse from a dict
bulk_send_validate_csv_response_from_dict = BulkSendValidateCsvResponse.from_dict(bulk_send_validate_csv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


