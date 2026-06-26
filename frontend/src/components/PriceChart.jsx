import { useEffect, useRef } from "react";
import {
    createChart,
    CandlestickSeries,
    LineSeries,
    HistogramSeries
} from "lightweight-charts";

function PriceChart({ data }) {

    const chartContainer = useRef(null);

    useEffect(() => {

        if (!data || data.length === 0) return;

        chartContainer.current.innerHTML = "";

        const chart = createChart(chartContainer.current, {

            width: chartContainer.current.clientWidth,

            height: 550,

            layout: {

                background: {

                    color: "#ffffff"

                },

                textColor: "#333"

            },

            grid: {

                vertLines: {

                    color: "#efefef"

                },

                horzLines: {

                    color: "#efefef"

                }

            },

            rightPriceScale: {

                borderColor: "#d1d4dc"

            },

            timeScale: {

                borderColor: "#d1d4dc"

            }

        });

        // ===========================
        // Candlestick Series
        // ===========================

        const candleSeries = chart.addSeries(CandlestickSeries);

        candleSeries.setData(

            data.map(item => ({

                time: item.date,

                open: Number(item._open_),

                high: Number(item._high_),

                low: Number(item._low_),

                close: Number(item._close_)

            }))

        );

        // ===========================
        // SMA 5
        // ===========================

        const sma5Series = chart.addSeries(LineSeries, {

            color: "#2962FF",

            lineWidth: 2,

            title: "SMA 5"

        });

        sma5Series.setData(

            data
                .filter(item => item.sma5 !== null)
                .map(item => ({

                    time: item.date,

                    value: Number(item.sma5)

                }))

        );

        // ===========================
        // SMA 10
        // ===========================

        const sma10Series = chart.addSeries(LineSeries, {

            color: "#FF9800",

            lineWidth: 2,

            title: "SMA 10"

        });

        sma10Series.setData(

            data
                .filter(item => item.sma10 !== null)
                .map(item => ({

                    time: item.date,

                    value: Number(item.sma10)

                }))

        );

        // ===========================
        // Bollinger Bands
        // ===========================

        const upperBand = chart.addSeries(LineSeries, {

            color: "#4CAF50",

            lineWidth: 1,

            title: "Upper Band"

        });

        upperBand.setData(

            data
                .filter(item => item.upper_band !== null)
                .map(item => ({

                    time: item.date,

                    value: Number(item.upper_band)

                }))

        );

        const middleBand = chart.addSeries(LineSeries, {

            color: "#9E9E9E",

            lineWidth: 1,

            title: "Middle Band"

        });

        middleBand.setData(

            data
                .filter(item => item.middle_band !== null)
                .map(item => ({

                    time: item.date,

                    value: Number(item.middle_band)

                }))

        );

        const lowerBand = chart.addSeries(LineSeries, {

            color: "#F44336",

            lineWidth: 1,

            title: "Lower Band"

        });

        lowerBand.setData(

            data
                .filter(item => item.lower_band !== null)
                .map(item => ({

                    time: item.date,

                    value: Number(item.lower_band)

                }))

        );

        // ===========================
        // Volume
        // ===========================

        const volumeSeries = chart.addSeries(HistogramSeries, {

            priceFormat: {

                type: "volume"

            },

            priceScaleId: ""

        });

        volumeSeries.priceScale().applyOptions({

            scaleMargins: {

                top: 0.8,

                bottom: 0

            }

        });

        volumeSeries.setData(

            data.map(item => ({

                time: item.date,

                value: Number(item.volume),

                color:

                    item._close_ >= item._open_

                        ? "#26a69a"

                        : "#ef5350"

            }))

        );

        chart.timeScale().fitContent();

        const resizeObserver = new ResizeObserver(() => {

            chart.applyOptions({

                width: chartContainer.current.clientWidth

            });

        });

        resizeObserver.observe(chartContainer.current);

        return () => {

            resizeObserver.disconnect();

            chart.remove();

        };

    }, [data]);

    return (

        <div className="bg-white rounded-xl shadow-lg p-6">

            <h2 className="text-2xl font-bold mb-5">

                Stock Price Chart

            </h2>

            <div
                ref={chartContainer}
                className="w-full"
            />

        </div>

    );

}

export default PriceChart;