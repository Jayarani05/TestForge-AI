import { useState } from "react";

import { Link, useNavigate } from "react-router-dom";

import api from "../api/axios";




function Register(){



    const navigate = useNavigate();



    const [name,setName] = useState("");

    const [email,setEmail] = useState("");

    const [password,setPassword] = useState("");

    const [error,setError] = useState("");







    async function handleSubmit(e){


        e.preventDefault();


        try{


            await api.post(

                "/auth/register",

                {

                    name,

                    email,

                    password

                }

            );



            navigate("/login");


        }


        catch(err){



            setError(

                "Registration failed"

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



{/* LOGO */}



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

Create your QA automation workspace


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

Create account


</h2>




<p

className="
text-center
text-gray-500
text-sm
mb-6
"

>

Start using TestForge AI


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

Full Name

</label>



<input


value={name}


onChange={(e)=>setName(e.target.value)}


placeholder="John Doe"


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


placeholder="Create password"


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


Create account


</button>









<p

className="
text-center
text-sm
mt-6
"

>


Already have an account?



<Link

to="/login"

className="
text-blue-600
ml-1
"

>

Sign in

</Link>




</p>







</form>






</div>



</div>



);



}




export default Register;