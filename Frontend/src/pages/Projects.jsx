import { useEffect, useState } from "react";

import api from "../api/axios";

import ProjectCard from "../components/ProjectCard";


function Projects(){


const [projects,setProjects] = useState([]);


const [form,setForm] = useState({

name:"",

description:"",

technology:""

});




useEffect(()=>{

loadProjects();

},[]);




const loadProjects = async()=>{


const response = await api.get(

"/projects"

);


setProjects(response.data);


};





const createProject = async()=>{


await api.post(

"/projects",

form

);


setForm({

name:"",
description:"",
technology:""

});


loadProjects();


};





return (

<div className="min-h-screen bg-black p-10">


<h1 className="text-white text-3xl font-bold">

Projects

</h1>



<div className="mt-8 space-y-4">


<input

placeholder="Project Name"

className="bg-gray-900 text-white p-3 rounded w-full"

value={form.name}

onChange={(e)=>

setForm({

...form,

name:e.target.value

})

}

/>



<input

placeholder="Description"

className="bg-gray-900 text-white p-3 rounded w-full"

value={form.description}

onChange={(e)=>

setForm({

...form,

description:e.target.value

})

}

/>



<input

placeholder="Technology"

className="bg-gray-900 text-white p-3 rounded w-full"

value={form.technology}

onChange={(e)=>

setForm({

...form,

technology:e.target.value

})

}

/>




<button

onClick={createProject}

className="bg-blue-600 text-white px-6 py-3 rounded"

>

Create Project

</button>


</div>





<div className="
grid
grid-cols-3
gap-6
mt-10
">


{


projects.map(

(project)=>(


<ProjectCard

key={project.id}

name={project.name}

description={project.description}

technology={project.technology}

/>

)

)

}


</div>


</div>

);


}


export default Projects;