import { useState } from "react";

import {

    Play,
    Terminal,
    CheckCircle,
    XCircle

} from "lucide-react";


import api from "../api/axios";




function Execution(){



const [code,setCode] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);






async function runTest(){


try{


setLoading(true);


const response = await api.post(

"/execution/run",

{

code:code,

language:"python",

framework:"selenium",

project_id:1

}

);


setResult(

response.data

);


}

catch(error){


console.log(error);


alert("Execution failed");


}



setLoading(false);


}








return (

<div>




{/* HEADER */}


<div className="mb-6">


<h1 className="text-2xl font-bold">

Test Execution

</h1>


<p className="text-gray-500">

Run automated tests and analyze execution results

</p>


</div>










<div className="grid grid-cols-2 gap-6">








{/* CODE PANEL */}


<div

className="
bg-white
border
rounded-xl
p-6
shadow-sm
"

>


<h2 className="font-semibold mb-4">

Automation Code

</h2>




<textarea


value={code}


onChange={(e)=>setCode(e.target.value)}


placeholder="Paste your Selenium test code here..."


className="
bg-gray-900
text-green-400
font-mono
text-sm
rounded-lg
p-5
w-full
h-96
resize-none
"


/>






<button


onClick={runTest}


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


<Play size={18}/>


{

loading

?

"Running..."

:

"Run Test"


}



</button>






</div>











{/* RESULT PANEL */}



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


<Terminal size={18}/>


Execution Result


</h2>









{

result

?


<div>


<div

className="
flex
items-center
gap-3
mb-5
"

>



{

result.passed

?

<CheckCircle className="text-green-600"/>

:

<XCircle className="text-red-600"/>

}



<h3 className="font-semibold">


{

result.passed

?

"Test Passed"

:

"Test Failed"


}


</h3>



</div>







<pre

className="
bg-gray-900
text-gray-100
rounded-lg
p-5
h-80
overflow-auto
text-sm
"

>


{JSON.stringify(

result,

null,

2

)}


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


Execution results appear here


</div>


}







</div>








</div>







</div>


);


}




export default Execution;