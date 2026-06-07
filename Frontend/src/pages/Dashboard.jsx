import {

FolderKanban,
TestTube,
PlayCircle,
Bug,
Bot

} from "lucide-react";


import StatCard from "../components/ui/StatCard";




function Dashboard(){


return (

<div>


{/* HEADER */}


<div
className="
mb-6
"
>


<h1
className="
text-2xl
font-bold
"
>

Welcome back, Jayarani 👋

</h1>


<p
className="
text-gray-500
"
>

Manage your AI powered QA automation workspace

</p>


</div>






{/* STATS */}


<div
className="
grid
grid-cols-4
gap-5
mb-6
"
>


<StatCard

title="Total Projects"

value="24"

icon={FolderKanban}

change="+12% from last month"

/>


<StatCard

title="Tests Generated"

value="3,562"

icon={TestTube}

change="+19% from last month"

/>


<StatCard

title="Executions"

value="1,287"

icon={PlayCircle}

change="+8% from last month"

/>


<StatCard

title="Bugs Found"

value="182"

icon={Bug}

change="-6% from last month"

/>


</div>









<div
className="
grid
grid-cols-3
gap-5
"
>




{/* PROJECTS */}


<div
className="
bg-white
border
rounded-xl
p-5
col-span-2
"
>


<h2
className="
font-semibold
mb-4
"
>

Recent Projects

</h2>




{

[

"E-Commerce Platform",

"Mobile Banking App",

"Inventory Management"

].map(

(project)=>(


<div

key={project}

className="
flex
justify-between
border-b
py-3
"

>


<div>


<p className="font-medium">

{project}

</p>


<p className="text-sm text-gray-500">

Updated recently

</p>


</div>


<span
className="
text-green-600
text-sm
"
>

Active

</span>



</div>


)

)

}



</div>










{/* AGENTS */}


<div
className="
bg-white
border
rounded-xl
p-5
"
>



<h2
className="
font-semibold
mb-4
flex
gap-2
items-center
"
>


<Bot size={18}/>


AI Agents


</h2>




{

[

"Generator Agent",

"Execution Agent",

"Bug Analyzer",

"Self Healing Agent"

].map(

(agent)=>(


<div

key={agent}

className="
flex
justify-between
py-3
"

>


<span>

{agent}

</span>


<span className="text-green-600">

Online

</span>



</div>


)

)

}




</div>




</div>




</div>

);


}


export default Dashboard;