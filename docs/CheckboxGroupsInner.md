# CheckboxGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | A unique identifier for the checkbox group. | 
**recipient_id** | **str** | The recipient ID associated with the checkbox group. | 
**checkbox_ids** | **List[str]** |  | 
**validation** | [**CheckboxValidation**](CheckboxValidation.md) |  | [optional] 
**required** | **bool** | Whether the group must be completed by the recipient. Defaults to false. | [optional] [default to False]
**min_value** | **int** | The minimum number of checkboxes that must be checked in the group. (Only for validation: minimum and range) | [optional] 
**max_value** | **int** | The maximum number of checkboxes that can be checked in the group. (Only for validation: maximum and range) | [optional] 
**exact_value** | **int** | The exact number of checkboxes that must be checked in the group. (Only for validation: exact) | [optional] 

## Example

```python
from signwell_sdk.models.checkbox_groups_inner import CheckboxGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CheckboxGroupsInner from a JSON string
checkbox_groups_inner_instance = CheckboxGroupsInner.from_json(json)
# print the JSON string representation of the object
print(CheckboxGroupsInner.to_json())

# convert the object into a dict
checkbox_groups_inner_dict = checkbox_groups_inner_instance.to_dict()
# create an instance of CheckboxGroupsInner from a dict
checkbox_groups_inner_from_dict = CheckboxGroupsInner.from_dict(checkbox_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


