import os

import pandas as pd
import requests

DATA_DIR = "../Data"
A_FNAME = 'A_office_data.xml'
B_FNAME = 'B_office_data.xml'
HR_FNAME = 'hr_data.xml'
SEP = '\n' + '=' * 80 + '\n'
pd.set_option('display.max_columns', 20)


def download_datasets():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    # Download data if it is unavailable.
    if (A_FNAME not in os.listdir(DATA_DIR) or
            B_FNAME not in os.listdir(DATA_DIR) or
            HR_FNAME not in os.listdir(DATA_DIR)):
        print('A_office_data loading.')
        url = f"https://www.dropbox.com/s/jpeknyzx57c4jb2/{A_FNAME}?dl=1"
        r = requests.get(url, allow_redirects=True)
        open(f"{DATA_DIR}/{A_FNAME}", 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = f"https://www.dropbox.com/s/hea0tbhir64u9t5/{B_FNAME}?dl=1"
        r = requests.get(url, allow_redirects=True)
        open(f"{DATA_DIR}/{B_FNAME}", 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = f"https://www.dropbox.com/s/u6jzqqg1byajy0s/{HR_FNAME}?dl=1"
        r = requests.get(url, allow_redirects=True)
        open(f"{DATA_DIR}/{HR_FNAME}", 'wb').write(r.content)
        print('Loaded.')

        # All data is now loaded to the Data folder.


def read_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """read all 3 datasets provided for this task from the xml files
    with directory and file names stored in global variables

    :returns - tuple with 3 pandas dataframes: A_office, B_office, HR_data
    """
    return pd.read_xml(f"{DATA_DIR}/{A_FNAME}"), \
        pd.read_xml(f"{DATA_DIR}/{B_FNAME}"), \
        pd.read_xml(f"{DATA_DIR}/{HR_FNAME}")


def examine_dataframes(*args) -> None:
    """prints basic information about the dataframe(s) provided

    :param - dataframe(s) to examine
    :returns - None
    """
    for df in args:
        print(SEP)
        print(f"SHAPE: {df.shape}, INFO:")
        print(df.info())
        print('---\nHEAD:')
        print(df.head())
        print('---\nTAIL:')
        print(df.tail())
    pass


if __name__ == '__main__':
    # original code put into the function - just in case of deleting some localy stored data
    download_datasets()

    # STAGE 1
    """Goals:
        reading dataframes from xml files
        working with df indices - changing them using values from the df itself 
        and some additional data (prefixes 'A'/'B' here)
    """

    # objective 1 - read data
    a_office, b_office, hr = read_data()

    # objective 2 - examine data

    # objective #3 - set indices
    a_office.index = a_office.employee_office_id.apply(lambda x: 'A' + str(x))
    b_office.index = b_office.apply(lambda row: 'B' + str(row.employee_office_id), axis=1)
    hr.set_index(keys='employee_id', drop=False, inplace=True, verify_integrity=True)

    # just 'hr.index = ...' is not enough here because
    # it doesn't assign the 'name' to the index as 'set_index' does...
    # hr.index = hr.employee_id.values

    # objective #4 - print results as lists of indices
    # print(a_office.index.tolist())
    # print(b_office.index.tolist())
    # print(hr.index.tolist())

    # STAGE 2

    """Goals:
        joining two df with identical structure with the aim of 'concat'
        joining the df with different structure, but indices values present in both df 
        handling the final df with joined data
    """

    # objectives #1, #2, #3 - done at Stage #1
    # objective #4 - concat A, B
    a_b = pd.concat([a_office, b_office])

    # objective #5
    """Use df.merge() to carry out the left merging of the unified office dataset with HR's dataset. 
        Merge both datasets by index — use left_index and right_index parameters. 
        Set indicator=True in df.merge(). 
        For the final table, leave only those employees whose data is contained in both datasets;
    """
    # merge according to the requirements given
    a_b_hr = a_b.merge(hr, how='left', left_index=True, right_index=True, indicator=True)

    # keep only data taken from both original dataframes
    a_b_hr.drop(a_b_hr[a_b_hr._merge != 'both'].index, inplace=True)

    # objective #6
    a_b_hr.drop(columns=['employee_office_id', 'employee_id', '_merge'], inplace=True)

    # objective #7
    a_b_hr.sort_index(inplace=True)

    # objective #8
    # print(new_df.index.to_list())
    # print(new_df.columns.to_list())

    # STAGE 3

    """Goals:
        conditional selection of rows and/or columns from a dataframe
        aggregating selected data
        converting the df got into list(s)
    """

    # objectives #1 - #7 - done before
    # objective #8 - actuall Stage #3 goals

    # objective #8.1
    avg_hour_and_dept = a_b_hr[['average_monthly_hours', 'Department']]
    avg_hour_and_dept = avg_hour_and_dept.sort_values('average_monthly_hours', ascending=False)
    # examine_dataframes(avg_hour_and_dept)
    # print(avg_hour_and_dept[0:10]['Department'].tolist())

    # objective #8.2
    it_emp_low_sal = a_b_hr[(a_b_hr.Department == 'IT') & (a_b_hr.salary == 'low')]
    # print(it_emp_low_sal.number_project.sum())

    # objective #8.3
    # What are the last evaluation scores and the satisfaction levels of the employees A4, B7064, and A3033?
    # print([list(row) for row in ABHR.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']].values])

    # STAGE 4

    """Goals:
        grouping data and aggregating them with builtin and custom functions
    """


    # objectives #1 - #7 - done before

    # objectives #8 - #10 - actual Stage #3 goals
    def count_bigger_5(x):
        return sum(x > 5)


    # 'left' - column originated from the initial 'hr_data' dataframe
    #    = 1.0 if the employee left the company
    #    = 0.0 if the employee still works in the company
    # the ABHR df has 5982 entries in total, where:
    #   'left' == 0.0   - 4570 entries
    #   'left' == 1.0   - 1412 entries

    # print(a_b_hr.groupby('left').agg({'number_project':['median', ('count_bigger_5', lambda x: count_bigger_5(x))],
    #          'time_spend_company': ['mean', 'median'], 'Work_accident': ['mean'],
    #              'last_evaluation': ['mean', 'std']}).round(2))

    # OR

    aggregations_to_satisfy_the_boss = {
        'number_project': ['median', count_bigger_5],  # num of proj an employee has worked on
        'time_spend_company': ['mean', 'median'],  # how many years worked in the company
        'Work_accident': 'mean',  # wheather has had an injury at work
        'last_evaluation': ['mean', 'std']  # last evaluation score
    }
    # print(ABHR.groupby('left').agg(aggregations_to_satisfy_the_boss).round(2).to_dict())

    # STAGE 5

    """Goals:
        grouping and transforming data with the 'pivot_table' function,
        filtering data from the pivot tables
        converting pivot tables to dictionaries
    """

    # objectives #1 - #7 - done before
    # objectives #8 - #11 - actual Stage #5 goals

    # objective #8 - from the 'objectives':
    #   1st pivot table: Department as index, left and salary as columns,
    #   average_monthly_hours as values. Output median values in the table.

    # ovjective #8 - from the description section:
    """
        The first pivot table displays departments as rows, 
        employees' current status (the 'left' column), and their salary level as columns. 
        The values should be the median number of monthly hours employees have worked.
        (these is done above - see the 'pivot1' df)

        BUT:
        In the table, the HR boss wants to see only those departments where either one is true:

        For the currently employed (the 'left' == 0.0): 
        the median value of the working hours of high-salary employees 
        is smaller than the hours of the medium-salary employees, 

        OR:

        For the employees who left (the 'left' == 1.0): 
        the median value of working hours of low-salary employees 
        is smaller than the hours of high-salary employees
    """
    a_b_hr_to_pivot = a_b_hr.copy(deep=True)

    pivoted_1_1 = a_b_hr_to_pivot.pivot_table(values='average_monthly_hours',
                                              index='Department', columns=['left', 'salary'], aggfunc='median')
    pivoted_1_2 = pivoted_1_1.loc[(pivoted_1_1[(0.0, 'high')] < pivoted_1_1[(0.0, 'medium')])
                                  & (pivoted_1_1[(1.0, 'low')] < pivoted_1_1[(1.0, 'high')])]

    # objective #9 - from the 'objectives' section:
    """
        second pivot table:
        time_spend_company as index, promotion_last_5years as column,
        satisfaction_level and last_evaluation as values.
        Output the min, max, and mean values in the table.
    """
    pivoted_2_1 = pd.pivot_table(a_b_hr, values=['last_evaluation', 'satisfaction_level'],
                                 index='time_spend_company', columns=['promotion_last_5years'],
                                 aggfunc=['min', 'max', 'mean'])

    # ovjective #9 - from the description section:
    """
        The second pivot table is where each row is an employee's time in the company; 
        the columns indicate whether an employee has had any promotion. 
        The values are the last evaluation score's minimum, maximum, mean, and satisfaction level. 
        Filter the table by the following rule: 
        select only those rows where the previous mean evaluation score 
        is higher for those without promotion than those who had.
    """
    # objective #10 applied to objective #9:
    pivoted_2_2 = pivoted_2_1.loc[
        pivoted_2_1[('mean', 'last_evaluation', 0)] > pivoted_2_1[('mean', 'last_evaluation', 1)]]

    # objective #11:
    # print(pivoted_1_1.to_dict())
    # print(pivoted_2_2.to_dict())
