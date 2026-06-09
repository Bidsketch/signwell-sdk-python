# CompletedPdfResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | URL to download the completed document | 

## Example

```python
from signwell_sdk.models.completed_pdf_response import CompletedPdfResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedPdfResponse from a JSON string
completed_pdf_response_instance = CompletedPdfResponse.from_json(json)
# print the JSON string representation of the object
print(CompletedPdfResponse.to_json())

# convert the object into a dict
completed_pdf_response_dict = completed_pdf_response_instance.to_dict()
# create an instance of CompletedPdfResponse from a dict
completed_pdf_response_from_dict = CompletedPdfResponse.from_dict(completed_pdf_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


