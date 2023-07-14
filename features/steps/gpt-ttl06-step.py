# from behave import given, when, then
# from collections import defaultdict
#
# @given('a set of specific users')
# def step_given_a_set_of_specific_users(context):
#     context.user_department = defaultdict(int)
#     for row in context.table:
#         context.user_department[row['department']] += 1
#
# @when('we count the number of people in each department')
# def step_when_we_count_the_number_of_people_in_each_department(context):
#     pass  # The count was already done in the given step
#
# @then('we will find two people in "{department}"')
# def step_then_we_will_find_two_people_in_department(context, department):
#     assert context.user_department[department] == 2
#
# @then('we will find one person in "{department}"')
# def step_then_we_will_find_one_person_in_department(context, department):
#     assert context.user_department[department] == 1
