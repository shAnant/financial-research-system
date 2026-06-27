import StatisticCard from "./StatisticCard";
import PriceChart from "./PriceChart";
import IndicatorsCard from "./IndicatorsCard";
import NewsSection from "./NewsSection";
import FundamentalsSection from "./FundamentalsSection";
import LLMSummarySection from "./LLMSummarySection";

function DashboardContent({

    priceData,

    news,

    fundamentals,

    llmSummary,

    loadingSummary,

    onGenerateSummary

}) {

    if (!priceData || priceData.length === 0) {

        return null;

    }

    const latest = priceData[priceData.length - 1];

    return (

        <div className="space-y-10 mt-10">

            {/* Statistics */}

            <div className="grid grid-cols-4 gap-4">

                <StatisticCard

                    title="Current Price"

                    value={latest._close_}

                    color="bg-blue-100"

                />

                <StatisticCard

                    title="Volume"

                    value={latest.volume.toLocaleString()}

                    color="bg-green-100"

                />

                <StatisticCard

                    title="Return %"

                    value={`${latest.percentage_change}%`}

                    color="bg-red-100"

                />

                <StatisticCard

                    title="Volatility"

                    value={`${latest.intraday_volatility}%`}

                    color="bg-yellow-100"

                />

            </div>

            {/* Chart */}

            <div className="grid grid-cols-4 gap-6">

                <div className="col-span-3">

                    <PriceChart

                        data={priceData}

                    />

                </div>

                <IndicatorsCard

                    data={priceData}

                />

            </div>

            {/* News + Fundamentals */}

            <div className="grid grid-cols-2 gap-6">

                <NewsSection

                    news={news}

                />

                <FundamentalsSection

                    fundamentals={fundamentals}

                />

            </div>

            {/* AI Summary */}

            <LLMSummarySection

                summary={llmSummary}

                loading={loadingSummary}

                onGenerate={onGenerateSummary}

            />

        </div>

    );

}

export default DashboardContent;