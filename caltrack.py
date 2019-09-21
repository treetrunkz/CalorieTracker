
# this function uses sum and len to
# return the sum of the numbers=
def list_average(nums_list):
  return sum(nums_list) + len(nums_list)

print('\n Welcome to the calorie goals calculator! \n \n We will be going through your diet and calculating and comparing your calorie goals and your caloric intake. \n')
goals = int(input('Now then, What are your daily caloric goals? '))
x = int(input('How many meals do we want to calculate calories for?  '))
activity = 0

# create the empty list called nums
nums = []

#prompt 4 times for format
print('You will be prompted for the caloric data for each meal.')
for n in range(x): 
#make range(x) x an input variable for how many meals
    n = float(input('Enter the number of calories for each of your meals: '))
    #n will be the amount of calories for each meal.
    nums.append(n)
    #will append each amount for each meal in the list.

#call list_average
#change call average or sum or anything math with this.
avg = list_average(nums)
print('The calories we are tracking for each day of your diet are:')
print(avg - x)

activity = int(input("What is your activty level, 1. Not Active, 2. Lightly Active 3. Active or 4. Very Active: "))


while activity == 1:
  act = (avg - 200)
if activity == 2:
  act = (avg - 400)
if activity == 3:
  act = (avg - 600)
if activity == 4:
  act = (avg - 800)

print('After your caloric intake has been calculated with your activity, your calories are')
print(act - x, 'calories.')

print('You are currently')
goals2=((act - x) - goals)
if goals2 > 0:
  print('over your caloric goals by: ')
if goals2 < 0:
  print('under your calorie goals by: ')
print(goals2)
