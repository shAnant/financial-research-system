function DateSelector({

    startDate,
    endDate,
    setStartDate,
    setEndDate

}) {

    return (

        <div className="flex gap-4">

            <div>

                <label className="font-semibold">

                    Start Date

                </label>

                <input
                    type="date"
                    value={startDate}
                    onChange={(e)=>setStartDate(e.target.value)}
                    className="border rounded-lg p-2"
                />

            </div>

            <div>

                <label className="font-semibold">

                    End Date

                </label>

                <input
                    type="date"
                    value={endDate}
                    onChange={(e)=>setEndDate(e.target.value)}
                    className="border rounded-lg p-2"
                />

            </div>

        </div>

    );

}

export default DateSelector;