import CodeBox from "../components/CodeBox";


function Execution(){


const logs = `
pytest started

test_login FAILED

AssertionError:
login != dashboard
`;



return (

<div className="bg-black min-h-screen p-10">


<h1 className="
text-white
text-3xl
font-bold
">

Test Execution

</h1>



<textarea

placeholder="Paste automation code..."

className="
w-full
h-40
bg-gray-900
text-white
rounded-xl
p-5
mt-8
"

/>



<button
className="
bg-blue-600
text-white
px-6
py-3
rounded-lg
mt-5
"
>

Run Test

</button>



<CodeBox

value={logs}

/>


</div>

);


}


export default Execution;