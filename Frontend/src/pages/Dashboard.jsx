import {

    useEffect,
    useState

} from "react";


import {

    FolderKanban,
    TestTube,
    PlayCircle,
    Bug

} from "lucide-react";


import api from "../api/axios";


import StatCard from "../components/ui/StatCard";





function Dashboard(){



const [dashboard,setDashboard] = useState(null);


const [loading,setLoading] = useState(true);





useEffect(()=>{


    loadDashboard();


},[]);







const loadDashboard = async()=>{


try{


const response = await api.get(

    "/dashboard/"

);



setDashboard(

    response.data

);



}

catch(error){


console.log(error);


}



setLoading(false);


};








if(loading){


return(

<div className="text-gray-500">

Loading dashboard...

</div>

);


}









return(

<div>


<h1 className="text-2xl font-bold mb-2">

Dashboard

</h1>



<p className="text-gray-500 mb-6">

Welcome back to TestForge AI

</p>









<div className="
grid
grid-cols-4
gap-5
mb-8
">





<StatCard

title="Projects"

value={dashboard.projects}

icon={FolderKanban}

/>




<StatCard

title="Generated Tests"

value={dashboard.generated_tests}

icon={TestTube}

/>




<StatCard

title="Executions"

value={dashboard.executions}

icon={PlayCircle}

/>




<StatCard

title="Bugs"

value={dashboard.bugs}

icon={Bug}

/>





</div>









<div className="
bg-white
border
rounded-xl
p-6
shadow-sm
">



<h2 className="font-semibold mb-4">

Recent Activity

</h2>





{

dashboard.recent_activity.length > 0

?

dashboard.recent_activity.map(

(item)=>(


<div

key={item.id}

className="
border-b
py-3
"

>


{item.story}


</div>


)

)


:


<div className="text-gray-400">

No activity yet

</div>


}





</div>







</div>


);


}




export default Dashboard;