import { useState } from "react";

import { Link, useNavigate } from "react-router-dom";

import { useAuth } from "../context/AuthContext";



function Login(){


    const navigate = useNavigate();


    const { login } = useAuth();



    const [email,setEmail] = useState("");

    const [password,setPassword] = useState("");

    const [error,setError] = useState("");





    async function handleSubmit(e){


        e.preventDefault();


        try{


            await login(

                email,

                password

            );


            navigate("/dashboard");


        }

        catch(err){


            setError(
                "Invalid email or password"
            );


        }


    }






return (

<div
className="
min-h-screen
flex
items-center
justify-center
bg-gray-50
"
>



<div
className="
w-full
max-w-md
"
>


{/* BRAND */}


<div
className="
text-center
mb-8
"
>


<h1
className="
text-3xl
font-bold
"
>

⚡ TestForge AI

</h1>


<p
className="
text-gray-500
mt-2
"
>

AI powered QA automation platform

</p>


</div>







<form

onSubmit={handleSubmit}

className="
bg-white
border
rounded-xl
shadow-sm
p-8
"

>



<h2
className="
text-xl
font-semibold
text-center
mb-2
"
>

Welcome back

</h2>


<p
className="
text-center
text-gray-500
text-sm
mb-6
"
>

Sign in to your account

</p>







{

error &&

<p
className="
bg-red-50
text-red-600
p-3
rounded-lg
text-sm
mb-4
"
>

{error}

</p>

}









<label className="text-sm">

Email

</label>


<input

type="email"

value={email}

onChange={(e)=>setEmail(e.target.value)}

placeholder="name@example.com"

className="
mt-2
mb-4
w-full
border
rounded-lg
p-3
"

/>








<label className="text-sm">

Password

</label>



<input

type="password"

value={password}

onChange={(e)=>setPassword(e.target.value)}

placeholder="Enter password"

className="
mt-2
mb-6
w-full
border
rounded-lg
p-3
"

/>







<button

className="
w-full
bg-blue-600
text-white
rounded-lg
p-3
hover:bg-blue-700
"

>

Sign in

</button>






<p
className="
text-center
text-sm
mt-6
"
>

Don't have an account?


<Link

to="/register"

className="
text-blue-600
ml-1
"

>

Sign up

</Link>


</p>





</form>


</div>


</div>

);


}


export default Login;