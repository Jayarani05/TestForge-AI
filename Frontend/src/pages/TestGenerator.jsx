import { useState } from "react";

import api from "../api/axios";

import ResultViewer from "../components/ResultViewer";



function TestGenerator(){


const [story,setStory] = useState("");


const [language,setLanguage] = useState(
    "Python"
);


const [framework,setFramework] = useState(
    "Pytest"
);


const [loading,setLoading] =
useState(false);


const [result,setResult] =
useState(null);





const generateTests = async()=>{


try{


setLoading(true);



const response = await api.post(

"/tests/generate",

{

user_story:story,

output_type:"test_cases",

language,

framework,

project_context:""

}

);



setResult(

response.data.agent_result

);



}

catch(error){


console.log(error);


alert(
"Generation failed"
);


}


setLoading(false);


};






return (


<div className="min-h-screen bg-black p-10">


<h1 className="
text-white
text-3xl
font-bold
">

AI Test Generator

</h1>




<textarea

value={story}

onChange={(e)=>setStory(e.target.value)}

placeholder="Enter user story..."

className="
w-full
h-40
mt-8
bg-gray-900
text-white
p-5
rounded-xl
"

/>





<div className="flex gap-5 mt-5">


<select

value={language}

onChange={(e)=>setLanguage(e.target.value)}

className="
bg-gray-900
text-white
p-3
rounded
"

>


<option>

Python

</option>


<option>

Java

</option>


</select>





<select

value={framework}

onChange={(e)=>setFramework(e.target.value)}

className="
bg-gray-900
text-white
p-3
rounded
"

>


<option>

Pytest

</option>


<option>

Selenium

</option>


</select>


</div>





<button

onClick={generateTests}

className="
bg-blue-600
text-white
px-6
py-3
rounded-lg
mt-6
"

>


{

loading
?
"Generating..."
:
"Generate Tests"


}


</button>





{

result &&

<ResultViewer

title="Generated Test Cases"

content={

JSON.stringify(
result,
null,
2
)

}

/>

}


</div>


);


}



export default TestGenerator;