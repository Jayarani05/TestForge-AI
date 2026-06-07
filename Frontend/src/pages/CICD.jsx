import { useState } from "react";

import {

    Rocket,
    Copy,
    Settings

} from "lucide-react";


import api from "../api/axios";



function CICD(){


const [language,setLanguage] = useState("python");

const [framework,setFramework] = useState("selenium");

const [tool,setTool] = useState("github actions");

const [pipeline,setPipeline] = useState(null);

const [loading,setLoading] = useState(false);






async function generatePipeline(){


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



setPipeline(

response.data

);



}


catch(error){


console.log(error);


alert("Pipeline generation failed");


}



setLoading(false);



}








return(

<div>


{/* HEADER */}


<div className="mb-6">


<h1 className="text-2xl font-bold">

CI/CD Generator

</h1>


<p className="text-gray-500">

Generate automated DevOps pipelines using AI

</p>


</div>









<div className="grid grid-cols-2 gap-6">







{/* SETTINGS */}


<div
className="
bg-white
border
rounded-xl
p-6
shadow-sm
"
>


<h2 className="
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

Language

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

Python

</option>


<option value="java">

Java

</option>


<option value="javascript">

JavaScript

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


<option value="selenium">

Selenium

</option>


<option value="playwright">

Playwright

</option>


<option value="pytest">

PyTest

</option>


</select>










<label className="text-sm">

CI/CD Tool

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











<button

onClick={generatePipeline}

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









{/* OUTPUT */}


<div
className="
bg-white
border
rounded-xl
p-6
shadow-sm
"
>



<div className="
flex
justify-between
mb-5
"
>


<h2 className="font-semibold">

Generated Pipeline

</h2>



<button

className="
flex
gap-2
text-blue-600
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


<pre

className="
bg-gray-900
text-green-400
rounded-lg
p-5
h-96
overflow-auto
text-sm
"

>


{

pipeline.pipeline_code ||

JSON.stringify(

pipeline,

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


Generated YAML appears here


</div>



}







</div>





</div>





</div>

);


}




export default CICD;