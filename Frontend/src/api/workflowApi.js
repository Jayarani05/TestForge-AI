import { api } from "./axios";



// ===============================
// Repository Analyzer
// ===============================

export const analyzeRepository = async (repoUrl) => {


    try {


        const response = await api.post(

            "/repository/analyze",

            {
                repo_url: repoUrl
            }

        );


        return response.data;


    }


    catch (error) {


        console.error(
            "Repository Analysis Error:",
            error
        );


        throw error;


    }

};







// ===============================
// Test Case Generation
// ===============================


export const generateTestCases = async (

    repoContext,

    userStory

) => {


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




                dependencies:

                    repoContext?.dependencies ||

                    [],




                api_endpoints:

                    repoContext?.api_endpoints ||

                    []


            },





            user_story:

                userStory,




            language:

                "English"


        };






        console.log(

            "FINAL TEST GENERATION PAYLOAD:",

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






        console.log(

            "TEST GENERATION RESPONSE:",

            response.data

        );





        return response.data;



    }


    catch (error) {


        console.error(

            "Generate Test Case API Error:",

            error.response?.data ||

            error.message

        );





        throw {


            error:


                error.response?.data?.detail ||

                error.message ||

                "Test generation failed"


        };


    }


};









// ===============================
// Automation Generation
// ===============================


export const generateAutomation = async (

    repoContext,

    testCases

) => {



    const response = await api.post(


        "/automation/generate",


        {


            repo_context:

                repoContext || {},




            test_cases:

                testCases || []


        }


    );




    return response.data;



};









// ===============================
// Test Execution
// ===============================


export const executeTests = async () => {


    const response = await api.post(

        "/tests/run"

    );



    return response.data;


};

// ===============================
// Test Execution
// ===============================


export const runTests = async () => {

    const response = await api.post(
        "/tests/run"
    );


    return response.data;

};