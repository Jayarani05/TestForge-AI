import Input from "../components/Input";


function Register(){


return (

<div className="min-h-screen bg-black flex justify-center items-center">


<div className="bg-gray-950 p-10 rounded-xl w-96">


<h2 className="text-white text-3xl">

Create Account

</h2>


<div className="space-y-5 mt-6">


<Input label="Name"/>


<Input label="Email"/>


<Input 
label="Password"
type="password"
/>


<select

className="
w-full
bg-gray-900
text-white
p-3
rounded-lg
border
border-gray-700
"

>


<option>

QA Engineer

</option>


<option>

Developer

</option>


<option>

Admin

</option>


</select>


<button className="
bg-blue-600
text-white
w-full
py-3
rounded-lg
">

Register

</button>


</div>


</div>


</div>

);

}


export default Register;