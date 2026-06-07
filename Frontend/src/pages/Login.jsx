import Input from "../components/Input";


function Login(){


return (

<div className="min-h-screen bg-black flex items-center justify-center">


<div className="
bg-gray-950 
p-10 
rounded-xl 
w-96 
shadow-lg
">


<h1 className="text-3xl text-white font-bold">

TestForge AI

</h1>


<p className="text-gray-400 mt-2">

AI QA Automation Platform

</p>


<div className="mt-8 space-y-5">


<Input

label="Email"

placeholder="Enter email"

/>


<Input

label="Password"

type="password"

placeholder="Enter password"

/>


<button className="
bg-blue-600
w-full
py-3
rounded-lg
text-white
">

Login

</button>


<p className="text-gray-400 text-center">

Create Account

</p>


</div>


</div>


</div>

);

}


export default Login;