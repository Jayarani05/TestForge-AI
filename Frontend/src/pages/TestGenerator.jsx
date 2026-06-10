import { useState } from "react";
import { api } from "../api/axios";
import Loader from "../components/Loader";
import "../components/TestCaseGenerator.css";



function TestCaseGenerator({
    repoContext,
    onGenerationComplete,
    onLoading,
}) {


    const [userStory, setUserStory] = useState("");

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    const [testCases, setTestCases] = useState(null);



    const handleGenerate = async () => {


        if (!userStory.trim()) {

            setError(
                "Please enter a user story"
            );

            return;

        }



        setLoading(true);

        setError("");

        onLoading?.(true);



        try {


            const payload = {


                repo_context: {

                    project_name:
                        repoContext?.project_name ||
                        "TestForge AI",


                    language:
                        repoContext?.language ||
                        "Python",


                    framework:
                        repoContext?.framework ||
                        "FastAPI",


                    total_files:
                        repoContext?.total_files ||
                        0

                },



                user_story:
                    userStory.trim(),



                language:
                    "English"


            };




            console.log(

                "Sending Payload:",

                JSON.stringify(
                    payload,
                    null,
                    2
                )

            );





            const response = await api.post(

                "/tests/generate",

                payload

            );




            const data = response.data;



            console.log(

                "Response:",

                data

            );




            setTestCases(data);



            onGenerationComplete?.(

                data

            );



        }


        catch(error){



            console.error(

                "Generation failed:",

                error

            );



            let message =
                "Failed to generate tests";



            const detail =
                error.response?.data?.detail;




            if(Array.isArray(detail)){


                message = detail

                    .map(

                        item => item.msg

                    )

                    .join(", ");


            }


            else if(

                typeof detail === "string"

            ){


                message = detail;


            }


            else if(

                error.message

            ){


                message = error.message;


            }



            setError(message);



        }



        finally{


            setLoading(false);


            onLoading?.(false);


        }


    };







    return (


        <div className="test-case-generator">


            <div className="generator-card">



                <h2>

                    Test Case Generator

                </h2>



                <p className="subtitle">

                    Generate QA test cases from user story

                </p>





                <textarea


                    value={userStory}


                    onChange={

                        (e)=>

                        setUserStory(

                            e.target.value

                        )

                    }


                    placeholder="As a user, I want login functionality..."


                    rows={6}

                />






                {
                    error &&

                    <p className="error-message">

                        {error}

                    </p>

                }






                <button


                    className="generate-btn"


                    disabled={

                        loading ||

                        !userStory.trim()

                    }


                    onClick={handleGenerate}

                >


                    {

                        loading

                        ?

                        <>

                            <Loader />

                            Generating...

                        </>


                        :

                        "Generate Test Cases"


                    }


                </button>









                {


                    testCases?.test_cases && (


                    <div className="test-cases-results">



                        <h3>

                            Generated Test Cases

                        </h3>





                        {

                        testCases.test_cases.map(

                        (tc,index)=>(


                        <div

                            key={index}

                            className="test-case-card"

                        >




                            <h4>


                                {tc.id}


                                {" - "}


                                {tc.title}


                            </h4>





                            <p>

                                {tc.description}

                            </p>





                            <p>


                                Priority:


                                {" "}


                                {tc.priority}


                            </p>






                            <h5>

                                Steps

                            </h5>






                            <ol>


                                {

                                tc.steps?.map(

                                (step,i)=>(


                                <li key={i}>

                                    {step}

                                </li>


                                ))

                                }


                            </ol>







                            <h5>

                                Expected Result

                            </h5>




                            <p>

                                {tc.expected_result}

                            </p>





                        </div>


                        ))

                        }


                    </div>


                    )


                }




            </div>


        </div>


    );


}



export default TestCaseGenerator;