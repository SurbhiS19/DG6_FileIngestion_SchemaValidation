import logging
import os
import subprocess
import yaml
import pandas as pd
import datetime
import gc
import re


################
# File Reading #
################

def read_config_file(filepath):
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)


def replacer(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def col_header_val(df,table_config):
    '''
    replace whitespaces in the column
    and standardized column names
    '''

    raw_columns = list(map(lambda x: x.lower(),  df.columns))
    yml_columns = list(map(lambda x: x.lower(),  table_config['columns']))

    yml_columns = [x.strip(' ') for x in yml_columns]
    raw_columns = [x.strip(' ') for x in raw_columns]


    expected_col=yml_columns


    if len(raw_columns) == len(expected_col) and list(expected_col)  == list( raw_columns):
        print("column name and column length validation passed")
        return 1
    else:
        print("column name and column length validation failed")
        mismatched_columns_file = list(set(raw_columns).difference(expected_col))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_col).difference(raw_columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'df columns: {raw_columns}')
        logging.info(f'expected columns: {expected_col}')
        return 0
