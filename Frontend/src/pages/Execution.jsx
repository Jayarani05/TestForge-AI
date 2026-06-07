import { useState } from "react";

import api from "../api/axios";

import CodeBox from "../components/CodeBox";



function Execution(){


    const [code,setCode] = useState("");

    const [loading,setLoading] = useState(false);

    const [result,setResult] = useState(null);




    const executeTest = async()=>{


        try{


            setLoading(true);



            const response = await api.post(

                "/execution/run",

                {

                    code: code

                }

            );




            console.log(

                response.data

            );



            setResult(

                response.data

            );



        }


        catch(error){


            console.log(

                "EXECUTION ERROR",

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

                Test Execution

            </h1>







            <textarea


                value={code}


                onChange={(e)=>

                    setCode(

                        e.target.value

                    )

                }


                placeholder="Paste pytest automation code..."


                className="
                w-full
                h-52
                bg-gray-900
                text-white
                rounded-xl
                p-5
                mt-8
                "

            />








            <button


                onClick={executeTest}


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

                    "Running..."

                    :

                    "Run Test"

                }


            </button>








            {

                result && (



                    <div className="mt-10">







                        <h2 className="text-white text-2xl">


                            {


                            result.execution_result?.passed

                            ?

                            "✅ Test Passed"

                            :

                            "❌ Test Failed"


                            }



                        </h2>








                        <h3 className="text-white mt-5">


                            Execution Logs


                        </h3>





                        <CodeBox


                            value={

                                result.execution_result?.logs

                            }


                        />









                        {


                        result.bug_analysis?.bug_found && (



                            <div className="
                            bg-red-950
                            text-white
                            p-6
                            rounded-xl
                            mt-6
                            ">





                                <h2 className="
                                text-xl
                                font-bold
                                ">

                                    AI Bug Analysis

                                </h2>








                                <p>


                                    <b>Title:</b>{" "}


                                    {

                                    result
                                    .bug_analysis
                                    .analysis
                                    ?.title

                                    }


                                </p>









                                <p>


                                    <b>Severity:</b>{" "}


                                    {

                                    result
                                    .bug_analysis
                                    .analysis
                                    ?.severity

                                    }


                                </p>










                                <p>


                                    <b>Root Cause:</b>{" "}


                                    {

                                    result
                                    .bug_analysis
                                    .analysis
                                    ?.root_cause

                                    }


                                </p>










                                <p>


                                    <b>Possible Fix:</b>{" "}


                                    {

                                    result
                                    .bug_analysis
                                    .analysis
                                    ?.possible_fix

                                    }


                                </p>










                                <p>


                                    <b>QA Recommendation:</b>{" "}


                                    {

                                    result
                                    .bug_analysis
                                    .analysis
                                    ?.qa_recommendation

                                    }


                                </p>





                            </div>



                        )


                        }



                    </div>


                )

            }





        </div>


    );


}



export default Execution;