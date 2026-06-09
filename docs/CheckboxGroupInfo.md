# CheckboxGroupInfo

Checkbox group configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Checkbox group ID | 
**group_name** | **str** | Name of the checkbox group | [optional] 
**recipient_id** | **str** | Recipient ID associated with the group | [optional] 
**checkbox_ids** | **List[str]** | IDs of checkboxes in this group | 
**validation** | [**CheckboxValidation**](CheckboxValidation.md) |  | [optional] 
**required** | **bool** | Whether at least one checkbox must be checked | 
**min_value** | **int** | Minimum number of checkboxes to check | [optional] 
**max_value** | **int** | Maximum number of checkboxes to check | [optional] 
**exact_value** | **int** | Exact number of checkboxes that must be checked | [optional] 

## Example

```python
from signwell_sdk.models.checkbox_group_info import CheckboxGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CheckboxGroupInfo from a JSON string
checkbox_group_info_instance = CheckboxGroupInfo.from_json(json)
# print the JSON string representation of the object
print(CheckboxGroupInfo.to_json())

# convert the object into a dict
checkbox_group_info_dict = checkbox_group_info_instance.to_dict()
# create an instance of CheckboxGroupInfo from a dict
checkbox_group_info_from_dict = CheckboxGroupInfo.from_dict(checkbox_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


