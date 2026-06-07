import { Outlet } from "react-router-dom";

import Sidebar from "../components/Sidebar";

import Header from "../components/Header";



function DashboardLayout(){


return(

<div className="min-h-screen bg-gray-50">


<Sidebar/>


<div className="ml-64 max-lg:ml-0">


<Header/>


<main className="p-6">


<Outlet/>


</main>


</div>


</div>

);


}


export default DashboardLayout;