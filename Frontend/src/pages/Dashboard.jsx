import { useEffect, useState } from "react";

import api from "../api/axios";

import StatCard from "../components/StatCard";


function Dashboard(){


const [data,setData] = useState(null);



useEffect(()=>{


loadDashboard();


},[]);





const loadDashboard = async()=>{


try{


const response = await api.get(

"/dashboard"

);


setData(

response.data

);


}

catch(error){


console.log(error);


}


};





if(!data){


return (

<div className="bg-black min-h-screen text-white p-10">

Loading...

</div>

);

}





return (

<div className="min-h-screen bg-black p-10">


<h1 className="text-white text-4xl font-bold">

Welcome {data.user.name} 👋

</h1>



<div className="
grid
grid-cols-4
gap-6
mt-10
">


<StatCard

title="Projects"

value={
data.analytics.total_projects
}

/>


<StatCard

title="Generated Tests"

value={
data.analytics.total_generations
}

/>


<StatCard

title="Executions"

value={
data.analytics.total_executions
}

/>


<StatCard

title="Bugs Found"

value={
data.analytics.bugs_found
}

/>


</div>


</div>

);


}


export default Dashboard;