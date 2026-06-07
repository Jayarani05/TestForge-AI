import { Outlet } from "react-router-dom";


import Sidebar from "../components/Sidebar";

import Header from "../components/Header";





function DashboardLayout(){



    return(


        <div
        className="
        flex
        bg-gray-50
        min-h-screen
        "
        >



            <Sidebar />





            <div
            className="
            ml-64
            flex-1
            "
            >



                <Header />



                <main
                className="
                p-6
                "
                >


                    <Outlet />


                </main>



            </div>




        </div>


    );


}



export default DashboardLayout;