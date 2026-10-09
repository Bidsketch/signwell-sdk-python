# ConditionalRuleInfo

Conditional rule configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Conditional rule ID | 
**target_id** | **str** | api_id of the field that owns the rule, or the external_id of a checkbox group when the rule is owned by a group (groups have no api_id) | 
**action_type** | **str** | Action applied to action_field_ids when the conditions are met | 
**action_field_ids** | **List[str]** | api_ids of fields the rule affects when triggered | [optional] 
**conditions** | [**List[ConditionalRuleInfoConditionsInner]**](ConditionalRuleInfoConditionsInner.md) |  | [optional] 

## Example

```python
from signwell_sdk.models.conditional_rule_info import ConditionalRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionalRuleInfo from a JSON string
conditional_rule_info_instance = ConditionalRuleInfo.from_json(json)
# print the JSON string representation of the object
print(ConditionalRuleInfo.to_json())

# convert the object into a dict
conditional_rule_info_dict = conditional_rule_info_instance.to_dict()
# create an instance of ConditionalRuleInfo from a dict
conditional_rule_info_from_dict = ConditionalRuleInfo.from_dict(conditional_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


