import api from "./axios";

export const getNews = async (stockName) => {

    const response = await api.get(
        `/stocks/${stockName}/news`
    );

    return response.data;
};

export const getNewsSentiment = async (
    newsFeedID
) => {

    const response = await api.get(
        `/stocks/news/${newsFeedID}`
    );

    return response.data;
};