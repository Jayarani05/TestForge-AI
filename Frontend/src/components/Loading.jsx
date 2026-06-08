import { Loader2 } from "lucide-react";


function Loading({text="Loading..."}){


return (

<div
className="
flex
items-center
justify-center
gap-3
text-gray-500
p-10
"
>


<Loader2
size={22}
className="animate-spin"
/>


{text}


</div>

);


}


export default Loading;