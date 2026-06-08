import { Link } from "react-router-dom";



function NotFound(){


return(

<div
className="
h-screen
flex
items-center
justify-center
bg-gray-50
"
>


<div
className="
text-center
"
>


<h1
className="
text-6xl
font-bold
"
>

404

</h1>



<p
className="
text-gray-500
mt-3
"
>

Page not found


</p>




<Link

to="/dashboard"

className="
inline-block
mt-5
bg-blue-600
text-white
px-5
py-3
rounded-lg
"

>

Back Dashboard

</Link>




</div>


</div>


);


}



export default NotFound;