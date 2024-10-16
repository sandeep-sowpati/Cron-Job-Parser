"""
This Program handles the Cron Expression Parser and prints the output in the specified format.

Cron Input Format : "Minute Hour DayOfTheMonth Month DayOftheWeek Task

Specified Components of the Input Data and there expression

Month         : What Month to Execute the Cron Job

DayOfTheMonth : On What Day/Days to Execute the Job

DayOfTheWeek  : Based on the DaysOfTheMonth , we will check whether the dates following on this condition or not then only the job will run.

Hour          : At What Hour/Hours During the Specified Day.

Minute        : During the specified Hours, at what time the Job will execute .

Task          : The Task to execute at the specified time


Special Characters:

*    ---> Any Value 

,    ---> Comma Seperated List

-    ---> interval or Range Between Data

/    ---> Step Values 

Example : 

*/15(Minutes) 0(Hours) 1,15(DaysOfMonth) *(Month) 1-5(DaysOfWeek) /usr/bin/find(Task)

Minutes has step value so we want to Execute it every 15 Minutes in the Given Hour

Hours has single Integer so we will start the Job at 12AM 

DaysOfMonth has 1,15 so we execute it on the 1st and 15th of every Month.

Month has * so we execute it on every Month

DaysOfWeek has has 1-5 so if the DaysOfMonth falls in this days , the job will be triggered,

/usr/bin/find is the task that will trigger.

"""

#All Imports go here

import sys



#All Constants Go here

DATA_FIELDS = ['minutes','hours','days_of_the_month','months','days_of_the_week','task']
PRINTING_FIELDS  = ['minute','hour','day of month','month','day of week','command']

#Data mapper to name the output fields to the specified field names, using it because in future if we want to change any outputformat its easier to print
FIELD_MAPPER = {data: print_field for data, print_field in zip(DATA_FIELDS, PRINTING_FIELDS)}

SPECIAL_CHARACTERS = {'*',',','-','/'}

FIELD_VALUES = []

MINUTES_IN_HOUR = 60
HOURS_IN_DAY=24
DAYS_IN_WEEK = 7
DAYS_IN_MONTH = 31
MONTHS_IN_YEAR = 12


def validate_the_data(non_validate_data:list, start:int, end:int)->list:
    """
    Function to Validate the data , takes the data validates it against the given ranges and return data if validatton is completed
    otherwise throws ValueError
    """
    if all(start <= num <= end for num in non_validate_data):
        return non_validate_data  # Data is valid
    else:
        raise ValueError("Given Inputs are wrong as they have crossed the default")


def parse_special_expression(speacial_expression:str,starting_range:int,ending_range:int)-> list:
    """
    A parser method that deals with Speacial Character such as , * - / 
    and provide the data in integer format 
    """
    parsed_data_list = []

    if '/' in speacial_expression:
        first,second = speacial_expression.split('/')
        if first == '*':
            parsed_data_list = [i for i in range(starting_range,ending_range+1,int(second))]
        
        else:
            raise ValueError("Invalid Format")

    elif ',' in speacial_expression:
        parsed_data_list = list(map(int,speacial_expression.split(',')))
        validate_the_data(parsed_data_list,starting_range,ending_range)

    elif '*' in speacial_expression:
        parsed_data_list = [i for i in range(starting_range,ending_range+1)]

    elif '-' in speacial_expression:
        start,end = list(map(int,speacial_expression.split('-')))
        parsed_data_list = [i for i in range(start,end+1)]
        validate_the_data(parsed_data_list,starting_range,ending_range)

    return parsed_data_list

def parse_full_expression(data_expression:str,start:int,end:int)->list:
    """
    takes the Expression checks if it falls under SPECIAL Category or not
    and based on that it will parse the data
    """
    parsed_data = []
    if any(char in SPECIAL_CHARACTERS for char in data_expression):
        parsed_data = parse_special_expression(data_expression,start,end)
    else:
        parsed_data.append(int(data_expression))
    
    return parsed_data

# def parse_non_zero_data(parsed_data:list, ending_value):

#     if 0 in parsed_data:
#         parsed_data.remove(0)
#         parsed_data.append(ending_value)
#     return parsed_data

def parse_minutes(minutes_expression:str)->list:
    """
    Takes the Minutes expression after spliting and use the above methods to parse the expression and validate the data
    """
    parsed_minutes =  parse_full_expression(minutes_expression,0,MINUTES_IN_HOUR-1)
    validated_data = validate_the_data(parsed_minutes,0,MINUTES_IN_HOUR-1)
    return validated_data

def parse_hours(hours_expression:str)->list:
    """
    Takes the Hours expression after spliting and use the above methods to parse the expression and validate the data
    """
    parsed_hours =  parse_full_expression(hours_expression,0,HOURS_IN_DAY-1)
    validated_data = validate_the_data(parsed_hours,0,HOURS_IN_DAY-1)
    return validated_data

def parse_days_of_the_month(days_of_the_month_expression:str)->list:
    """
    Takes the Days of the Months expression after spliting and use the above methods to parse the expression and validate the data
    """
    parsed_days_of_the_month = parse_full_expression(days_of_the_month_expression,1,DAYS_IN_MONTH)
    # parsed_days_of_the_month =  parse_non_zero_data(parsed_days_of_the_month,DAYS_IN_MONTH)
    validated_data = validate_the_data(parsed_days_of_the_month,1,DAYS_IN_MONTH)
    return validated_data


def parse_months(months_expression:str)->list:
    """
    Takes the Months expression after spliting and use the above methods to parse the expression and validate the data
    """
    parsed_months = parse_full_expression(months_expression,1,MONTHS_IN_YEAR)
    # parsed_months =  parse_non_zero_data(parsed_months,MONTHS_IN_YEAR)
    validated_data = validate_the_data(parsed_months,1,MONTHS_IN_YEAR)
    return validated_data

def parse_days_of_the_week(days_of_the_week_expression:str)->list:
    """
    Takes the Parse Days of the Week expression after spliting and use the above methods to parse the expression and validate the data
    """
    parsed_days_of_week = parse_full_expression(days_of_the_week_expression,1,DAYS_IN_WEEK)
    # parsed_days_of_week =  parse_non_zero_data(parsed_days_of_week,DAYS_IN_WEEK)
    validated_data = validate_the_data(parsed_days_of_week,1,DAYS_IN_WEEK)
    return validated_data

def parse_task(task_expression):
    """
    Takes the Command expression after spliting and use the above methods to parse the expression and validate the data
    """
    return [task_expression]


#Funcational mapper
function_name_mapper = {
    'minutes' : parse_minutes,
    'hours' : parse_hours,
    'days_of_the_month' : parse_days_of_the_month,
    'months': parse_months,
    'days_of_the_week': parse_days_of_the_week,
    'task' : parse_task
}


def parse_expression(cron_expression:str)->dict:
    """
    takes the Cron Expression as an input and call differnt parsers to follow the SRP of SOLID Design Principle,
    """
    parsed_data = {}
    print(cron_expression)
    FIELD_VALUES = cron_expression.split()
    for data_field,data_value in zip(DATA_FIELDS,FIELD_VALUES):
        # print(f"{data_field}  : {data_value}")
        function_name  = function_name_mapper.get(data_field)
        values = function_name(data_value)
        parsed_data[data_field] = values
    return parsed_data

def print_parsed_data(parsed_dict:dict[str:list]):
    """Takes the whole parsed data in Dictionary Format and Print Convert the code fileds name to specified printing fields and print the 
    key values in table format specified
    """
    for key,values in parsed_dict.items():
        updated_key = FIELD_MAPPER.get(key)
        len_of_key = len(updated_key)
        spaces_pending = 20-len_of_key
        values_str = ' '.join(map(str, values))
        print(f"{updated_key} {' '*spaces_pending} {values_str}")
    

def main(raw_string):

    """
    Inorder to Solve SRP , implemented this function
    first we parse the expression 
    and then we print the expression , so both are independent of each other
    """
    parsed_dict = parse_expression(raw_string)
    print_parsed_data(parsed_dict)

if __name__ == '__main__':
    cron_input = sys.argv[1]
    main(cron_input)