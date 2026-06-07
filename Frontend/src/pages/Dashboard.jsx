import StatCard from "../components/StatCard";


function Dashboard(){


const analytics={

projects:10,

tests:250,

executions:100,

bugs:25

};



return (

<div className="min-h-screen bg-black p-10">


<h1 className="text-white text-3xl font-bold">

Welcome Back 👋

</h1>


<div className="
grid
grid-cols-4
gap-6
mt-10
">


<StatCard

title="Projects"

value={analytics.projects}

/>


<StatCard

title="Generated Tests"

value={analytics.tests}

/>


<StatCard

title="Executions"

value={analytics.executions}

/>


<StatCard

title="Bugs Found"

value={analytics.bugs}

/>


</div>


</div>

);


}


export default Dashboard;