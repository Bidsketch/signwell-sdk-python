# DetailedOption

Detailed option object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Option display name | 
**api_id** | **str** | Unique identifier for the option | [optional] 
**is_other** | **bool** | Whether this is the special \&quot;Other\&quot; option | [optional] [default to False]

## Example

```python
from signwell_sdk.models.detailed_option import DetailedOption

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedOption from a JSON string
detailed_option_instance = DetailedOption.from_json(json)
# print the JSON string representation of the object
print(DetailedOption.to_json())

# convert the object into a dict
detailed_option_dict = detailed_option_instance.to_dict()
# create an instance of DetailedOption from a dict
detailed_option_from_dict = DetailedOption.from_dict(detailed_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


