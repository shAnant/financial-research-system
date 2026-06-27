import { useState } from "react";

import StockSelector from "../components/StockSelector";
import DateSelector from "../components/DateSelector";

import DashboardContent from "../components/DashboardContent";

import { getStockPrice } from "../api/stockApi";
import { getNews } from "../api/newsApi";
import { getFundamentals } from "../api/fundamentalsApi";
import { getLLMSummary } from "../api/llmApi";

function ResearchDashboard() {

    const [selectedStock, setSelectedStock] = useState(null);

    const [startDate, setStartDate] = useState("");

    const [endDate, setEndDate] = useState("");

    const [priceData, setPriceData] = useState([]);

    const [news, setNews] = useState([]);

    const [fundamentals, setFundamentals] = useState(null);

    const [loading, setLoading] = useState(false);

    const [llmSummary, setLLMSummary] = useState(null);

    const [loadingSummary, setLoadingSummary] = useState(false);

    const handleAnalyze = async () => {

        if (!selectedStock) {

            alert("Please select a stock");

            return;

        }

        if (!startDate || !endDate) {

            alert("Please select dates");

            return;

        }

        const start = new Date(startDate);

        const end = new Date(endDate);

        const diff =

            (end - start) /

            (1000 * 60 * 60 * 24);

        if (diff > 300) {

            alert("Maximum date range is 300 days.");

            return;

        }

        try {

            setLoading(true);

            const [

                stockResponse,

                newsResponse,

                fundamentalResponse

            ] = await Promise.all([

                getStockPrice(

                    selectedStock.symbol,

                    startDate,

                    endDate

                ),

                getNews(

                    selectedStock.symbol

                ),

                getFundamentals(

                    selectedStock.symbol

                )

            ]);

            setPriceData(stockResponse);

            setNews(newsResponse);

            setFundamentals(fundamentalResponse);

        }

        catch(error){

            console.log(error);

        }

        finally{

            setLoading(false);

        }

    };

    const handleGenerateSummary = async () => {

        if (!selectedStock) {
            alert("Please select a stock.");
            return;
        }

        try {

            setLoadingSummary(true);

            const data = await getLLMSummary(
                selectedStock.symbol
            );

            setLLMSummary(data);

        }
        catch (error) {

            console.error(error);

        }
        finally {

            setLoadingSummary(false);

        }

    };

 return (

    <div className="p-8">

        <h1 className="text-3xl font-bold mb-8">
            Financial Research Dashboard
        </h1>

        <div className="grid grid-cols-3 gap-6">

            <StockSelector
                selectedStock={selectedStock}
                setSelectedStock={setSelectedStock}
            />

            <DateSelector
                startDate={startDate}
                endDate={endDate}
                setStartDate={setStartDate}
                setEndDate={setEndDate}
            />

        </div>

        <button
            onClick={handleAnalyze}
            className="mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg"
        >
            Analyze
        </button>

        {loading && (
            <h2 className="mt-6">
                Loading...
            </h2>
        )}

        {!loading && priceData.length > 0 && (
            <DashboardContent
                priceData={priceData}
                news={news}
                fundamentals={fundamentals}
                llmSummary={llmSummary}
                loadingSummary={loadingSummary}
                onGenerateSummary={handleGenerateSummary}
            />
        )}

    </div>

);
}
export default ResearchDashboard;