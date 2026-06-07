import { useState } from "react";

import {
    Rocket,
    Copy,
    Settings,
    CheckCircle
} from "lucide-react";

import api from "../api/axios";



function CICD(){


const [language,setLanguage] = useState("python");

const [framework,setFramework] = useState("pytest");

const [tool,setTool] = useState("github actions");

const [pipeline,setPipeline] = useState(null);

const [loading,setLoading] = useState(false);






const generatePipeline = async()=>{


try{


setLoading(true);


const response = await api.post(

"/cicd/generate",

{

language,

framework,

tool

}

);



console.log(
    "PIPELINE RESPONSE",
    response.data
);



setPipeline(

response.data.pipeline_code ||
response.data.pipeline ||
response.data

);



}

catch(error){


console.log(error);


alert("Pipeline generation failed");


}



setLoading(false);



};









const getPipelineText = ()=>{


if(!pipeline){

return "";

}



if(typeof pipeline === "string"){

return pipeline;

}



if(pipeline.pipeline_code){

return pipeline.pipeline_code;

}



return JSON.stringify(

pipeline,

null,

2

);


};









const copyPipeline = ()=>{


navigator.clipboard.writeText(

getPipelineText()

);


alert("Copied");


};









return(

<div>



{/* HEADER */}


<div className="mb-6">


<h1 className="text-2xl font-bold">

CI/CD Generator

</h1>


<p className="text-gray-500">

Generate DevOps pipelines using AI

</p>


</div>











<div className="grid grid-cols-2 gap-6">








{/* LEFT */}


<div
className="
bg-white
border
rounded-xl
p-6
shadow-sm
"
>


<h2
className="
font-semibold
flex
gap-2
items-center
mb-5
"
>


<Settings size={18}/>

Pipeline Settings


</h2>










<label className="text-sm">

Project Type

</label>


<select

value={language}

onChange={(e)=>setLanguage(e.target.value)}

className="
w-full
border
rounded-lg
p-3
mt-2
mb-5
"

>


<option value="python">

Python Automation

</option>


<option value="java">

Java Automation

</option>


<option value="javascript">

Javascript Automation

</option>



</select>










<label className="text-sm">

Framework

</label>



<select

value={framework}

onChange={(e)=>setFramework(e.target.value)}

className="
w-full
border
rounded-lg
p-3
mt-2
mb-5
"

>



<option value="pytest">

pytest

</option>


<option value="selenium">

selenium

</option>


<option value="playwright">

playwright

</option>


<option value="junit">

junit

</option>



</select>









<label className="text-sm">

CI Tool

</label>



<select

value={tool}

onChange={(e)=>setTool(e.target.value)}

className="
w-full
border
rounded-lg
p-3
mt-2
mb-5
"

>



<option value="github actions">

GitHub Actions

</option>



<option value="jenkins">

Jenkins

</option>




</select>









<div
className="
bg-blue-50
border
rounded-xl
p-4
text-sm
mb-5
"
>


<b>Configuration</b>


<p>

Language: {language}

</p>


<p>

Framework: {framework}

</p>


<p>

Tool: {tool}

</p>



</div>










<button

onClick={generatePipeline}

disabled={loading}

className="
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


<Rocket size={18}/>


{

loading

?

"Generating..."

:

"Generate Pipeline"

}


</button>







</div>











{/* RIGHT */}



<div
className="
bg-white
border
rounded-xl
p-6
shadow-sm
"
>



<div
className="
flex
justify-between
mb-5
items-center
"
>


<h2
className="
font-semibold
flex
gap-2
"
>


<CheckCircle size={18}/>

Generated Pipeline


</h2>




<button

onClick={copyPipeline}

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

pipeline

?


<div
className="
border
rounded-xl
bg-gray-50
p-5
h-96
overflow-auto
"
>


<pre
className="
text-sm
whitespace-pre-wrap
font-mono
"
>


{

getPipelineText()

}


</pre>


</div>




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


Generated YAML appears here


</div>



}








</div>





</div>





</div>


);


}



export default CICD;