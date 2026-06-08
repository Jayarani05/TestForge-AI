import { Inbox } from "lucide-react";



function EmptyState({

title,

message

}){


return(

<div
className="
border
border-dashed
rounded-xl
p-10
text-center
text-gray-500
"
>


<Inbox
size={35}
className="mx-auto mb-3"
/>


<h3
className="
font-semibold
text-gray-700
"
>

{title}

</h3>


<p className="text-sm mt-2">

{message}

</p>



</div>

);


}


export default EmptyState;