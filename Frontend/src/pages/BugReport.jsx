import { useState } from "react";

import {

    Bug,
    AlertTriangle,
    Lightbulb

} from "lucide-react";


import api from "../api/axios";




function BugAnalyzer(){



const [logs,setLogs] = useState("");

const [analysis,setAnalysis] = useState(null);

const [loading,setLoading] = useState(false);






async function analyzeBug(){



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



setAnalysis(

response.data.analysis

);



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


placeholder="Paste failed execution logs here..."


className="
w-full
h-96
bg-gray-900
text-red-300
font-mono
rounded-lg
p-5
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



<div

className="
border
rounded-lg
p-4
"

>


<div

className="
flex
gap-2
items-center
text-red-600
font-semibold
"

>


<AlertTriangle size={18}/>


{

analysis.severity || "HIGH"

}


</div>


</div>









<div>


<h3 className="font-semibold">

Root Cause

</h3>


<p className="text-gray-600">

{

analysis.root_cause

}

</p>


</div>









<div>


<h3 className="font-semibold">

Possible Fix

</h3>


<p className="text-gray-600">

{

analysis.possible_fix

}

</p>


</div>









<div>


<h3 className="font-semibold">

QA Recommendation

</h3>


<p className="text-gray-600">

{

analysis.qa_recommendation

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