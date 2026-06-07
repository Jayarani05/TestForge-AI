import { NavLink } from "react-router-dom";


import { useAuth } from "../../context/AuthContext";




function Sidebar(){



    const { logout } = useAuth();





    const menu = [



        {

            name:"Dashboard",

            path:"/dashboard",

            icon:"📊"

        },



        {

            name:"Projects",

            path:"/projects",

            icon:"🗂️"

        },



        {

            name:"AI Generator",

            path:"/generate",

            icon:"🤖"

        },



        {

            name:"Execution",

            path:"/execution",

            icon:"⚙️"

        },



        {

            name:"Repository",

            path:"/repository",

            icon:"🧠"

        },



        {

            name:"Self Healing",

            path:"/healing",

            icon:"🩹"

        },



        {

            name:"CI/CD",

            path:"/cicd",

            icon:"🚀"

        },



        {

            name:"Export",

            path:"/export",

            icon:"📄"

        }



    ];









    return (




        <div

            className="
            h-screen
            w-64
            bg-gray-950
            text-white
            fixed
            left-0
            top-0
            p-6
            "


        >





            <h1

                className="
                text-2xl
                font-bold
                mb-10
                "

            >


                TestForge AI


            </h1>








            {


                menu.map(

                    (item)=>(



                        <NavLink


                            key={item.path}


                            to={item.path}


                            className={

                                ({isActive})=>


                                `

                                block
                                p-3
                                rounded-lg
                                mb-3


                                ${

                                    isActive

                                    ?

                                    "bg-blue-600"

                                    :

                                    "hover:bg-gray-800"

                                }


                                `


                            }


                        >



                            {item.icon}


                            {" "}


                            {item.name}



                        </NavLink>



                    )

                )

            }









            <button


                onClick={logout}


                className="
                absolute
                bottom-8
                left-6
                bg-red-600
                px-8
                py-3
                rounded-lg
                hover:bg-red-700
                "



            >



                Logout



            </button>








        </div>



    );



}



export default Sidebar;