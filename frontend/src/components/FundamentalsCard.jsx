function FundamentalsCard({

    title,

    metrics

}) {

    return (

        <div className="bg-white rounded-xl shadow p-5">

            <h2 className="font-bold mb-4">

                {title}

            </h2>

            {

                Object.entries(metrics).map(

                    ([metric, values]) => (

                        <div

                            key={metric}

                            className="mb-5"

                        >

                            <strong>

                                {metric}

                            </strong>

                            {

                                Object.entries(values).map(

                                    ([year, value]) => (

                                        <div key={year}>

                                            {year}

                                            {" : "}

                                            {value}

                                        </div>

                                    )

                                )

                            }

                        </div>

                    )

                )

            }

        </div>

    );

}

export default FundamentalsCard;