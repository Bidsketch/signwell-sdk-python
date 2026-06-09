# LabelRequest

Labels can be used to organize documents and templates in a way that can make it easy to find using the document search/template search in SignWell. Labels can be used to organize documents in a way that can make it easy to find using the document search in SignWell.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from signwell_sdk.models.label_request import LabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelRequest from a JSON string
label_request_instance = LabelRequest.from_json(json)
# print the JSON string representation of the object
print(LabelRequest.to_json())

# convert the object into a dict
label_request_dict = label_request_instance.to_dict()
# create an instance of LabelRequest from a dict
label_request_from_dict = LabelRequest.from_dict(label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


