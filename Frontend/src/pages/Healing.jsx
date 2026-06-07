import { useState } from "react";

import {

    Wrench,
    CheckCircle,
    AlertCircle

} from "lucide-react";


import api from "../api/axios";



function Healing(){


const [failedCode,setFailedCode] = useState("");

const [errorLog,setErrorLog] = useState("");

const [dom,setDom] = useState("");

const [result,setResult] = useState(null);

const [loading,setLoading] = useState(false);






async function repairTest(){


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







<div className="grid grid-cols-2 gap-6">





{/* LEFT */}


<div
className="
bg-white
border
rounded-xl
p-6
shadow-sm
"
>



<h2 className="
font-semibold
flex
gap-2
items-center
mb-5
"
>

<AlertCircle size={18}/>

Broken Test

</h2>





<textarea

value={failedCode}

onChange={(e)=>setFailedCode(e.target.value)}

placeholder="Paste failed Selenium code..."

className="
w-full
h-40
border
rounded-lg
p-4
font-mono
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
"

/>






<textarea

value={dom}

onChange={(e)=>setDom(e.target.value)}

placeholder="Paste current DOM snapshot..."

className="
w-full
h-32
border
rounded-lg
p-4
mt-4
font-mono
"

/>








<button

onClick={repairTest}

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









{/* RIGHT */}



<div
className="
bg-white
border
rounded-xl
p-6
shadow-sm
"
>


<h2 className="
font-semibold
flex
gap-2
items-center
mb-5
"
>

<CheckCircle size={18}/>

AI Solution

</h2>





{

result

?


<div className="space-y-5">



<div>


<p className="text-sm text-gray-500">

Broken Locator

</p>


<h3 className="font-semibold text-red-600">

{result.broken_locator}

</h3>


</div>







<div>


<p className="text-sm text-gray-500">

Suggested Locator

</p>


<h3 className="font-semibold text-green-600">

{result.suggested_locator}

</h3>


</div>






<div>


<p className="text-sm text-gray-500">

Reason

</p>


<p>

{result.reason}

</p>


</div>








<pre
className="
bg-gray-900
text-green-400
rounded-lg
p-5
overflow-auto
"
>


{result.fixed_code}


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


AI repaired code appears here


</div>

}



</div>





</div>





</div>


);


}



export default Healing;