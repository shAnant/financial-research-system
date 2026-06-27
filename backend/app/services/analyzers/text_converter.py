import requests
import json

def json_to_text(data: dict) -> str:
    """
    Converts the financial summary JSON into a formatted text
    suitable for LLM prompts.

    Parameters
    ----------
    data : dict
        JSON returned by the /summary/{stock_name} endpoint.

    Returns
    -------
    str
        Readable financial context.
    """

    text = []

    # There is only one stock at the top level
    stock_name, stock_data = next(iter(data.items()))

    text.append(f"Company: {stock_name}")
    text.append("")

    if "title" in stock_data:
        text.append(stock_data["title"])
        text.append("")

    # Iterate through every financial category
    for category, metrics in stock_data.items():

        if category == "title":
            continue

        text.append(category)
        text.append("")

        for metric_name, observations in metrics.items():

            text.append(f"{metric_name}:")

            for observation in observations:
                text.append(f"  • {observation}")

            text.append("")

    return "\n".join(text)

# data = requests.get("http://127.0.0.1:8000/summary/RELIANCE.NS").json()
# # print(json.dumps(data,indent=4))
# print(json_to_text(data))