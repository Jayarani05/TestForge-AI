import { NavLink } from "react-router-dom";


import {

    LayoutDashboard,
    FolderKanban,
    Bot,
    PlayCircle,
    Github,
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
            name:"AI Generator",
            path:"/generate",
            icon:Bot
        },


        {
            name:"Execution",
            path:"/execution",
            icon:PlayCircle
        },


        {
            name:"Repository",
            path:"/repository",
            icon:Github
        },


        {
            name:"Self Healing",
            path:"/healing",
            icon:Wrench
        },


        {
            name:"CI/CD",
            path:"/cicd",
            icon:Rocket
        },


        {
            name:"Export",
            path:"/export",
            icon:FileDown
        },


        {
            name:"Settings",
            path:"/settings",
            icon:Settings
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
            flex
            items-center
            px-6
            border-b
            "
            >


                <div>


                    <h1
                    className="
                    text-xl
                    font-bold
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










            {/* MENU */}



            <nav
            className="
            flex-1
            p-4
            "
            >




                {

                menu.map((item)=>{


                    const Icon=item.icon;



                    return(


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
                    rounded-xl
                    mb-2
                    text-sm
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



                        {item.name}



                    </NavLink>



                    )


                })


                }





            </nav>









            {/* PROFILE */}


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
                    font-medium
                    text-sm
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
                gap-2
                text-red-600
                text-sm
                w-full
                p-3
                rounded-lg
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