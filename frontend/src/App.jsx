import ResearchDashboard from "./pages/ResearchDashboard";

function App() {

    return (
        <>
            <ResearchDashboard />
        </>
    );

}

export default App;

// make a react page in which, there is a user input field in which the user have to select a stock name from a drop down(the list of stocks is fetched from the database from the stocks table with an api end point present at the backend (@router.get("/stocks/stockslist")) int the form of [

//             {

//                 "id" : stock.id,

//                 "symbol" : stock.symbol

//             }

//             for stock in stocks_list

//         ]), and then user will select the stock name and then the frontend will send the stock_name , along with the stock_id to the backend, and after the user have submitted the request to the backend, the frontend should be updated with the following features, 

// 1- get the stocks price in a date range with maximum limit of 30 days from the backend api end point (@router.get("/stocks/{stock_name}/{start_date}/{end_date}") in the form of data = (

//         db.query(StockData, StocksIndicators)

//         .outerjoin(

//             StocksIndicators,

//             (StockData.stock_id == StocksIndicators.stock_id)

//             & (StockData.id == StocksIndicators.data_id)

//         )

//         .filter(

//             StockData.stock_id == stock_id,

//             StockData.date >= start_date,

//             StockData.date <= end_date

//         )

//         .order_by(StockData.date)

//         .all()

//     )

//     return [

//     {

//         **{

//             c.name: getattr(stock, c.name)

//             for c in StockData.__table__.columns

//         },

//         **(

//             {

//                 c.name: getattr(indicator, c.name)

//                 for c in StocksIndicators.__table__.columns

//             }

//             if indicator

//             else {}

//         )

//     }

//     for stock, indicator in data

// ])

// 2- get the top 5 recents news about the particular stock along with its sentiment score and label with the backend api end point (@router.get("/stocks/{stock_name}/news") in the form of [ 

//         {

//             "id": news.id,

//             "stock": stock.symbol,

//             "content_id": news.content_id,

//             "title": news.title,

//             "summary": news.summary,

//             "date": news.date,

//             "url": news.url,

//             "source": news.source

//         }

//         for news, stock in data

//     ], @router.get("/stocks/news/{news_feed_id}") in the form of return [

//         {

//             "news_feed_id" : info.news_feed_id,

//             "label" : info.label,

//             "sentiment" : info.sentiment

//         }

//         for info in data

//     ])



// 3- gives the fundamental analyzers from the endpoint (@router.get("/fundamentals/{stock_name}")) in the form of {"stock_name":"RELIANCE.NS","metrics":{"growth":{"EPS growth":{"2023-03-31":7.16,"2024-03-31":4.37,"2025-03-31":0.04},"Revenue Growth":{"2024-03-31":2.65,"2025-03-31":7.06,"2026-03-31":9.59},"Net Income Growth":{"2024-03-31":4.38,"2025-03-31":0.04,"2026-03-31":15.98}},"margin":{"Gross Margin":{"2023-03-31":23.46,"2024-03-31":25.13,"2025-03-31":25.09,"2026-03-31":25.58},"Operating Margin":{"2023-03-31":11.62,"2024-03-31":12.39,"2025-03-31":11.66,"2026-03-31":11.48},"Net Margin":{"2023-03-31":7.6,"2024-03-31":7.73,"2025-03-31":7.22,"2026-03-31":7.64}},"returns":{"ROE":{"2023-03-31":9.32,"2024-03-31":8.77,"2025-03-31":8.26,"2026-03-31":8.93},"ROA":{"2023-03-31":4.15,"2024-03-31":3.96,"2025-03-31":3.57,"2026-03-31":3.71},"ROIC":{"2023-03-31":9.91,"2024-03-31":9.99,"2025-03-31":9.44,"2026-03-31":9.49}},"liquidity":{"current ratio":{"2023-03-31":1.07,"2024-03-31":1.18,"2025-03-31":1.1,"2026-03-31":1.1},"cash ratio":{"2023-03-31":0.09,"2024-03-31":0.24,"2025-03-31":0.22,"2026-03-31":0.25}},"leverage":{"Dept_to_Equity":{"2023-03-31":0.20802883607445669,"2024-03-31":0.19712116155823567,"2025-03-31":0.18951388144633077,"2026-03-31":0.18272471007373264},"Dept_to_assets":{"2023-03-31":0.46711143891645435,"2024-03-31":0.43623224752703593,"2025-03-31":0.43830052182163187,"2026-03-31":0.44025087663020035},"Net Dept":{"2023-03-31":3002360000000.0,"2024-03-31":2526020000000.0,"2025-03-31":2689300000000.0,"2026-03-31":2606730000000.0}},"Cash Flow Quality":{"fcf_margin":{"2023-03-31":-2.96,"2024-03-31":0.66,"2025-03-31":4.02,"2026-03-31":6.55},"ocf_margin":{"2023-03-31":13.1,"2024-03-31":17.62,"2025-03-31":18.52,"2026-03-31":18.17},"Cash Conversions":{"2023-03-31":1.7245659800305837,"2024-03-31":2.2807486246965714,"2025-03-31":2.5658023202389155,"2026-03-31":2.3783720210461157}}}}
