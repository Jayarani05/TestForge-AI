import { useEffect, useState } from "react";

import {
    FolderKanban,
    Trash,
    Edit
} from "lucide-react";

import api from "../api/axios";


function Projects(){


const [projects,setProjects] = useState([]);

const [name,setName] = useState("");

const [description,setDescription] = useState("");

const [technology,setTechnology] = useState("");

const [editId,setEditId] = useState(null);



useEffect(()=>{

    loadProjects();

},[]);




const loadProjects = async()=>{


try{

const response = await api.get(
    "/projects/"
);


setProjects(
    response.data
);


}
catch(error){

console.log(error);

}


};





const saveProject = async()=>{


try{


const data = {

    name,
    description,
    technology

};



if(editId){


await api.put(

`/projects/${editId}`,

data

);


}


else{


await api.post(

"/projects/create",

data

);


}




setName("");

setDescription("");

setTechnology("");

setEditId(null);



loadProjects();


}

catch(error){


console.log(error);


alert("Operation failed");


}


};






const editProject = (project)=>{


setEditId(project.id);


setName(project.name);


setDescription(project.description);


setTechnology(project.technology);


};








const deleteProject = async(id)=>{


if(!confirm("Delete this project?")){

return;

}



await api.delete(

`/projects/${id}`

);



loadProjects();



};










return(

<div>


<h1 className="text-2xl font-bold mb-6">

Projects

</h1>







<div className="
bg-white
border
rounded-xl
p-5
mb-6
">


<input

value={name}

onChange={(e)=>setName(e.target.value)}

placeholder="Project name"

className="border p-3 rounded-lg w-full mb-3"

/>




<input

value={description}

onChange={(e)=>setDescription(e.target.value)}

placeholder="Description"

className="border p-3 rounded-lg w-full mb-3"

/>





<input

value={technology}

onChange={(e)=>setTechnology(e.target.value)}

placeholder="Technology"

className="border p-3 rounded-lg w-full mb-3"

/>





<button

onClick={saveProject}

className="
bg-blue-600
text-white
px-5
py-3
rounded-lg
"

>


{

editId

?

"Update Project"

:

"Create Project"

}


</button>


</div>








<div className="
grid
grid-cols-3
gap-5
">


{

projects.map(

(project)=>(


<div

key={project.id}

className="
bg-white
border
rounded-xl
p-5
shadow-sm
"

>



<FolderKanban/>


<h2 className="font-bold mt-3">


{project.name}


</h2>



<p className="text-gray-500">


{project.description}


</p>




<p className="text-sm mt-2">


{project.technology}


</p>






<div className="flex gap-3 mt-5">



<button

onClick={()=>editProject(project)}

className="text-blue-600"

>

<Edit/>


</button>






<button

onClick={()=>deleteProject(project.id)}

className="text-red-600"

>


<Trash/>


</button>



</div>





</div>


)

)

}


</div>



</div>

);


}



export default Projects;