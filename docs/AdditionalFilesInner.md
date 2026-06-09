# AdditionalFilesInner

Additional files to be appended to the document. Will not replace existing files from the template. Document files can be uploaded by specifying a file URL or base64 string. Either `file_url` or `file_base64` must be present (not both). Valid file types are: .pdf, .docx, .jpg, .png, .ppt, .xls, .pages, and .txt.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file that will be uploaded. | 
**file_url** | **str** | Publicly available URL of the file to be uploaded. | [optional] 
**file_base64** | **bytearray** | A RFC 4648 base64 string of the file to be uploaded. | [optional] 

## Example

```python
from signwell_sdk.models.additional_files_inner import AdditionalFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalFilesInner from a JSON string
additional_files_inner_instance = AdditionalFilesInner.from_json(json)
# print the JSON string representation of the object
print(AdditionalFilesInner.to_json())

# convert the object into a dict
additional_files_inner_dict = additional_files_inner_instance.to_dict()
# create an instance of AdditionalFilesInner from a dict
additional_files_inner_from_dict = AdditionalFilesInner.from_dict(additional_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


