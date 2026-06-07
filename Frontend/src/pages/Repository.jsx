import { useState } from "react";

import api from "../api/axios";


function Repository(){


const [url,setUrl] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);




const analyzeRepo = async()=>{


try{


setLoading(true);



const response = await api.post(

"/repository/analyze",

{

repo_url:url

}

);



console.log(response.data);


setResult(

response.data.repository_analysis

);


}

catch(error){


console.log(

error.response?.data

);


alert("Repository analysis failed");


}



setLoading(false);


};





return (

<div className="min-h-screen bg-black p-10">


<h1 className="text-white text-3xl font-bold">

Repository Intelligence

</h1>




<input


value={url}


onChange={(e)=>setUrl(e.target.value)}


placeholder="Enter GitHub repository URL"


className="
w-full
bg-gray-900
text-white
p-4
rounded-xl
mt-8
"


/>




<button


onClick={analyzeRepo}


className="
bg-blue-600
text-white
px-6
py-3
rounded-lg
mt-5
"


>


{

loading
?
"Analyzing..."
:
"Analyze Repository"

}


</button>






{

result && (


<div className="
bg-gray-900
text-white
rounded-xl
p-6
mt-8
">


<h2 className="text-xl">

Project Type:

</h2>


<p>

{result.project_type}

</p>





<h2 className="text-xl mt-5">

Languages

</h2>


<ul>


{

result.languages?.map(

(x,i)=>(

<li key={i}>

{x}

</li>

)

)

}


</ul>





<h2 className="text-xl mt-5">

Features

</h2>



<ul>


{

result.features?.map(

(x,i)=>(

<li key={i}>

{x}

</li>

)

)

}


</ul>




</div>

)

}



</div>


);


}


export default Repository;