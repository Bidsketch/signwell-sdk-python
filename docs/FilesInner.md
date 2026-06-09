# FilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file that will be uploaded. | 
**file_url** | **str** | Publicly available URL of the file to be uploaded. | [optional] 
**file_base64** | **bytearray** | A RFC 4648 base64 string of the file to be uploaded. | [optional] 

## Example

```python
from signwell_sdk.models.files_inner import FilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilesInner from a JSON string
files_inner_instance = FilesInner.from_json(json)
# print the JSON string representation of the object
print(FilesInner.to_json())

# convert the object into a dict
files_inner_dict = files_inner_instance.to_dict()
# create an instance of FilesInner from a dict
files_inner_from_dict = FilesInner.from_dict(files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


