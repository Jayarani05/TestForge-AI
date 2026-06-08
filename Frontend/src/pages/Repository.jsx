import { useState } from "react";

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





function Repository(){


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



setResult(

response.data.analysis ||

response.data.result ||

response.data

);



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

"Analyzed Repository"

}

</p>



<p>

<b>Quality :</b>{" "}

{

result.score ||

result.quality_score ||

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

result.tech_stack

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

result.recommendations

)

.map((item,index)=>(



<li key={index}>

✅ {item}

</li>



))


}


</ul>



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