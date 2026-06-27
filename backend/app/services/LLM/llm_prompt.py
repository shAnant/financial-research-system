from services.analyzers.get_summary import get_stock_summary
from services.analyzers.text_converter import json_to_text
import requests

def get_prompt(stock_name):
    summary_json = get_stock_summary(stock_name)

    context = json_to_text(summary_json)

    prompt = f"""
    You are a senior equity research analyst.

    Analyze the following financial observations and produce a professional equity research report.

    Instructions:
    - Do not repeat every observation.
    - Focus on trends and overall financial performance.
    - Base your conclusions only on the provided information.
    - Use professional financial terminology.

    Return the response in the following JSON format:

    {{
        "executive_summary": "",
        "growth_analysis": "",
        "profitability_analysis": "",
        "liquidity_analysis": "",
        "cash_flow_analysis": "",
        "strengths": [],
        "weaknesses": [],
        "overall_financial_health": {{
            "rating": "",
            "reason": ""
        }}
    }}

    Financial Observations:

    {context}
    """
    return prompt