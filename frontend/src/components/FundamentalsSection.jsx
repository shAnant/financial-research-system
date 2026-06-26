import FundamentalsCard from "./FundamentalsCard";

function FundamentalsSection({

    fundamentals

}) {

    if (!fundamentals) return null;

    const metrics = fundamentals.metrics;

    return (

        <div>

            <h2 className="text-2xl font-bold mb-6">

                Fundamental Analysis

            </h2>

            <div className="grid grid-cols-2 gap-6">

                {

                    Object.entries(metrics).map(

                        ([category, value]) => (

                            <FundamentalsCard

                                key={category}

                                title={category}

                                metrics={value}

                            />

                        )

                    )

                }

            </div>

        </div>

    );

}

export default FundamentalsSection;