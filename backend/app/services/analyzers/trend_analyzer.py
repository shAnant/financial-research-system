def analyze_trend(values):
    """
    values = {
        "2024-03-31":102.9,
        "2025-03-31":-2.42,
        "2026-03-31":19.09
    }
    """

    years = sorted(values.keys())
    nums = [values[y] for y in years]

    observations = []

    for i in range(1, len(nums)):

        prev = nums[i - 1]
        curr = nums[i]

        if curr > prev:
            observations.append(
                f"In {years[i]}, the metric increased from {prev:.2f} to {curr:.2f}."
            )

        elif curr < prev:
            observations.append(
                f"In {years[i]}, the metric declined from {prev:.2f} to {curr:.2f}."
            )

        else:
            observations.append(
                f"In {years[i]}, the metric remained unchanged at {curr:.2f}."
            )

    return observations