function IndicatorsCard({ data }) {

    if (!data || data.length === 0) return null;

    const latest = data[data.length - 1];

    const indicators = [

        {
            name: "SMA 5",
            value: latest.sma5
        },

        {
            name: "SMA 10",
            value: latest.sma10
        },

        {
            name: "RSI",
            value: latest.rsi
        },

        {
            name: "EMA 12",
            value: latest.ema12
        },

        {
            name: "EMA 26",
            value: latest.ema26
        },

        {
            name: "MACD",
            value: latest.macd
        },

        {
            name: "ATR 14",
            value: latest.atr14
        },

        {
            name: "Relative Volume",
            value: latest.relative_volume
        }

    ];

    return (

        <div className="bg-white rounded-xl shadow-lg p-6">

            <h2 className="text-xl font-bold mb-5">

                Technical Indicators

            </h2>

            <div className="space-y-4">

                {

                    indicators.map(indicator => (

                        <div

                            key={indicator.name}

                            className="flex justify-between border-b pb-2"

                        >

                            <span>

                                {indicator.name}

                            </span>

                            <span>

                                {

                                    indicator.value === null

                                    ?

                                    "-"

                                    :

                                    indicator.value

                                }

                            </span>

                        </div>

                    ))

                }

            </div>

        </div>

    );

}

export default IndicatorsCard;