function IndicatorsTable({ data }) {

    if (!data.length) return null;

    const latest = data[data.length - 1];

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold mb-5">

                Latest Technical Indicators

            </h2>

            <table className="w-full">

                <tbody>

                    <tr>

                        <td>RSI</td>

                        <td>{latest.rsi_14}</td>

                    </tr>

                    <tr>

                        <td>MACD</td>

                        <td>{latest.macd}</td>

                    </tr>

                    <tr>

                        <td>SMA20</td>

                        <td>{latest.sma_20}</td>

                    </tr>

                    <tr>

                        <td>EMA20</td>

                        <td>{latest.ema_20}</td>

                    </tr>

                </tbody>

            </table>

        </div>

    );

}

export default IndicatorsTable;