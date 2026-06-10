import { useState } from "react";
import { api } from "../api/axios";
import Loader from "./Loader";
import "./TestCaseGenerator.css";


export default function TestCaseGenerator({
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

            setError("Please enter a user story");
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
                        0,


                    structure:
                        repoContext?.structure ||
                        [],


                    dependencies:
                        repoContext?.dependencies ||
                        []

                },



                user_story:
                    userStory.trim(),



                language:
                    "English"

            };





            console.log(
                "SENDING TEST PAYLOAD:",
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




            const result = response.data;




            console.log(
                "TEST RESPONSE:",
                result
            );





            setTestCases(result);




            onGenerationComplete?.(
                result
            );



        }


        catch (err) {



            console.log(

                "BACKEND ERROR:",

                JSON.stringify(
                    err.response?.data,
                    null,
                    2
                )

            );





            let message =
                "Failed to generate test cases";




            const detail =
                err.response?.data?.detail;





            if (Array.isArray(detail)) {


                message = detail

                    .map(

                        e =>

                            `${e.loc?.join(".")} : ${e.msg}`

                    )

                    .join("\n");


            }


            else if (typeof detail === "string") {


                message = detail;


            }


            else if (err.message) {


                message = err.message;

            }





            setError(message);


        }



        finally {


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




                <div className="input-group">


                    <label>
                        User Story
                    </label>



                    <textarea

                        placeholder="As a user, I want registration functionality..."

                        value={userStory}


                        onChange={(e)=>{

                            setUserStory(
                                e.target.value
                            );

                            setError("");

                        }}


                        disabled={loading}

                        rows={6}

                    />




                    {
                        error &&

                        <pre className="error-message">

                            {error}

                        </pre>
                    }


                </div>





                <button

                    onClick={handleGenerate}

                    disabled={
                        loading ||
                        !userStory.trim()
                    }

                    className="generate-btn"

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

                    testCases?.test_cases &&


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




                                <b>
                                    Priority:
                                </b>

                                {" "}

                                {tc.priority}




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


                }


            </div>


        </div>

    );


}