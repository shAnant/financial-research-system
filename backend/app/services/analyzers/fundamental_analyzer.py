import requests
from urllib.parse import quote
import json

growth = ["Basic EPS", "Total Revenue", "Net Income"]
margin = ["Gross Profit", "Operating Income", "Net Income"]
returns = ["Stockholders Equity", "Total Assets", "Invested Capital"]
leverage = ["Total Assets", "Stockholders Equity", "Cash And Cash Equivalents"]
cashflow = ["Free Cash Flow", "Operating Cash Flow"]

def growth_derive_data(data):
    metric = next(iter(data))
    revenue = data[metric]
    dates = sorted(revenue.keys())
    
    map = {
        "Basic EPS" : "EPS growth",
        "Total Revenue" : "Revenue Growth",
        "Net Income" : "Net Income Growth"
    }
    
    growth = {map[metric]:{}}
    for i in range(1, len(dates)):
        prev_date = dates[i-1]
        curr_date = dates[i]
        
        prev_val = revenue[prev_date]
        curr_val = revenue[curr_date]
        growth[map[metric]][curr_date] = round(((curr_val - prev_val)/prev_val)*100,2)
    return growth

def margins_derive_data(stock_name, data):
    response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Total%20Revenue")
    revenue_data = response.json()[0]
    revenue_data = revenue_data["metrics"]["Total Revenue"]
    metric = next(iter(data))
    income = data[metric]
    dates = sorted(income.keys())
    data = data[metric]
    
    map = {
        "Gross Profit" : "Gross Margin",
        "Operating Income" : "Operating Margin",
        "Net Income" : "Net Margin"
    }
    
    margin = {map[metric]:{}}
    
    for curr_date in dates:
        income_type = income[curr_date]  
        total_revenue = revenue_data[curr_date]
        
        margin[map[metric]][curr_date] = round((income_type/total_revenue)*100,2)
    return margin        
        
def returns_derived_data(stock_name,data):
    data = data[0]['metrics']
    metric = next(iter(data))
    
    result = {}
    
    if metric == "Stockholders Equity":
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Net%20Income")
        net_income = response.json()[0]
        net_income = net_income['metrics']['Net Income']
        equity = data[metric]
        # print(json.dumps(equity, indent=4))
        
        dates = sorted(net_income.keys())
        result["ROE"] = {}
        for curr_date in dates:
            income = net_income[curr_date]
            stock_holder_equity = equity[curr_date]
            result['ROE'][curr_date] = round((income/stock_holder_equity)*100,2)
    elif metric == "Total Assets":
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Net%20Income")
        net_income = response.json()[0]
        net_income = net_income['metrics']['Net Income']
        equity = data[metric]
        # print(json.dumps(equity, indent=4))
        
        dates = sorted(net_income.keys())
        result["ROA"] = {}
        for curr_date in dates:
            income = net_income[curr_date]
            stock_holder_equity = equity[curr_date]
            result['ROA'][curr_date] = round((income/stock_holder_equity)*100,2)
    elif metric == "Invested Capital":
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Operating%20Income")
        op_income = response.json()[0]
        op_income = op_income['metrics']['Operating Income']
        equity = data[metric]
        # print(json.dumps(equity, indent=4))
        
        dates = sorted(op_income.keys())
        result["ROIC"] = {}
        for curr_date in dates:
            income = op_income[curr_date]
            stock_holder_equity = equity[curr_date]
            result['ROIC'][curr_date] = round((income/stock_holder_equity)*100,2)
            
    return result
        
def derive_curr_ratio(curr_asset, curr_lia):
    curr_asset = curr_asset["metrics"]["Current Assets"]
    curr_lia = curr_lia["metrics"]["Current Liabilities"]
    dates = sorted(curr_asset.keys())
    result = {}
    result["current ratio"] = {}
    for date in dates:
        current_asset = curr_asset[date]
        current_liabilities = curr_lia[date]
        result["current ratio"][date] = round(current_asset/current_liabilities,2)
    return result

def derive_cash_ratio(cash_eqi, curr_lia):
    cash_eqi = cash_eqi['metrics']['Cash And Cash Equivalents']
    curr_lia = curr_lia["metrics"]["Current Liabilities"]
    dates = sorted(cash_eqi.keys())
    
    result = {}
    result["cash ratio"] = {}
    for date in dates:
        cash_and_cash_equi  = cash_eqi[date]
        current_lia = curr_lia[date]
        result["cash ratio"][date] = round(cash_and_cash_equi/current_lia,2)
    return result
    
def leverage_derived_data(stock_name, data):
    map = {
        "Total Assets" : "Dept_to_Equity",
        "Stockholders Equity" : "Dept_to_assets"
    }
    response_total_dept = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Total%20Debt")
    total_dept_data = response_total_dept.json()[0]
    total_dept_data = total_dept_data['metrics']['Total Debt']
    data = data[0]['metrics']
    metric = next(iter(data))
    data = data[metric]
    # print(metric)
    result = {}
    result[map[metric]] = {}
    dates = sorted(total_dept_data.keys())
    for date in dates:
        total_dept = total_dept_data[date]
        factor = data[date]
        result[map[metric]][date] = total_dept/factor
    return result
    
def net_dept(stock_name, data):
    response_total_dept = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Total%20Debt")
    total_dept_data = response_total_dept.json()[0]
    total_dept_data = total_dept_data['metrics']['Total Debt']
    data = data[0]['metrics']
    metric = next(iter(data))
    data = data[metric]
    # print(metric)
    result = {}
    result["Net Dept"] = {}
    dates = sorted(total_dept_data.keys())
    for date in dates:
        total_dept = total_dept_data[date]
        factor = data[date]
        result["Net Dept"][date] = total_dept-factor
    return result
        
def derived_margin(stock_name, data):
    map = {
        "Free Cash Flow" : "fcf_margin",
        "Operating Cash Flow" : "ocf_margin"
    }
    data = data[0]['metrics']
    metric = next(iter(data))
    data = data[metric]
    result = {}
    result[map[metric]] = {}
    response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Total%20Revenue")
    total_rev = response.json()

    total_rev = total_rev[0]['metrics']['Total Revenue']
    dates = sorted(total_rev.keys())
    for date in dates:
        cash_flow = data[date]
        total_revenue = total_rev[date]
        result[map[metric]][date] = round((cash_flow/total_revenue)*100,2)
    return result

def calculate_cash_conversion(stock_name):
    cashflow = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Operating%20Cash%20Flow").json()[0]['metrics']['Operating Cash Flow']
    income = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Net%20Income").json()[0]['metrics']['Net Income']
    dates = sorted(cashflow.keys())
    result = {}
    result['Cash Conversions'] = {}
    for date in dates:
        operating_cash_flow = cashflow[date]
        net_income = income[date]
        result['Cash Conversions'][date] = operating_cash_flow/net_income
    return result

def derives_metrics(stock_name):
    result = {"stock_name":stock_name, "metrics":{}}
    
    result["metrics"]["growth"] = {}
    for factor in growth:
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/{quote(factor)}")
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))
            calculated_metrics = growth_derive_data(data[0]['metrics'])
            result['metrics']['growth'].update(calculated_metrics)
        else:
            print("error :",response.status_code)
            
    result["metrics"]["margin"] = {}
    for factor in margin:
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/{quote(factor)}")
        if response.status_code == 200:
            data = response.json()
            calculated_metrics = margins_derive_data(stock_name,data[0]['metrics'])
            result['metrics']['margin'].update(calculated_metrics)
        else:
            print(f"Error code : {response.status_code}")
            
    result["metrics"]["returns"] = {}
    for factor in returns:
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/{quote(factor)}")
        if response.status_code == 200:
            data = response.json()
            calculated_metrics = returns_derived_data(stock_name, data)
            result['metrics']['returns'].update(calculated_metrics)
        else:
            print(f"error code : {response.status_code}")
    
    result["metrics"]["liquidity"] = {}
    response_curr_asset = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Current%20Assets")
    response_curr_lia = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Current%20Liabilities")
    current_ratio = derive_curr_ratio(response_curr_asset.json()[0], response_curr_lia.json()[0])
    result["metrics"]["liquidity"].update(current_ratio)
    
    response_cash_eqi = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/Cash%20And%20Cash%20Equivalents")
    cash_ratio = derive_cash_ratio(response_cash_eqi.json()[0], response_curr_lia.json()[0])
    result['metrics']['liquidity'].update(cash_ratio)
    
    result["metrics"]["leverage"] = {}
    for factor in leverage:
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/{quote(factor)}")
        if response.status_code == 200:
            data = response.json()
            if factor == "Cash And Cash Equivalents":
                calculated_metrics = net_dept(stock_name, data)
            else:
                calculated_metrics = leverage_derived_data(stock_name, data)
            result["metrics"]["leverage"].update(calculated_metrics)
        else:
            print(f"Error code : {response.status_code}")
    
    result["metrics"]["Cash Flow Quality"] = {}
    for factor in cashflow:
        response = requests.get(f"http://127.0.0.1:8000/stocks/{stock_name}/{quote(factor)}")
        if response.status_code == 200:
            data = response.json()
            calculated_metrics = derived_margin(stock_name, data)
            result['metrics']['Cash Flow Quality'].update(calculated_metrics)
        else:
            print(f"Error code : {response.status_code}")
            
    result['metrics']['Cash Flow Quality'].update(calculate_cash_conversion(stock_name))
        
    
    return result

# derived_metrics = derives_metrics("RELIANCE.NS")



# print(json.dumps(derived_metrics, indent=4)) 