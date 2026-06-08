function Settings(){


    return (


        <div>


            <h1
            className="
            text-2xl
            font-bold
            mb-6
            "
            >

                Settings

            </h1>





            <div
            className="
            bg-white
            rounded-xl
            border
            p-6
            "
            >


                <h2
                className="
                font-semibold
                mb-4
                "
                >

                    Profile

                </h2>



                <div
                className="
                space-y-4
                "
                >



                    <div>


                        <label
                        className="
                        text-sm
                        text-gray-500
                        "
                        >

                            Name

                        </label>


                        <input

                        value="Jayarani"

                        readOnly

                        className="
                        mt-1
                        border
                        rounded-lg
                        p-2
                        w-full
                        "

                        />


                    </div>






                    <div>


                        <label
                        className="
                        text-sm
                        text-gray-500
                        "
                        >

                            Role

                        </label>


                        <input

                        value="QA Engineer"

                        readOnly

                        className="
                        mt-1
                        border
                        rounded-lg
                        p-2
                        w-full
                        "

                        />


                    </div>





                </div>


            </div>



        </div>


    );


}



export default Settings;