import { useState } from "react";

import { useLocation } from "react-router-dom";


import {
    Play,
    CheckCircle,
    XCircle,
    Clock,
    Bug,
    Activity,
    Wand2
} from "lucide-react";


import api from "../api/axios";







function Execution(){



const location = useLocation();



// RECEIVE GENERATED CODE

const generatedCode =

    location.state?.generated_code || "";





console.log(

    "RECEIVED CODE:",

    generatedCode

);






const [code,setCode] =

    useState(generatedCode);




const [result,setResult] =

    useState(null);




const [loading,setLoading] =

    useState(false);









// ===========================
// RUN EXECUTION
// ===========================


async function runTest(){



if(!code.trim()){


alert(
"No generated code found"
);


return;


}






try{



setLoading(true);





console.log(

"EXECUTION REQUEST",

code

);







const response = await api.post(

"/execution/run",

{

code:code

}

);








console.log(

"EXECUTION RESPONSE",

response.data

);







setResult(

response.data

);



}




catch(error){



console.log(

"EXECUTION ERROR",

error

);



alert(

"Execution failed"

);



}





finally{


setLoading(false);


}




}









return(

<div>






<h1 className="
text-2xl
font-bold
mb-6
">

Test Execution Engine

</h1>









<div className="
grid
grid-cols-2
gap-8
">









{/* LEFT SIDE */}


<div className="
bg-white
border
rounded-xl
p-6
">





<h2 className="
font-bold
mb-4
">

Generated Automation Code

</h2>







<textarea


value={code}


onChange={(e)=>setCode(e.target.value)}


placeholder="Generated automation code appears here"


className="
w-full
h-[450px]
border
rounded-xl
p-5
font-mono
text-sm
resize-none
"


/>








<button


onClick={runTest}


disabled={loading}



className="
mt-5
bg-blue-600
text-white
px-6
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

"Executing..."

:

"Execute Tests"

}



</button>







</div>














{/* RIGHT SIDE */}


<div className="
bg-white
border
rounded-xl
p-6
">







<h2 className="
font-bold
flex
gap-2
mb-5
">


<Activity/>


Execution Result


</h2>








{


result

?




<div>









{/* STATUS */}



<div className="
grid
grid-cols-3
gap-4
mb-6
">









<div className="
border
rounded-xl
p-4
">


<Clock/>


<p>Status</p>



<b>


{

result.execution_result?.status

}


</b>



</div>











<div className="
border
rounded-xl
p-4
">



{

result.execution_result?.passed

?

<CheckCircle className="text-green-600"/>

:

<XCircle className="text-red-600"/>

}



<p>Result</p>



<b>


{

result.execution_result?.passed

?

"PASSED"

:

"FAILED"


}



</b>





</div>









<div className="
border
rounded-xl
p-4
">


<Clock/>


<p>Time</p>


<b>


{

result.execution_result?.execution_time || "-"

}


</b>




</div>





</div>












{/* BUG ANALYZER */}



<div className="
border
rounded-xl
p-5
mb-5
">





<h2 className="
font-bold
flex
gap-2
mb-3
">


<Bug/>


Bug Analyzer Agent


</h2>








{

result.execution_result?.passed


?


<p>

✅ No bugs detected

</p>



:


<div className="space-y-2">



<p>

🐞 Bug detected

</p>





<p>


<b>Severity :</b>{" "}


{

result.bug_analysis?.severity

}


</p>








<p>


<b>Root Cause :</b>{" "}


{

result.bug_analysis?.root_cause

}


</p>








<p>


<b>Possible Fix :</b>{" "}


{

result.bug_analysis?.possible_fix

}


</p>








<p>


<b>Recommendation :</b>{" "}


{

result.bug_analysis?.qa_recommendation

}


</p>





</div>



}







</div>













{/* SELF HEALING */}


{


result.self_healing?.applied &&



<div className="
border
rounded-xl
p-5
mb-5
">





<h2 className="
font-bold
flex
gap-2
mb-3
">


<Wand2/>


Self Healing Agent


</h2>






<p>

✅ Auto fix generated

</p>







<pre className="
bg-gray-900
text-green-400
rounded-xl
p-4
mt-3
whitespace-pre-wrap
text-sm
">



{


result.self_healing
?.fixed_code
?.fixed_code

||

result.self_healing
?.fixed_code


}



</pre>





</div>


}












{/* LOGS */}



<div className="
bg-gray-900
text-green-400
rounded-xl
p-4
">



<h3 className="
text-white
mb-2
">

Logs

</h3>




<pre className="
whitespace-pre-wrap
text-sm
">


{


result.execution_result?.logs

||

result.execution_result?.errors

||

"No logs"


}



</pre>





</div>








</div>



:



<div className="
h-96
flex
items-center
justify-center
text-gray-400
">


Waiting for execution


</div>



}








</div>






</div>






</div>

);


}





export default Execution;