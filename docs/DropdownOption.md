# DropdownOption

A dropdown option - either a simple string or a detailed object with name and optional api_id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Option display name | 
**api_id** | **str** | Unique identifier for the option | [optional] 
**is_other** | **bool** | Whether this is the special \&quot;Other\&quot; option | [optional] [default to False]

## Example

```python
from signwell_sdk.models.dropdown_option import DropdownOption

# TODO update the JSON string below
json = "{}"
# create an instance of DropdownOption from a JSON string
dropdown_option_instance = DropdownOption.from_json(json)
# print the JSON string representation of the object
print(DropdownOption.to_json())

# convert the object into a dict
dropdown_option_dict = dropdown_option_instance.to_dict()
# create an instance of DropdownOption from a dict
dropdown_option_from_dict = DropdownOption.from_dict(dropdown_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


