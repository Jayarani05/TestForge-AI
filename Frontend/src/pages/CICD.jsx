import { useState } from "react";

import api from "../api/axios";

import CodeBox from "../components/CodeBox";



function CICD(){


    const [language,setLanguage] =
    useState("Python");


    const [framework,setFramework] =
    useState("Pytest");


    const [tool,setTool] =
    useState("GitHub Actions");


    const [pipeline,setPipeline] =
    useState(null);


    const [loading,setLoading] =
    useState(false);




    const generatePipeline = async()=>{


        try{


            setLoading(true);



            const response = await api.post(

                "/cicd/generate",

                {

                    language: language,

                    framework: framework,

                    tool: tool

                }

            );




            console.log(
                response.data
            );



            setPipeline(

                response.data.pipeline

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








    return(


        <div className="min-h-screen bg-black p-10">





            <h1 className="text-white text-3xl font-bold">

                CI/CD Generator

            </h1>








            <select

            value={language}

            onChange={(e)=>

            setLanguage(e.target.value)

            }

            className="bg-gray-900 text-white p-4 rounded-xl mt-8"

            >


                <option>

                    Python

                </option>


                <option>

                    Java

                </option>


            </select>








            <select

            value={framework}

            onChange={(e)=>

            setFramework(e.target.value)

            }

            className="bg-gray-900 text-white p-4 rounded-xl ml-5"

            >


                <option>

                    Pytest

                </option>


                <option>

                    Selenium

                </option>


                <option>

                    JUnit

                </option>



            </select>








            <select

            value={tool}

            onChange={(e)=>

            setTool(e.target.value)

            }

            className="bg-gray-900 text-white p-4 rounded-xl ml-5"

            >



                <option>

                    GitHub Actions

                </option>



                <option>

                    Jenkins

                </option>



            </select>









            <br />






            <button


            onClick={generatePipeline}


            disabled={loading}


            className="bg-blue-600 text-white px-6 py-3 rounded-lg mt-6"


            >



            {

            loading

            ?

            "Generating..."

            :

            "Generate Pipeline"

            }



            </button>









            {

            pipeline &&


            <div className="mt-8">


                <h2 className="text-white text-xl">


                    {

                    pipeline.file_name

                    }


                </h2>



                <CodeBox

                value={

                pipeline.pipeline_code

                }

                />



            </div>


            }





        </div>


    );


}



export default CICD;