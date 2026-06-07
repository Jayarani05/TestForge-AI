import {

    useState,
    useEffect

} from "react";


import {

    Bot,
    Copy,
    Sparkles

} from "lucide-react";


import api from "../api/axios";





function TestGenerator(){



const [story,setStory] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);



const [projects,setProjects] = useState([]);

const [projectId,setProjectId] = useState("");





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



if(response.data.length > 0){


setProjectId(

    response.data[0].id

);


}



}


catch(error){


console.log(error);


}


};










const generateTests = async()=>{


try{


if(!projectId){


alert(

    "Please create/select a project first"

);


return;


}




setLoading(true);




const response = await api.post(

"/tests/generate",

{


user_story:story,


output_type:"test_cases",


language:"python",


framework:"selenium",


project_context:"",


project_id:Number(

    projectId

)


}

);





setResult(

response.data.agent_result

);



}


catch(error){


console.log(error);


alert(

"Generation failed"

);


}




setLoading(false);



};









return(

<div>


<div className="mb-6">


<h1 className="text-2xl font-bold">

AI Test Generator

</h1>



<p className="text-gray-500">

Generate QA test cases using AI agents

</p>


</div>







<div className="grid grid-cols-2 gap-6">





<div className="
bg-white
border
rounded-xl
p-6
shadow-sm
">


<h2 className="
font-semibold
flex
gap-2
items-center
mb-5
">


<Sparkles size={18}/>


Requirement


</h2>






<select

value={projectId}

onChange={(e)=>setProjectId(e.target.value)}

className="
w-full
border
rounded-lg
p-3
mb-5
"

>


<option value="">

Select Project

</option>



{


projects.map(

(project)=>(


<option

key={project.id}

value={project.id}

>


{project.name}


</option>


)

)

}


</select>







<textarea

value={story}

onChange={(e)=>setStory(e.target.value)}

placeholder="Enter user story or requirement..."

className="
w-full
h-72
border
rounded-lg
p-4
resize-none
"

/>








<button

onClick={generateTests}

disabled={loading}

className="
mt-5
bg-blue-600
text-white
px-5
py-3
rounded-lg
flex
gap-2
items-center
"

>


<Bot size={18}/>


{

loading ?

"Generating..."

:

"Generate Tests"

}


</button>




</div>








<div className="
bg-white
border
rounded-xl
p-6
shadow-sm
">



<div className="
flex
justify-between
items-center
mb-5
">


<h2 className="font-semibold">

Generated Output

</h2>



<button

className="
text-blue-600
flex
gap-2
text-sm
"

>


<Copy size={16}/>

Copy


</button>


</div>







{

result ?


<pre

className="
bg-gray-900
text-green-400
rounded-lg
p-5
overflow-auto
h-96
text-sm
"

>


{

JSON.stringify(

result,

null,

2

)

}


</pre>


:


<div

className="
h-96
flex
items-center
justify-center
text-gray-400
"

>


AI generated tests appear here


</div>


}




</div>


</div>



</div>


);


}




export default TestGenerator;