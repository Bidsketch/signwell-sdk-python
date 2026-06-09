# TemplateCheckboxGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | A unique identifier for the checkbox group. | 
**placeholder_id** | **str** | The recipient ID associated with the checkbox group. | 
**checkbox_ids** | **List[str]** |  | 
**validation** | [**CheckboxValidation**](CheckboxValidation.md) |  | [optional] 
**required** | **bool** | Whether the group must be completed by the recipient. Defaults to false. | [optional] [default to False]
**min_value** | **int** | The minimum number of checkboxes that must be checked in the group. (Only for validation: minimum and range) | [optional] 
**max_value** | **int** | The maximum number of checkboxes that can be checked in the group. (Only for validation: maximum and range) | [optional] 
**exact_value** | **int** | The exact number of checkboxes that must be checked in the group. (Only for validation: exact) | [optional] 

## Example

```python
from signwell_sdk.models.template_checkbox_groups_inner import TemplateCheckboxGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateCheckboxGroupsInner from a JSON string
template_checkbox_groups_inner_instance = TemplateCheckboxGroupsInner.from_json(json)
# print the JSON string representation of the object
print(TemplateCheckboxGroupsInner.to_json())

# convert the object into a dict
template_checkbox_groups_inner_dict = template_checkbox_groups_inner_instance.to_dict()
# create an instance of TemplateCheckboxGroupsInner from a dict
template_checkbox_groups_inner_from_dict = TemplateCheckboxGroupsInner.from_dict(template_checkbox_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


