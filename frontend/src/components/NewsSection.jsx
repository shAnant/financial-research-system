import NewsCard from "./NewsCard";

function NewsSection({ news }) {

    return (

        <div className="space-y-4">

            <h2 className="text-2xl font-semibold">

                Latest News

            </h2>

            {

                news.map(item => (

                    <NewsCard

                        key={item.id}

                        news={item}

                    />

                ))

            }

        </div>

    );

}

export default NewsSection;