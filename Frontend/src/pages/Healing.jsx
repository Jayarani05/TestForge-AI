import { useState } from "react";

import {

    Wrench,
    CheckCircle,
    AlertCircle,
    Bug,
    Code,
    Lightbulb

} from "lucide-react";


import api from "../api/axios";




function Healing(){


const [failedCode,setFailedCode] = useState("");

const [errorLog,setErrorLog] = useState("");

const [dom,setDom] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);







async function repairTest(){


if(!failedCode.trim()){

alert("Paste broken test code");

return;

}



try{


setLoading(true);



const response = await api.post(

"/healing/repair",

{

failed_code:failedCode,

error_log:errorLog,

dom_snapshot:dom

}

);



setResult(response.data);



}

catch(error){


console.log(error);


alert("Healing failed");


}



setLoading(false);


}









return (

<div>




{/* HEADER */}


<div className="mb-6">


<h1 className="text-2xl font-bold">

AI Self Healing

</h1>


<p className="text-gray-500">

Automatically repair broken automation tests

</p>


</div>










<div className="
grid
grid-cols-2
gap-6
">







{/* LEFT PANEL */}



<div className="
bg-white
border
rounded-xl
p-6
shadow-sm
">



<h2 className="
font-semibold
flex
gap-2
items-center
mb-5
">

<AlertCircle size={18}/>

Broken Test

</h2>





<textarea

value={failedCode}

onChange={(e)=>setFailedCode(e.target.value)}

placeholder="Paste failed Selenium / Pytest code..."

className="
w-full
h-44
border
rounded-lg
p-4
font-mono
resize-none
"

/>








<textarea

value={errorLog}

onChange={(e)=>setErrorLog(e.target.value)}

placeholder="Paste error log..."

className="
w-full
h-32
border
rounded-lg
p-4
mt-4
font-mono
resize-none
"

/>








<textarea

value={dom}

onChange={(e)=>setDom(e.target.value)}

placeholder="Paste DOM snapshot..."

className="
w-full
h-32
border
rounded-lg
p-4
mt-4
font-mono
resize-none
"

/>









<button

onClick={repairTest}

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
">

<Wrench size={18}/>


{

loading

?

"Repairing..."

:

"Repair Test"

}


</button>



</div>











{/* RIGHT PANEL */}




<div className="
bg-white
border
rounded-xl
p-6
shadow-sm
">





<h2 className="
font-semibold
flex
gap-2
items-center
mb-6
">

<CheckCircle size={18}/>

AI Solution

</h2>









{

result

?



<div className="space-y-5">







{/* ISSUE */}


<div className="
border
rounded-xl
p-5
">


<h3 className="
font-bold
flex
gap-2
mb-3
">

<Bug size={18}/>

Problem Found

</h3>


<p>

{

result.broken_locator ||

result.issue ||

"Broken locator detected"

}

</p>


</div>









{/* FIX */}


<div className="
border
rounded-xl
p-5
">


<h3 className="
font-bold
flex
gap-2
mb-3
">

<Lightbulb size={18}/>

Suggested Fix

</h3>



<p className="font-semibold">


{

result.suggested_locator ||

result.fix ||

"Updated locator generated"

}


</p>



</div>










{/* REASON */}



<div className="
border
rounded-xl
p-5
">


<h3 className="font-bold mb-3">

Reason

</h3>



<p className="text-gray-600">

{

result.reason ||

result.explanation ||

"AI detected UI change and repaired the automation script."

}

</p>



</div>











{/* FIXED CODE */}



<div className="
border
rounded-xl
p-5
">


<h3 className="
font-bold
flex
gap-2
mb-3
">

<Code size={18}/>

Fixed Code

</h3>



<div className="
bg-gray-50
border
rounded-lg
p-4
font-mono
text-sm
overflow-auto
">


{

result.fixed_code ||

"No code returned"

}


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

AI repaired solution appears here

</div>



}






</div>







</div>






</div>

);


}



export default Healing;