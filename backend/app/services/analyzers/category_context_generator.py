from services.analyzers.trend_analyzer import analyze_trend
import json

def category_to_context(category_name, metrics):

    context = {}

    # context.append(f"{category_name.upper()} ANALYSIS\n")

    analysis = f"{category_name.upper()} ANALYSIS"
    context.update({analysis:{}})

    for metric_name, values in metrics.items():
        # print(f"{metric_name} {values} \n")
    #     context.append(f"{metric_name}:")

        trend = analyze_trend(values)
        context[analysis].update({metric_name: trend})
    #     for line in trend:
    #         context.append(f"- {line}")

    #     context.append("")
    return context

    # return "\n".join(context)