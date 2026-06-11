import { useState } from "react";

import {
    useLocation,
    useNavigate
} from "react-router-dom";


import api from "../api/axios";


import { saveHistory } from "../services/historyService";


import {

    FileText,
    Wand2,
    FolderGit2,
    Code2

} from "lucide-react";








function TestGenerator(){



const location = useLocation();

const navigate = useNavigate();





// ============================
// DATA FROM REPOSITORY PAGE
// ============================


const repository =
location.state?.repository;



const repoUrl =
location.state?.repo_url;






const [story,setStory] =
useState("");

const [tests,setTests] =
useState(null);

const [loading,setLoading] =
useState(false);










// ============================
// GENERATE TEST CASES
// ============================


async function generateTests(){



if(!story.trim()){


alert(
"Enter user story"
);


return;


}







try{



setLoading(true);






const payload = {


user_story:
story,


output_type:
"test_cases",


language:
"python",


framework:
"pytest",


project_id:
0,




project_context:{


repo_url:
repoUrl,



repository_analysis:{


name:
repository?.name,


tech_stack:
repository?.tech_stack,


security:
repository?.security,


rating:
repository?.rating


},





source_code:

repository?.repo_context



}



};








console.log(

"SENDING QA DATA",

payload

);








const response =
await api.post(

"/tests/generate",

payload

);








console.log(

"GENERATED",

response.data

);








const result =

response.data.agent_result;






setTests(

result

);









// ============================
// SAVE TEST CASES FOR EXPORT
// ============================


localStorage.setItem(

"testCases",


JSON.stringify(

result?.generated_test_cases || result,

null,

2

)

);










// ============================
// SAVE HISTORY
// ============================


saveHistory({


type:

"Test Generation",



title:

"AI QA Test Cases Generated",



description:

story,



status:

"Completed",




data:{



repository:

repository?.name || "Repository",



repo_url:

repoUrl,



user_story:

story,



test_cases:

result?.generated_test_cases



}



});







}



catch(error){



console.log(

"TEST ERROR",

error

);




alert(

"Test generation failed"

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

AI Test Generator

</h1>











{/* REPOSITORY INFO */}


<div

className="
bg-white
border
rounded-xl
p-6
mb-6
"

>



<h2

className="
font-semibold
flex
gap-2
mb-3
"

>


<FolderGit2 size={18}/>


Loaded Repository


</h2>






<p>


<b>Name :</b>{" "}



{

repository?.name ||

"Repository Loaded"

}



</p>







<p>


<b>Tech Stack :</b>{" "}



{


repository
?.tech_stack
?.join(", ")

||

"Detected"


}


</p>




</div>










{/* USER STORY */}


<div

className="
bg-white
border
rounded-xl
p-6
"

>



<h2

className="
font-semibold
flex
gap-2
mb-3
"

>


<FileText size={18}/>


User Story


</h2>








<textarea


value={story}


onChange={(e)=>

setStory(

e.target.value

)

}



placeholder="
As a user I want login using email and password
so that I can access my dashboard.
"



className="
border
rounded-lg
w-full
h-36
p-3
"


/>









<button


onClick={generateTests}


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
mt-4
"

>


<Wand2 size={18}/>



{


loading

?

"Generating..."

:

"Generate Test Cases"


}


</button>




</div>











{/* RESULT */}


{


tests &&


<div

className="
bg-white
border
rounded-xl
p-6
mt-6
"

>





<h2

className="
text-xl
font-bold
mb-5
"

>


Generated Test Cases


</h2>








<div

className="
bg-gray-100
rounded-lg
p-5
"

>



<pre

className="
whitespace-pre-wrap
text-sm
"

>


{


JSON.stringify(

tests.generated_test_cases,

null,

2

)


}



</pre>




</div>









<button



onClick={()=>{


navigate(

"/code-generation",

{


state:{



repo_url:

repoUrl,



repository:

repository,



user_story:

story,



test_cases:

tests?.generated_test_cases



}



}


);



}}




className="
mt-6
bg-green-600
text-white
px-6
py-3
rounded-lg
flex
gap-2
items-center
"

>


<Code2 size={18}/>


Convert To Code


</button>






</div>


}







</div>


);


}





export default TestGenerator;