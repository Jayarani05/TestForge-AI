import { useState } from "react";

import {

    GitBranch,
    Search,
    Code,
    ShieldCheck,
    Lightbulb

} from "lucide-react";


import api from "../api/axios";



function Repository(){


const [url,setUrl] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);





async function analyzeRepo(){


try{


setLoading(true);


const response = await api.post(

"/repository/analyze",

{

repo_url:url

}

);


setResult(response.data);


}


catch(error){

console.log(error);

alert("Repository analysis failed");

}


setLoading(false);


}







return(

<div>


{/* HEADER */}


<div className="mb-6">


<h1 className="text-2xl font-bold">

Repository Intelligence

</h1>


<p className="text-gray-500">

Analyze source code repositories using AI

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


<h2 className="
font-semibold
flex
items-center
gap-2
mb-5
">

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

"Analyzing"

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







{/* TECH */}


<div className="
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
"
>

<Code size={18}/>

Tech Stack

</h2>




{


(result.tech_stack || []).map(

(item)=>(

<span

key={item}

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

)

)

}



</div>









{/* SECURITY */}



<div className="
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
"
>

<ShieldCheck size={18}/>

Security

</h2>



<p>

{

result.security || "No critical issues detected"

}

</p>




</div>









{/* RECOMMENDATIONS */}


<div className="
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
"
>

<Lightbulb size={18}/>

AI Recommendations

</h2>





<pre className="text-sm">

{

JSON.stringify(

result.recommendations,

null,

2

)

}

</pre>





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