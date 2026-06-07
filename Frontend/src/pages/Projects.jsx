import ProjectCard from "../components/ProjectCard";


function Projects(){


const projects=[

{
name:"Food Delivery Testing",
description:"Spring Boot application testing",
technology:"Spring Boot + React"
},

{
name:"Ecommerce QA",
description:"Automation test platform",
technology:"MERN"
}

];


return (

<div className="
min-h-screen
bg-black
p-10
">


<h1 className="
text-white
text-3xl
font-bold
">

Projects

</h1>


<button className="
bg-blue-600
text-white
px-5
py-3
rounded-lg
mt-6
">

+ Create Project

</button>



<div className="
grid
grid-cols-3
gap-6
mt-10
">


{

projects.map(

(project,index)=>(


<ProjectCard

key={index}

{...project}

/>

)

)

}


</div>


</div>

);

}


export default Projects;