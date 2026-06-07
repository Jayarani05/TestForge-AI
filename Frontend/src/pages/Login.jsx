import { useState } from "react";

import { useNavigate } from "react-router-dom";

import { useAuth } from "../context/AuthContext";

import Input from "../components/Input";


function Login(){


const navigate = useNavigate();


const { login } = useAuth();



const [email,setEmail] = useState("");

const [password,setPassword] = useState("");

const [error,setError] = useState("");




const handleLogin = async()=>{


try{


await login(

email,

password

);


navigate(

"/dashboard"

);


}

catch(err){


setError(

"Invalid email or password"

);


}


};




return (


<div className="min-h-screen bg-black flex items-center justify-center">


<div className="bg-gray-950 p-10 rounded-xl w-96">


<h1 className="text-white text-3xl font-bold">

TestForge AI

</h1>


<p className="text-gray-400">

AI QA Automation Platform

</p>


<div className="space-y-5 mt-8">


<Input

label="Email"

value={email}

onChange={(e)=>setEmail(e.target.value)}

/>



<Input

label="Password"

type="password"

value={password}

onChange={(e)=>setPassword(e.target.value)}

/>



{

error &&

<p className="text-red-500">

{error}

</p>

}



<button

onClick={handleLogin}

className="bg-blue-600 text-white w-full py-3 rounded-lg"

>


Login


</button>


</div>


</div>


</div>

);


}


export default Login;