import ResultViewer from "../components/ResultViewer";


function TestGenerator(){


return (

<div className="
min-h-screen
bg-black
p-10
">


<h1 className="
text-white
text-3xl
font-bold
">

AI Test Generator

</h1>



<textarea

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


<div className="
flex
gap-5
mt-5
">


<select className="
bg-gray-900
text-white
p-3
rounded
">

<option>
Python
</option>

<option>
Java
</option>


</select>



<select className="
bg-gray-900
text-white
p-3
rounded
">

<option>
Pytest
</option>

<option>
Selenium
</option>

</select>


</div>



<button className="
bg-blue-600
text-white
px-6
py-3
rounded-lg
mt-6
">

Generate Tests

</button>


<ResultViewer

title="Generated Tests"

content="AI output appears here"

/>


</div>

);


}


export default TestGenerator;