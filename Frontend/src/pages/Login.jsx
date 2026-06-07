import { useState } from "react";

import { useNavigate } from "react-router-dom";

import api from "../api/axios";



function Login(){



    const navigate = useNavigate();




    const [email,setEmail] =

        useState("");



    const [password,setPassword] =

        useState("");




    const loginUser = async()=>{



        try{





            const response = await api.post(


                "/auth/login",


                {


                    email:email,


                    password:password


                }


            );






            console.log(

                response.data

            );






            localStorage.setItem(


                "token",


                response.data.access_token


            );






            navigate(

                "/dashboard"

            );






        }


        catch(error){



            console.log(


                error.response?.data


            );



            alert(


                "Invalid login"


            );



        }



    };









    return(



        <div className="min-h-screen bg-black flex justify-center items-center">






            <div className="
            bg-gray-900
            p-10
            rounded-xl
            w-96
            ">






                <h1 className="
                text-white
                text-3xl
                font-bold
                mb-8
                ">


                    Login


                </h1>









                <input


                    value={email}


                    onChange={(e)=>

                        setEmail(

                            e.target.value

                        )

                    }


                    placeholder="Email"



                    className="
                    w-full
                    p-3
                    rounded
                    mb-5
                    "


                />









                <input


                    value={password}


                    type="password"


                    onChange={(e)=>

                        setPassword(

                            e.target.value

                        )

                    }


                    placeholder="Password"



                    className="
                    w-full
                    p-3
                    rounded
                    mb-5
                    "


                />









                <button


                    onClick={loginUser}


                    className="
                    bg-blue-600
                    text-white
                    w-full
                    py-3
                    rounded
                    "


                >


                    Login


                </button>






            </div>





        </div>


    );



}




export default Login;