import axios from "./axios";

export async function getLLMSummary(stockName) {

    const response = await axios.get(
        `/llm/summary/${stockName}`
    );

    return response.data;

}