import { NavLink } from "react-router-dom";


import {

    LayoutDashboard,
    FolderKanban,
    Bot,
    PlayCircle,
    Code,
    Bug,
    Wrench,
    Rocket,
    FileDown,
    Settings,
    LogOut

} from "lucide-react";


import { useAuth } from "../context/AuthContext";





function Sidebar(){



    const { logout } = useAuth();





    const menu = [



        {

            name:"Dashboard",

            path:"/dashboard",

            icon:LayoutDashboard

        },



        {

            name:"Projects",

            path:"/projects",

            icon:FolderKanban

        },



        {

            name:"Test Generator",

            path:"/generate",

            icon:Bot

        },



        {

            name:"Test Execution",

            path:"/execution",

            icon:PlayCircle

        },



        {
            name:"Repository Analysis",

            path:"/repository",

            icon:Code
        },



        {

            name:"Self Healing",

            path:"/healing",

            icon:Wrench

        },



        {

            name:"CI/CD Generator",

            path:"/cicd",

            icon:Rocket

        },



        {

            name:"Export Center",

            path:"/export",

            icon:FileDown

        },



        {

            name:"Settings",

            path:"/settings",

            icon:Settings

        },

        {
            name:"Bug Analysis",
            path:"/bugs",
            icon:Bug
        }



    ];










    return (



        <aside


        className="
        fixed
        left-0
        top-0

        h-screen
        w-64

        bg-white

        border-r
        border-gray-200

        flex
        flex-col
        "


        >








            {/* LOGO */}



            <div

            className="
            h-16

            px-5

            flex
            items-center

            border-b
            "

            >




                <div>



                    <h1

                    className="
                    text-lg
                    font-bold
                    text-gray-900
                    "

                    >


                        ⚡ TestForge AI


                    </h1>





                    <p

                    className="
                    text-xs
                    text-gray-500
                    "

                    >


                        QA Automation Platform


                    </p>





                </div>




            </div>













            {/* NAVIGATION */}



            <nav

            className="
            flex-1

            p-3

            overflow-y-auto
            "

            >






            {


                menu.map(


                    (item)=>{



                        const Icon = item.icon;





                        return (




                            <NavLink


                            key={item.path}


                            to={item.path}



                            className={({isActive})=>


                            `


                            flex

                            items-center

                            gap-3


                            px-4

                            py-3


                            rounded-lg


                            text-sm


                            mb-1


                            transition



                            ${


                            isActive


                            ?


                            "bg-blue-600 text-white shadow"


                            :


                            "text-gray-600 hover:bg-gray-100"


                            }


                            `


                            }


                            >






                                <Icon size={18}/>






                                <span>


                                    {item.name}


                                </span>






                            </NavLink>





                        );



                    }


                )


            }








            </nav>














            {/* USER */}



            <div

            className="
            border-t

            p-4
            "

            >






                <div

                className="
                bg-gray-50

                rounded-xl

                p-3

                mb-3
                "

                >






                    <p

                    className="
                    text-sm
                    font-semibold
                    "

                    >


                        Jayarani


                    </p>







                    <p

                    className="
                    text-xs
                    text-gray-500
                    "

                    >


                        QA Engineer


                    </p>








                </div>












                <button



                onClick={logout}



                className="
                flex

                items-center

                gap-3


                w-full


                px-3

                py-2


                rounded-lg


                text-sm


                text-red-600


                hover:bg-red-50
                "


                >






                    <LogOut size={18}/>





                    Logout






                </button>










            </div>









        </aside>




    );



}





export default Sidebar;