import { useEffect, useState } from "react";
import { getStocksList } from "../api/stockApi";

function StockSelector({ selectedStock, setSelectedStock }) {

    const [stocks, setStocks] = useState([]);

    useEffect(() => {

        const fetchStocks = async () => {

            try {

                const data = await getStocksList();

                setStocks(data);

            } catch (error) {

                console.log(error);

            }

        };

        fetchStocks();

    }, []);

    return (

        <div className="flex flex-col gap-2">

            <label className="font-semibold">
                Select Stock
            </label>

            <select
                className="border rounded-lg p-2"
                value={selectedStock?.symbol || ""}
                onChange={(e) => {

                    const stock = stocks.find(
                        s => s.symbol === e.target.value
                    );

                    setSelectedStock(stock);

                }}
            >

                <option value="">
                    Select Stock
                </option>

                {

                    stocks.map(stock => (

                        <option
                            key={stock.id}
                            value={stock.symbol}
                        >

                            {stock.symbol}

                        </option>

                    ))

                }

            </select>

        </div>

    );

}

export default StockSelector;