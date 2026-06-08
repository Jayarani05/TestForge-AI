import { useState } from "react";

import {
    Bug,
    AlertTriangle,
    Lightbulb,
    CheckCircle,
    Wrench
} from "lucide-react";


import api from "../api/axios";



function BugAnalyzer(){


const [logs,setLogs] = useState("");

const [analysis,setAnalysis] = useState(null);

const [loading,setLoading] = useState(false);





async function analyzeBug(){


if(!logs.trim()){

    alert("Paste failure logs");

    return;

}



try{


setLoading(true);



const response = await api.post(

"/bugs/analyze",

{

execution_result:{

passed:false,

error:logs

}

}

);




let data = response.data.analysis;


// handle raw llm response

if(data?.raw_analysis){

try{

data = JSON.parse(data.raw_analysis);

}

catch(e){

data = {

root_cause:data.raw_analysis

}

}

}




setAnalysis(data);



}


catch(error){


console.log(error);


alert("Bug analysis failed");


}



setLoading(false);


}










return (

<div>


{/* HEADER */}


<div className="mb-6">


<h1 className="text-2xl font-bold">

AI Bug Analyzer

</h1>


<p className="text-gray-500">

Analyze failed executions and find root causes

</p>


</div>










<div className="grid grid-cols-2 gap-6">







{/* INPUT */}


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

<Bug size={18}/>

Failure Logs

</h2>






<textarea


value={logs}


onChange={(e)=>setLogs(e.target.value)}


placeholder="Paste failed test logs..."


className="
w-full
h-96
border
rounded-lg
p-5
font-mono
resize-none
"


/>








<button


onClick={analyzeBug}


className="
mt-5
bg-blue-600
text-white
px-5
py-3
rounded-lg
"

>


{

loading

?

"Analyzing..."

:

"Analyze Bug"

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



<h2

className="
font-semibold
mb-5
flex
gap-2
items-center
"

>

<Lightbulb size={18}/>

AI Diagnosis

</h2>







{

analysis

?



<div className="space-y-5">





{/* SEVERITY */}


<div

className="
border
rounded-xl
p-4
flex
items-center
gap-3
"

>


<AlertTriangle

className="text-red-500"

/>


<div>


<p className="text-gray-500 text-sm">

Severity

</p>


<h3 className="
font-bold
text-red-600
">

{

analysis.severity ||

analysis.risk ||

"HIGH"

}

</h3>


</div>



</div>








{/* ROOT CAUSE */}


<div

className="
border
rounded-xl
p-4
"

>


<h3 className="
font-semibold
flex
gap-2
mb-2
">

<Bug size={18}/>

Root Cause

</h3>


<p className="text-gray-600">


{

analysis.root_cause ||

analysis.cause ||

"Not detected"

}


</p>


</div>








{/* FIX */}


<div

className="
border
rounded-xl
p-4
"

>


<h3 className="
font-semibold
flex
gap-2
mb-2
">

<Wrench size={18}/>

Possible Fix

</h3>


<p className="text-gray-600">


{

analysis.possible_fix ||

analysis.fix ||

analysis.solution ||

"Not available"

}


</p>


</div>








{/* RECOMMENDATION */}


<div

className="
border
rounded-xl
p-4
"

>


<h3 className="
font-semibold
flex
gap-2
mb-2
">

<CheckCircle size={18}/>

QA Recommendation


</h3>



<p className="text-gray-600">


{

analysis.qa_recommendation ||

analysis.recommendation ||

analysis.recommendations ||

"Add regression test coverage"

}


</p>



</div>






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

Bug analysis appears here


</div>



}




</div>






</div>




</div>


);


}



export default BugAnalyzer;