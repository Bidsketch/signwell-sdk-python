# LabelResponse

Labels can be used to organize documents and templates in a way that can make it easy to find using the document search/template search in SignWell. Labels can be used to organize documents in a way that can make it easy to find using the document search in SignWell.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from signwell_sdk.models.label_response import LabelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LabelResponse from a JSON string
label_response_instance = LabelResponse.from_json(json)
# print the JSON string representation of the object
print(LabelResponse.to_json())

# convert the object into a dict
label_response_dict = label_response_instance.to_dict()
# create an instance of LabelResponse from a dict
label_response_from_dict = LabelResponse.from_dict(label_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


