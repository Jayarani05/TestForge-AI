import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import {
    FileCode,
    Rocket,
    Copy,
    PlayCircle
} from "lucide-react";

import api from "../api/axios";

import CodeBox from "../components/CodeBox";

import {
    getGeneratedTests,
    getRepoContext,
    saveAutomationCode
} from "../services/workflowService";


function Automation(){

const navigate = useNavigate();

const [repoContext,setRepoContext] = useState(null);
const [testCases,setTestCases] = useState([]);
const [automation,setAutomation] = useState(null);
const [loading,setLoading] = useState(false);


useEffect(()=>{

setRepoContext(
getRepoContext()
);

setTestCases(
getGeneratedTests()
);

},[]);


const getCode = ()=>{

if(!automation){
return "";
}

return automation.code ||
automation.generated_code ||
JSON.stringify(
automation,
null,
2
);

};


const generateAutomation = async()=>{

if(!repoContext){
alert("Analyze a repository first");
return;
}

if(!testCases.length){
alert("Generate test cases first");
return;
}

try{

setLoading(true);

const response = await api.post(
"/automation/generate",
{
repo_context: repoContext,
test_cases: testCases,
project_name: repoContext.project_name || "TestProject"
}
);

setAutomation(response.data);

saveAutomationCode(response.data);

}
catch(error){

console.log(error);
alert("Automation generation failed");

}

setLoading(false);

};


const copyCode = ()=>{

navigator.clipboard.writeText(
getCode()
);

alert("Copied");

};


return(

<div>

<div className="mb-6">

<h1 className="text-2xl font-bold">
Automation Generator
</h1>

<p className="text-gray-500">
Convert generated QA test cases into executable automation code
</p>

</div>


<div className="grid grid-cols-2 gap-6">

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
<FileCode size={18}/>
Workflow Inputs
</h2>

<div className="grid grid-cols-2 gap-4 mb-6">

<div className="border rounded-xl p-4">
<p className="text-gray-500 text-sm">
Repository
</p>
<b>
{repoContext?.project_name || "Not analyzed"}
</b>
</div>

<div className="border rounded-xl p-4">
<p className="text-gray-500 text-sm">
Test Cases
</p>
<b>
{testCases.length}
</b>
</div>

<div className="border rounded-xl p-4">
<p className="text-gray-500 text-sm">
Language
</p>
<b>
{repoContext?.language || "Unknown"}
</b>
</div>

<div className="border rounded-xl p-4">
<p className="text-gray-500 text-sm">
Framework
</p>
<b>
{repoContext?.framework || "Auto"}
</b>
</div>

</div>

<button
onClick={generateAutomation}
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
<Rocket size={18}/>
{
loading
?
"Generating..."
:
"Generate Automation"
}
</button>

<button
onClick={()=>navigate("/generate")}
className="
ml-3
border
px-5
py-3
rounded-lg
"
>
Back to Tests
</button>

</div>


<div className="
bg-white
border
rounded-xl
p-6
shadow-sm
">

<div className="
flex
justify-between
items-center
mb-5
">

<h2 className="
font-semibold
flex
gap-2
items-center
">
<FileCode size={18}/>
Generated Code
</h2>

<div className="flex gap-3">

<button
onClick={copyCode}
disabled={!automation}
className="
text-blue-600
flex
gap-2
text-sm
items-center
"
>
<Copy size={16}/>
Copy
</button>

<button
onClick={()=>navigate("/execution")}
disabled={!automation}
className="
text-blue-600
flex
gap-2
text-sm
items-center
"
>
<PlayCircle size={16}/>
Run
</button>

</div>

</div>

{
automation
?
<div className="h-[520px] overflow-auto">
<CodeBox value={getCode()}/>
</div>
:
<div className="
h-[520px]
flex
items-center
justify-center
text-gray-400
border
rounded-xl
">
Generated automation code appears here
</div>
}

</div>

</div>

</div>

);

}


export default Automation;
