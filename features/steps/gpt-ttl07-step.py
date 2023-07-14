# from behave import given, then
# from collections import defaultdict
#
# @given('a set of specific users')
# def step_given_a_set_of_specific_users(context):
#     context.user_department = defaultdict(list)
#     for row in context.table:
#         context.user_department[row['department']].append(row['name'])
#
# @then('we will have the following people in "{department}"')
# def step_then_we_will_have_the_following_people_in_department(context, department):
#     actual_people = set(context.user_department[department])
#     expected_people = {row['name'] for row in context.table}
#     assert actual_people == expected_people
#
# @then('we will have at least the following people in "{department}"')
# def step_then_we_will_have_at_least_the_following_people_in_department(context, department):
#     actual_people = set(context.user_department[department])
#     expected_people = {row['name'] for row in context.table}
#     assert expected_people.issubset(actual_people)
