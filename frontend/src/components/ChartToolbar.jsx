function ChartToolbar({

    showSMA5,
    setShowSMA5,

    showSMA10,
    setShowSMA10,

    showBands,
    setShowBands,

    showVolume,
    setShowVolume

}) {

    return (

        <div className="flex gap-6 mb-5">

            <label>

                <input

                    type="checkbox"

                    checked={showSMA5}

                    onChange={()=>

                        setShowSMA5(!showSMA5)

                    }

                />

                SMA5

            </label>

            <label>

                <input

                    type="checkbox"

                    checked={showSMA10}

                    onChange={()=>

                        setShowSMA10(!showSMA10)

                    }

                />

                SMA10

            </label>

            <label>

                <input

                    type="checkbox"

                    checked={showBands}

                    onChange={()=>

                        setShowBands(!showBands)

                    }

                />

                Bollinger Bands

            </label>

            <label>

                <input

                    type="checkbox"

                    checked={showVolume}

                    onChange={()=>

                        setShowVolume(!showVolume)

                    }

                />

                Volume

            </label>

        </div>

    );

}

export default ChartToolbar;