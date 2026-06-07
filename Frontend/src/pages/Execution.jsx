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






const runTest = async()=>{


if(!code.trim()){

alert("Enter automation code");

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



setResult(response.data);



}

catch(error){


console.log(error);

alert("Execution failed");


}



setLoading(false);



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








{/* LEFT SIDE */}


<div className="
border
rounded-xl
p-6
bg-white
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

placeholder="Paste your pytest / automation code here..."

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









{/* RIGHT SIDE */}



<div className="
border
rounded-xl
p-6
bg-white
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





{/* TOP CARDS */}



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

<p className="
text-gray-500
mt-2
">

Status

</p>


<b>

{
result.execution_result.status
}

</b>


</div>








<div className="
border
rounded-xl
p-5
">


{

result.execution_result.passed

?

<CheckCircle className="text-green-600"/>

:

<XCircle className="text-red-600"/>

}



<p className="
text-gray-500
mt-2
">

Result

</p>


<b>

{

result.execution_result.passed

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


<p className="
text-gray-500
mt-2
">

Time

</p>


<b>

{
result.execution_result.execution_time
}

</b>


</div>




</div>









{/* BUG */}



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
">

{

result.bug_analysis.bug_found

?

"Bug detected"

:

"No bugs detected 🎉"

}

</p>



<p className="
text-gray-500
mt-2
">

{

result.bug_analysis.message

}

</p>



</div>










{/* CLEAN SUMMARY */}



<div className="
border
rounded-xl
p-5
">



<h2 className="
font-bold
mb-5
">

Execution Summary

</h2>





<div className="
space-y-4
">






<div className="
flex
justify-between
border-b
pb-3
">


<span className="text-gray-500">

Status

</span>


<b>

{

result.execution_result.passed

?

"Success"

:

"Failed"

}

</b>


</div>









<div className="
flex
justify-between
border-b
pb-3
">


<span className="text-gray-500">

Execution Time

</span>


<b>

{
result.execution_result.execution_time
}

</b>


</div>








<div className="
flex
justify-between
border-b
pb-3
">


<span className="text-gray-500">

Bug Found

</span>


<b>

{

result.bug_analysis.bug_found

?

"Yes"

:

"No"

}

</b>


</div>







</div>



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