import { useEffect, useState } from "react";

import {
    Bot,
    Sparkles,
    Cpu,
    Database,
    FileText,
    CheckCircle,
    XCircle,
    Shield,
    AlertTriangle
} from "lucide-react";

import api from "../api/axios";



function TestCard({test}){

return(

<div className="
border
rounded-xl
p-4
mb-3
shadow-sm
bg-white
">

<div className="
flex
justify-between
items-center
">

<b>
{test.id}
</b>


<span className="
text-sm
font-semibold
">

{test.priority}

</span>


</div>


<p className="
text-sm
mt-2
text-gray-600
">

{test.title}

</p>


</div>

);

}






function TestGenerator(){


const [projects,setProjects]=useState([]);

const [projectId,setProjectId]=useState("");

const [story,setStory]=useState("");

const [language,setLanguage]=useState("python");

const [framework,setFramework]=useState("selenium");

const [result,setResult]=useState(null);

const [loading,setLoading]=useState(false);




const frameworks={

python:[
"selenium",
"pytest",
"playwright"
],

java:[
"selenium",
"junit",
"testng"
],

javascript:[
"playwright",
"jest",
"cypress"
]

};





useEffect(()=>{

loadProjects();

},[]);





const loadProjects=async()=>{

try{

const res=await api.get(
"/projects/"
);


setProjects(res.data);


if(res.data.length>0){

setProjectId(
res.data[0].id
);

}


}

catch(err){

console.log(err);

}

};







const generateTests=async()=>{


if(!projectId){

alert("Select project");

return;

}


if(!story){

alert("Enter requirement");

return;

}



try{


setLoading(true);



const res=await api.post(

"/tests/generate",

{

project_id:Number(projectId),

user_story:story,

output_type:"test_cases",

language,

framework,

project_context:{}

}

);



setResult(

res.data.agent_result

);



}

catch(err){

console.log(err);

alert("Generation failed");

}



setLoading(false);


};










return(

<div>


<h1 className="
text-2xl
font-bold
">

AI Test Generator

</h1>


<p className="
text-gray-500
mb-6
">

Generate QA test cases using AI Agents

</p>








<div className="
grid
grid-cols-2
gap-6
">








{/* INPUT */}


<div className="
border
rounded-xl
p-6
bg-white
">


<h2 className="
font-bold
flex
gap-2
mb-5
">

<Sparkles/>

Requirement

</h2>





<select

value={projectId}

onChange={(e)=>setProjectId(e.target.value)}

className="
border
p-3
rounded-lg
w-full
mb-4
"

>


{
projects.map(p=>(

<option

key={p.id}

value={p.id}

>

{p.name}

</option>

))

}


</select>






<textarea

value={story}

onChange={(e)=>setStory(e.target.value)}

placeholder="Enter user story"

className="
border
rounded-lg
p-4
w-full
h-72
"

/>








<div className="
grid
grid-cols-2
gap-4
mt-4
">



<select

value={language}

onChange={(e)=>{

let value=e.target.value;

setLanguage(value);

setFramework(
frameworks[value][0]
);

}}

className="border p-3"

>


<option value="python">
Python
</option>

<option value="java">
Java
</option>

<option value="javascript">
Javascript
</option>


</select>






<select

value={framework}

onChange={(e)=>setFramework(e.target.value)}

className="border p-3"

>


{

frameworks[language].map(f=>(

<option key={f}>

{f}

</option>

))

}


</select>


</div>








<button

onClick={generateTests}

className="
mt-5
bg-blue-600
text-white
px-5
py-3
rounded-lg
flex
gap-2
"

>

<Bot/>


{
loading
?
"Generating..."
:
"Generate Tests"
}


</button>



</div>









{/* OUTPUT */}


<div className="
border
rounded-xl
p-6
bg-white
overflow-auto
h-[700px]
">


<h2 className="
font-bold
mb-5
">

Generated Output

</h2>





{

result

?


<div className="space-y-5">









<div className="
grid
grid-cols-2
gap-4
">



<div className="
border
rounded-xl
p-4
">


<Cpu/>


<p className="text-gray-500">

Selected AI

</p>


<b>

{
result.judge_result?.selected_model
||
"AI Agent"
}

</b>


</div>







<div className="
border
rounded-xl
p-4
">


<Database/>


<p className="text-gray-500">

Framework

</p>


<b>

{framework}

</b>


</div>


</div>









{/* REQUIREMENTS */}



<div className="
border
rounded-xl
p-5
bg-gray-50
">


<h3 className="
font-bold
flex
gap-2
mb-3
">

<FileText/>

Requirement Analysis

</h3>





<ul className="
list-disc
ml-5
text-sm
">

{

result.requirement_intelligence
?.functional_requirements
?.map((item,i)=>(

<li key={i}>

{item}

</li>

))

}

</ul>







<h3 className="
font-bold
mt-5
flex
gap-2
">

<AlertTriangle/>

Risks

</h3>


{

result.requirement_intelligence
?.risk_analysis
?.risks
?.map((risk,i)=>(


<div

key={i}

className="
bg-red-50
p-3
rounded-lg
mt-2
text-sm
"

>

{risk}

</div>


))

}


</div>









{/* TEST SECTIONS */}


{

[

[
"positive_tests",
<CheckCircle/>,
"Positive Tests"
],


[
"negative_tests",
<XCircle/>,
"Negative Tests"
],


[
"security_tests",
<Shield/>,
"Security Tests"
],


[
"edge_cases",
<AlertTriangle/>,
"Edge Cases"
]


].map(section=>(


<div key={section[0]}>


<h3 className="
font-bold
flex
gap-2
mb-3
">

{section[1]}

{section[2]}

</h3>



{

result.generated_test_cases
?.result
?.[section[0]]
?.map(test=>(

<TestCard

key={test.id}

test={test}

/>

))

}


</div>


))

}






</div>


:


<div className="
h-96
flex
items-center
justify-center
text-gray-400
">

AI generated tests appear here

</div>


}



</div>



</div>


</div>

);

}


export default TestGenerator;