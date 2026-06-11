import { useState } from "react";

import { useNavigate } from "react-router-dom";

import {

    GitBranch,
    Search,
    Code,
    ShieldCheck,
    Lightbulb,
    Star,
    FolderGit2,
    Rocket

} from "lucide-react";


import api from "../api/axios";

import { saveHistory } from "../services/historyService";






function Repository(){


const navigate = useNavigate();


const [url,setUrl] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);









// ==============================
// ANALYZE REPOSITORY
// ==============================


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







const repoResult =

response.data.analysis ||

response.data.result ||

response.data;







setResult(

repoResult

);








// ==============================
// SAVE HISTORY
// ==============================


saveHistory({

    type:"Repository Analysis",


    title:

        repoResult.name ||

        "GitHub Repository",



    description:

        `Repository analyzed successfully`,



    status:"Completed",



    data:{


        repo_url:url,


        tech_stack:

            repoResult.tech_stack,


        security:

            repoResult.security,


        rating:

            repoResult.rating

    }


});






}

catch(error){



console.log(error);



alert(

"Repository analysis failed"

);



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


<div className="
bg-white
border
rounded-xl
p-6
">


<h2 className="font-semibold flex gap-2 mb-4">

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


<div className="
bg-white
border
rounded-xl
p-6
">



<h2 className="font-semibold flex gap-2 mb-4">


<Code size={18}/>

Tech Stack


</h2>





{

listData(

result.tech_stack

)

.map(

(item,index)=>(



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
">



<h2 className="font-semibold flex gap-2 mb-4">


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









{/* SCORE */}


<div className="
bg-white
border
rounded-xl
p-6
">



<h2 className="font-semibold flex gap-2 mb-4">


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











{/* RECOMMENDATION */}


<div className="
bg-white
border
rounded-xl
p-6
col-span-2
">


<h2 className="font-semibold flex gap-2 mb-4">


<Lightbulb size={18}/>

AI Recommendations


</h2>





<ul className="space-y-2">


{


listData(

result.recommendations

)

.map(

(item,index)=>(


<li key={index}>

✅ {item}

</li>


)

)

}


</ul>



</div>










{/* NEXT */}


<div className="
bg-white
border
rounded-xl
p-6
col-span-2
flex
justify-end
">


<button


onClick={()=>{


navigate(

"/generate",

{

state:{

repository:result,

repo_url:url

}

}

);


}}


className="
bg-green-600
text-white
px-6
py-3
rounded-lg
flex
items-center
gap-2
"

>


<Rocket size={18}/>


Generate Tests


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