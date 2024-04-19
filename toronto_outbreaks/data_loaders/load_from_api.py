import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """Template for loading data from multiple APIs"""
    dfs = []
    # for year in range(2016, 2025):
    #     url = f'https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/3c7b2e27-b269-4277-b244-43d49bd290e0/download/ob_report_{year}.csv'
    #     response = requests.get(url)
    #     df = pd.read_csv(io.StringIO(response.text), sep=',')
    #     print(url)
    #     print(df.head())
    #     dfs.append(df)
    urls = ['https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/3c7b2e27-b269-4277-b244-43d49bd290e0/download/ob_report_2024.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/663292d2-3690-4007-96c3-a4a0d308dec3/download/ob_report_2023.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/be1d2d2d-579b-4abb-931c-5a233ecdff49/download/ob_report_2022.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/6b805d0c-9c8d-486e-914f-d789edd4e59a/download/ob_report_2021.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/8a3d830f-7783-4b9b-9011-3d78b9125194/download/ob_report_2020.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/e810c8ab-3bea-469f-97ae-c8d238938b21/download/ob_report_2019.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/aefb2244-b9f1-417a-b4a9-dd197d89c5b2/download/ob_report_2018.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/651987a6-0d9b-460c-bdb1-ae84bf4f382f/download/ob_report_2017.csv','https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/80ce0bd7-adb2-4568-b9d7-712f6ba38e4e/resource/04e2a0e8-364e-4853-be7c-108771616800/download/ob_report_2016.csv']
    for url in urls:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text), sep=',')
        print(url)
        print(df.head())
        dfs.append(df)
    final_df = pd.concat(dfs, ignore_index=True)
    print(final_df.tail())
    return final_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
