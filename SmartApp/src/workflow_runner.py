# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:30:44 2020

@author: Himanshu.Manjarawala
"""
from models import Company, Index
import pandas as pd

def get_snp_500_companies(url):
    companies = []
    table = pd.read_html(url)[0]
    for index, row in table.iterrows():
        company = Company(row['Symbol'])
        company.name = row['Security']
        company.sector = row['GICS Sector']
        company.industry = row['GICS Sub Industry']
        company.date_added = row['Date first added']
        companies.append(company)
    return companies

def get_ftse_companies(url):
    companies = []
    table = pd.read_html(url)[3]
    for index, row in table.iterrows():
        company = Company(row['EPIC'])
        company.name = row['Company']
        company.sector = row['FTSE Industry Classification Benchmark sector[12]']
        companies.append(company)
    return companies

async def run(config):
    companies_map = {
        Index.SNP500: get_snp_500_companies,
        Index.FTSE100: get_ftse_companies
        }
    
    url = config.get_url()
    
    func_to_get_data = companies_map.get(config.index, None)
    if func_to_get_data is None:
        raise KeyError(f'{input.index} is not suppported')

    companies = func_to_get_data(url)
    return [c.name for c in companies]