function LLMSummarySection({

    summary,

    loading,

    onGenerate

}) {

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-2xl font-bold mb-5">

                🤖 AI Financial Analysis

            </h2>

            {

                !summary &&

                <button

                    onClick={onGenerate}

                    className="bg-blue-600 text-white px-5 py-3 rounded-lg"

                >

                    Generate AI Summary

                </button>

            }

            {

                loading &&

                <p>

                    Generating Summary...

                </p>

            }

            {

                summary &&

                <>

                    <h3 className="font-bold mt-4">

                        Executive Summary

                    </h3>

                    <p>

                        {summary.executive_summary}

                    </p>

                    <h3 className="font-bold mt-6">

                        Growth Analysis

                    </h3>

                    <p>

                        {summary.growth_analysis}

                    </p>

                    <h3 className="font-bold mt-6">

                        Profitability

                    </h3>

                    <p>

                        {summary.profitability_analysis}

                    </p>

                    <h3 className="font-bold mt-6">

                        Liquidity

                    </h3>

                    <p>

                        {summary.liquidity_analysis}

                    </p>

                    <h3 className="font-bold mt-6">

                        Cash Flow

                    </h3>

                    <p>

                        {summary.cash_flow_analysis}

                    </p>

                    <h3 className="font-bold mt-6">

                        Strengths

                    </h3>

                    <ul className="list-disc ml-5">

                        {

                            summary.strengths.map(

                                (item,index)=>

                                    <li key={index}>

                                        {item}

                                    </li>

                            )

                        }

                    </ul>

                    <h3 className="font-bold mt-6">

                        Weaknesses

                    </h3>

                    <ul className="list-disc ml-5">

                        {

                            summary.weaknesses.map(

                                (item,index)=>

                                    <li key={index}>

                                        {item}

                                    </li>

                            )

                        }

                    </ul>

                    <h3 className="font-bold mt-6">

                        Overall Financial Health

                    </h3>

                    <p>

                        <strong>

                            Rating:

                        </strong>

                        {summary.overall_financial_health.rating}

                    </p>

                    <p className="mt-2">

                        {summary.overall_financial_health.reason}

                    </p>

                </>

            }

        </div>

    );

}

export default LLMSummarySection;