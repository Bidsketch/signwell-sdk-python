# LabelInfo

Label information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Label ID | [optional] 
**name** | **str** | Label name | [optional] 

## Example

```python
from signwell_sdk.models.label_info import LabelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LabelInfo from a JSON string
label_info_instance = LabelInfo.from_json(json)
# print the JSON string representation of the object
print(LabelInfo.to_json())

# convert the object into a dict
label_info_dict = label_info_instance.to_dict()
# create an instance of LabelInfo from a dict
label_info_from_dict = LabelInfo.from_dict(label_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


