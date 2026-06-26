import api from "./axios";

export const getStocksList = async () => {
    const response = await api.get("/stocks/stockslist");
    return response.data;
};

export const getStockPrice = async (
    stockName,
    startDate,
    endDate
) => {

    const response = await api.get(
        `/stocks/${stockName}/${startDate}/${endDate}`
    );

    return response.data;
};