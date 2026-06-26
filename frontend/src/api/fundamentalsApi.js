import api from "./axios";

export const getFundamentals = async (
    stockName
) => {

    const response = await api.get(
        `/fundamentals/${stockName}`
    );

    return response.data;
};