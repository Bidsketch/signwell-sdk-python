# ConditionalRuleInfoConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_type** | **str** | How field_api_ids combine within this condition | [optional] 
**status** | **str** | Field state that satisfies this condition | [optional] 
**join_operator** | **str** | How this condition joins with the next one in the rule | [optional] 
**field_api_ids** | **List[str]** | api_ids of fields evaluated by this condition | [optional] 
**position** | **int** | Order of this condition within the rule | [optional] 

## Example

```python
from signwell_sdk.models.conditional_rule_info_conditions_inner import ConditionalRuleInfoConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionalRuleInfoConditionsInner from a JSON string
conditional_rule_info_conditions_inner_instance = ConditionalRuleInfoConditionsInner.from_json(json)
# print the JSON string representation of the object
print(ConditionalRuleInfoConditionsInner.to_json())

# convert the object into a dict
conditional_rule_info_conditions_inner_dict = conditional_rule_info_conditions_inner_instance.to_dict()
# create an instance of ConditionalRuleInfoConditionsInner from a dict
conditional_rule_info_conditions_inner_from_dict = ConditionalRuleInfoConditionsInner.from_dict(conditional_rule_info_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


