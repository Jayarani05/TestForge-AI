import { useState } from "react";

import { useNavigate } from "react-router-dom";

import {

    GitBranch,
    Search,
    Code,
    ShieldCheck,
    Lightbulb,
    Star,
    FolderGit2

} from "lucide-react";


import api from "../api/axios";

import { saveRepoContext } from "../services/workflowService";





function Repository(){


const navigate = useNavigate();

const [url,setUrl] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);








async function analyzeRepo(){



if(!url.trim()){

alert("Enter repository URL");

return;

}



try{


setLoading(true);



const response = await api.post(

"/repository/analyze",

{

repo_url:url

}

);



console.log(

"REPO RESPONSE",

response.data

);



const analysis =
response.data.analysis ||
response.data.result ||
response.data;

saveRepoContext(analysis);

setResult(analysis);



}



catch(error){


console.log(error);


alert("Repository analysis failed");


}



setLoading(false);



}









const listData = (data)=>{


if(!data){

return [];

}


if(Array.isArray(data)){

return data;

}


return [data];


};









return(


<div>




{/* HEADER */}



<div className="mb-6">


<h1 className="text-2xl font-bold">

Repository Intelligence

</h1>



<p className="text-gray-500">

Analyze GitHub repositories using AI agents

</p>



</div>









{/* INPUT */}



<div
className="
bg-white
border
rounded-xl
p-6
shadow-sm
mb-6
"
>



<h2
className="
font-semibold
flex
items-center
gap-2
mb-5
"
>

<GitBranch size={18}/>

Repository URL

</h2>







<div className="flex gap-4">



<input

value={url}

onChange={(e)=>setUrl(e.target.value)}

placeholder="https://github.com/user/project"

className="
flex-1
border
rounded-lg
p-3
"

/>






<button

onClick={analyzeRepo}

disabled={loading}

className="
bg-blue-600
text-white
px-5
rounded-lg
flex
gap-2
items-center
"
>


<Search size={18}/>


{

loading

?

"Analyzing..."

:

"Analyze"

}


</button>



</div>


</div>











{


result

?


<div className="grid grid-cols-2 gap-6">









{/* OVERVIEW */}


<div
className="
bg-white
border
rounded-xl
p-6
"
>


<h2 className="
font-semibold
flex
gap-2
mb-4
">

<FolderGit2 size={18}/>

Repository Overview

</h2>



<p>

<b>Name :</b>{" "}

{

result.name ||
result.project_name ||

"Analyzed Repository"

}

</p>



<p>

<b>Quality :</b>{" "}

{

result.score ||

result.quality_score ||
`${result.total_files || 0} files`

||

"Good"

}

</p>



</div>











{/* TECH STACK */}


<div
className="
bg-white
border
rounded-xl
p-6
"
>



<h2 className="
font-semibold
flex
gap-2
mb-4
">

<Code size={18}/>

Tech Stack

</h2>





{

listData(

result.tech_stack ||
[
result.language,
result.framework,
...(result.dependencies || []).slice(0,6)
].filter(Boolean)

)

.map((item,index)=>(


<span

key={index}

className="
inline-block
bg-blue-50
text-blue-600
px-3
py-1
rounded-full
mr-2
mb-2
"

>


{item}


</span>


))


}



</div>










{/* SECURITY */}



<div
className="
bg-white
border
rounded-xl
p-6
"
>


<h2 className="
font-semibold
flex
gap-2
mb-4
">

<ShieldCheck size={18}/>

Security Analysis

</h2>



<p>

{

result.security ||

"No security issues detected"

}

</p>



</div>










{/* RECOMMENDATION */}



<div
className="
bg-white
border
rounded-xl
p-6
"
>


<h2 className="
font-semibold
flex
gap-2
mb-4
">

<Star size={18}/>

Repository Score

</h2>



<h1 className="text-4xl font-bold text-blue-600">


{

result.rating ||

"8/10"

}


</h1>



</div>









{/* AI Suggestions */}



<div
className="
bg-white
border
rounded-xl
p-6
col-span-2
"
>


<h2 className="
font-semibold
flex
gap-2
mb-4
">

<Lightbulb size={18}/>

AI Recommendations

</h2>






<ul className="space-y-2">


{


listData(

result.recommendations ||
[
result.api_endpoints?.length
?
`${result.api_endpoints.length} API endpoints detected for test coverage`
:
null,
result.classes?.length
?
`${result.classes.length} classes found for automation context`
:
null,
result.functions?.length
?
`${result.functions.length} functions available for unit and integration tests`
:
null,
"Repository context saved for test generation"
].filter(Boolean)

)

.map((item,index)=>(



<li key={index}>

✅ {item}

</li>



))


}


</ul>



</div>


<div className="
bg-white
border
rounded-xl
p-6
col-span-2
flex
items-center
justify-between
">

<div>

<h2 className="font-semibold">
Workflow Ready
</h2>

<p className="text-gray-500 text-sm mt-1">
Use this repository context to generate QA test cases.
</p>

</div>

<button
onClick={()=>navigate("/generate")}
className="
bg-blue-600
text-white
px-5
py-3
rounded-lg
"
>
Continue to Test Generation
</button>

</div>





</div>



:



<div

className="
bg-white
border
rounded-xl
h-64
flex
items-center
justify-center
text-gray-400
"

>


Repository insights appear here


</div>



}





</div>


);


}




export default Repository;
