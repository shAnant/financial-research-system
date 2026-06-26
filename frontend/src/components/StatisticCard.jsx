function StatisticCard({

    title,

    value,

    color

}){

    return(

        <div className={`rounded-xl p-5 ${color}`}>

            <p className="text-sm">

                {title}

            </p>

            <h2 className="text-3xl font-bold">

                {value}

            </h2>

        </div>

    )

}

export default StatisticCard;