import { useState } from "react";

import {
    useLocation,
    useNavigate
} from "react-router-dom";


import {
    Code2,
    Play
} from "lucide-react";


import api from "../api/axios";


import { saveHistory } from "../services/historyService";







function CodeGeneration(){



const location = useLocation();

const navigate = useNavigate();





const {

    test_cases,

    user_story,

    repository

} = location.state || {};








const [code,setCode] = useState("");

const [loading,setLoading] = useState(false);










async function generateCode(){



try{



setLoading(true);






const payload = {


    test_cases:

        test_cases,



    repo_context:

        repository,



    language:

        "python",



    framework:

        "pytest"


};








console.log(

"SENDING CODE REQUEST",

payload

);








const response = await api.post(

"/code/generate",

payload

);









console.log(

"FULL BACKEND RESPONSE",

response.data

);









let generatedCode = "";





if(

response.data?.generated_code?.code

){



generatedCode =

response.data.generated_code.code;



}




else if(

response.data?.code

){



generatedCode =

response.data.code;



}





else if(

typeof response.data?.generated_code === "string"

){



generatedCode =

response.data.generated_code;



}





else{


generatedCode =

JSON.stringify(

response.data,

null,

2

);


}










setCode(

generatedCode

);










// ============================
// SAVE FOR EXPORT
// ============================


localStorage.setItem(

"generatedCode",

generatedCode

);









// ============================
// SAVE HISTORY
// ============================


saveHistory({



type:

"Code Generation",




title:

"Automation Code Generated",




description:

"PyTest Selenium automation script generated",




status:

"Completed",




data:{



repository:

repository?.name || "Repository",




framework:

"PyTest + Selenium",




code:

generatedCode



}



});









}



catch(error){



console.log(

"CODE ERROR",

error

);




alert(

"Code generation failed"

);



}







finally{



setLoading(false);



}



}













return(


<div>






<h1

className="
text-2xl
font-bold
mb-6
"

>


Automation Code Generator


</h1>










<div

className="
bg-white
border
rounded-xl
p-6
mb-6
"

>



<h2 className="font-bold mb-3">


Input Summary


</h2>








<p>


<b>Repository :</b>{" "}



{

repository?.name ||

"Repository Loaded"

}


</p>








<p>


<b>User Story :</b>{" "}


{

user_story ||

"Loaded"

}


</p>








<p>


<b>Framework :</b>{" "}


PyTest + Selenium


</p>








<p>


<b>Test Cases :</b>{" "}


{

test_cases

?

"Loaded"

:

"Missing"

}


</p>





</div>












<button


onClick={generateCode}


disabled={loading}


className="
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



<Code2 size={18}/>




{

loading

?

"Generating..."

:

"Generate Automation Code"


}



</button>











{


code &&




<div

className="
mt-6
bg-gray-900
text-green-400
rounded-xl
p-5
"

>






<h2

className="
text-white
font-bold
mb-4
"

>


Generated Automation Script


</h2>








<pre

className="
whitespace-pre-wrap
overflow-auto
max-h-[500px]
text-sm
"

>


{code}


</pre>









<button



onClick={()=>{


navigate(

"/execution",

{


state:{



generated_code:

code,



test_cases:

test_cases,



repository:

repository



}



}


);



}}



className="
mt-6
bg-green-600
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



Execute Tests



</button>





</div>



}







</div>


);



}





export default CodeGeneration;