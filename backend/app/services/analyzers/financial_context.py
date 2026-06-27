from services.analyzers.category_context_generator import category_to_context
import json

def generate_financial_context(financial_data):

    context = {}

    context.update({"title":"The following financial information summarizes the company's historical performance."})

    for category, metrics in financial_data.items():

        context.update(
            category_to_context(category, metrics)
        )

        # context.append("\n")

    # return "\n".join(context)
    return context
