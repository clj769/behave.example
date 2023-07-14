# from behave import given, when, then, register_type
#
# class Calculator:
#     def add(self, x, y):
#         return x + y
#
# def parse_number(text):
#     return int(text)
#
# register_type(number=parse_number)
#
# @given('I have a calculator')
# def step_given_i_have_a_calculator(context):
#     context.calculator = Calculator()
#
# @when('I add "{x:number}" and "{y:number}"')
# def step_when_i_add_x_and_y(context, x, y):
#     context.result = context.calculator.add(x, y)
#
# @then('the calculator returns "{sum:number}"')
# def step_then_the_calculator_returns_sum(context, sum):
#     assert context.result == sum, f'got: {context.result}, expected: {sum}'
