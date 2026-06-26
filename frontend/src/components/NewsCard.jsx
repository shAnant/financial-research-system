function NewsCard({ news }) {

    const color =

        news.label === "Positive"

            ? "bg-green-100"

            : news.label === "Negative"

            ? "bg-red-100"

            : "bg-yellow-100";

    return (

        <div className="border rounded-xl p-5">

            <div className="flex justify-between">

                <span className={`${color} px-3 py-1 rounded`}>

                    {news.label}

                </span>

                <span>

                    {news.sentiment}

                </span>

            </div>

            <h3 className="font-bold mt-3">

                {news.title}

            </h3>

            <p className="mt-3">

                {news.summary}

            </p>

            <a

                href={news.url}

                target="_blank"

            >

                Read More

            </a>

        </div>

    );

}

export default NewsCard;