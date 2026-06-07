import { useState } from "react";

import api from "../api/axios";



function Healing(){


    const [failedCode,setFailedCode] = useState("");

    const [errorLog,setErrorLog] = useState("");

    const [dom,setDom] = useState("");

    const [result,setResult] = useState(null);

    const [loading,setLoading] = useState(false);




    const repairLocator = async()=>{


        try{


            setLoading(true);



            const response = await api.post(

                "/healing/repair",

                {

                    failed_code: failedCode,

                    error_log: errorLog,

                    dom_snapshot: dom

                }

            );



            console.log(response.data);



            setResult(

                response.data.healed_result

            );



        }


        catch(error){


            console.log(

                error.response?.data

            );


            alert(

                JSON.stringify(

                    error.response?.data,

                    null,

                    2

                )

            );


        }




        setLoading(false);


    };







    return (


        <div className="min-h-screen bg-black p-10">



            <h1 className="text-white text-3xl font-bold">

                AI Self Healing Locator

            </h1>








            <textarea


                value={failedCode}


                onChange={(e)=>

                    setFailedCode(e.target.value)

                }


                placeholder="Paste failed Selenium code"


                className="
                bg-gray-900
                text-white
                p-4
                rounded-xl
                w-full
                h-32
                mt-8
                "

            />









            <textarea


                value={errorLog}


                onChange={(e)=>

                    setErrorLog(e.target.value)

                }


                placeholder="Paste Selenium error log"


                className="
                bg-gray-900
                text-white
                p-4
                rounded-xl
                w-full
                h-32
                mt-5
                "

            />









            <textarea


                value={dom}


                onChange={(e)=>

                    setDom(e.target.value)

                }


                placeholder="Paste current HTML DOM"


                className="
                bg-gray-900
                text-white
                p-4
                rounded-xl
                w-full
                h-32
                mt-5
                "

            />










            <button


                onClick={repairLocator}


                disabled={loading}


                className="
                bg-blue-600
                text-white
                px-6
                py-3
                rounded-lg
                mt-5
                "

            >


                {

                loading

                ?

                "Healing..."

                :

                "Repair Locator"

                }


            </button>









            {

                result &&



                <div className="
                bg-gray-900
                text-white
                rounded-xl
                p-6
                mt-8
                ">




                    <p>

                    <b>Broken Locator:</b>{" "}

                    {result.broken_locator}

                    </p>





                    <p>

                    <b>Reason:</b>{" "}

                    {result.reason}

                    </p>






                    <p>

                    <b>Suggested:</b>{" "}

                    {result.suggested_locator}

                    </p>






                    <pre>

                    {result.fixed_code}

                    </pre>





                </div>


            }





        </div>


    );


}



export default Healing;