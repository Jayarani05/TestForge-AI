import { useState } from "react";

import api from "../api/axios";



function Export(){


    const [exportType,setExportType] =
    useState("pdf");


    const [content,setContent] =
    useState("");


    const [loading,setLoading] =
    useState(false);




    const downloadFile = async()=>{


        try{


            setLoading(true);



            const response =
            await api.post(

                "/export",

                {

                    export_type:
                    exportType,


                    data:{


                        generated_test_cases:{


                            "Generated Tests":[


                                {


                                    id:"TC001",


                                    title:
                                    content,


                                    type:
                                    "Functional",


                                    priority:
                                    "High"


                                }


                            ]


                        },



                        code:
                        content,


                        language:
                        "python"


                    }


                },


                {

                    responseType:
                    "blob"

                }


            );







            const url =
            window.URL.createObjectURL(

                new Blob(
                    [response.data]
                )

            );




            const link =
            document.createElement(
                "a"
            );



            link.href=url;






            if(exportType==="pdf"){


                link.download=
                "qa_report.pdf";


            }


            else if(exportType==="excel"){


                link.download=
                "test_cases.xlsx";


            }


            else{


                link.download=
                "generated_test.py";


            }




            link.click();




        }


        catch(error){


            console.log(
                error
            );


            alert(
                "Export failed"
            );


        }



        setLoading(false);


    };








    return(


        <div className="min-h-screen bg-black p-10">


            <h1 className="text-white text-3xl font-bold">

                Export Center

            </h1>





            <textarea


            value={content}


            onChange={(e)=>

            setContent(
                e.target.value
            )

            }


            placeholder="Paste generated test content"


            className="
            bg-gray-900
            text-white
            p-5
            rounded-xl
            w-full
            h-52
            mt-8
            "


            />







            <select


            value={exportType}


            onChange={(e)=>

            setExportType(
                e.target.value
            )

            }


            className="
            bg-gray-900
            text-white
            p-4
            rounded-xl
            mt-5
            "


            >


                <option value="pdf">

                    PDF

                </option>



                <option value="excel">

                    Excel

                </option>



                <option value="code">

                    Code

                </option>



            </select>








            <button


            onClick={downloadFile}


            disabled={loading}


            className="
            bg-blue-600
            text-white
            px-6
            py-3
            rounded-lg
            ml-5
            "


            >


            {

            loading

            ?

            "Exporting..."

            :

            "Download"

            }


            </button>






        </div>


    );


}



export default Export;