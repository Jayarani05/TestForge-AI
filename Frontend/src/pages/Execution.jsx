import { useState } from "react";

import {

    Play,
    CheckCircle,
    XCircle,
    Clock,
    Bug,
    Activity

} from "lucide-react";


import api from "../api/axios";






function Execution(){



const [code,setCode] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);









// ===============================
// RUN TEST EXECUTION
// ===============================


const runTest = async()=>{



if(!code.trim()){


    alert(
        "Enter automation code"
    );


    return;

}





try{



setLoading(true);



const response = await api.post(

    "/execution/run",

    {

        code:code

    }

);




console.log(

    "EXECUTION RESULT",

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




};









return(


<div>




<h1 className="
text-2xl
font-bold
">

Test Execution

</h1>




<p className="
text-gray-500
mb-8
">

Run automated tests and analyze execution results

</p>









<div className="
grid
grid-cols-2
gap-8
">







{/* ================= LEFT ================= */}


<div className="
bg-white
border
rounded-xl
p-6
">




<h2 className="
font-bold
mb-5
">

Automation Code

</h2>






<textarea


value={code}


onChange={(e)=>setCode(e.target.value)}



placeholder="
Paste generated pytest selenium code here...
"



className="
w-full
h-[420px]
border
rounded-xl
p-5
font-mono
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
px-8
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









{/* ================= RIGHT ================= */}



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
mb-6
">


<Activity/>


Execution Result


</h2>









{


result


?



<div>







{/* STATUS CARDS */}


<div className="
grid
grid-cols-3
gap-5
mb-8
">








<div className="
border
rounded-xl
p-5
">


<Clock/>


<p className="text-gray-500 mt-2">

Status

</p>



<b>


{

result.execution_result?.status

}


</b>



</div>










<div className="
border
rounded-xl
p-5
">



{

result.execution_result?.passed

?

<CheckCircle className="text-green-600"/>

:

<XCircle className="text-red-600"/>

}




<p className="text-gray-500 mt-2">

Result

</p>




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
p-5
">


<Clock/>


<p className="text-gray-500 mt-2">

Time

</p>



<b>


{

result.execution_result?.execution_time

||
"-"


}


</b>



</div>







</div>












{/* BUG ANALYZER */}



<div className="
border
rounded-xl
p-5
mb-6
">





<h2 className="
font-bold
flex
gap-2
mb-4
">


<Bug/>


Bug Analysis


</h2>






<p className="
font-semibold
mb-4
">



{

result.execution_result?.passed

?

"✅ No Bugs Found"

:

"🐞 Bug Detected"


}



</p>









{

!result.execution_result?.passed &&



<div className="
space-y-3
">



<p>

<b>Severity : </b>


{

result.bug_analysis?.severity

}


</p>






<p>

<b>Root Cause : </b>


{

result.bug_analysis?.root_cause

}


</p>







<p>

<b>Possible Fix : </b>


{

result.bug_analysis?.possible_fix

}


</p>







<p>

<b>QA Recommendation : </b>


{

result.bug_analysis?.qa_recommendation

}


</p>





</div>



}







</div>









{/* LOGS */}



<div className="
bg-gray-900
text-green-400
rounded-xl
p-5
">



<h2 className="
font-bold
mb-3
text-white
">

Logs

</h2>




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


Run tests to see execution report


</div>



}






</div>





</div>





</div>



);


}





export default Execution;