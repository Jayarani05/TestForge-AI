import { useEffect,useState } from "react";

import {

History as HistoryIcon,
Trash2,
CheckCircle

} from "lucide-react";


import {

getHistory,
clearHistory

} from "../services/historyService";





function History(){


const [items,setItems]=useState([]);




useEffect(()=>{


setItems(

getHistory()

);


},[]);






function removeAll(){


clearHistory();


setItems([]);


}






return(

<div>



<div className="
flex
justify-between
items-center
mb-6
">


<h1 className="
text-2xl
font-bold
flex
gap-2
">

<HistoryIcon/>

Activity History

</h1>





<button

onClick={removeAll}

className="
bg-red-600
text-white
px-4
py-2
rounded-lg
flex
gap-2
"

>

<Trash2 size={18}/>

Clear

</button>



</div>









{


items.length===0

?

<div className="
bg-white
border
rounded-xl
h-60
flex
items-center
justify-center
text-gray-400
">

No history available

</div>


:



<div className="space-y-5">


{

items.map((item)=>(



<div

key={item.id}

className="
bg-white
border
rounded-xl
p-5
flex
justify-between
items-center
"

>



<div>


<h2 className="
font-bold
text-lg
">

{item.type}

</h2>



<p>

{item.title}

</p>



<p className="
text-gray-500
text-sm
">

{item.description}

</p>



</div>







<div className="
text-right
">


<CheckCircle className="
text-green-600
ml-auto
"/>



<b>

{item.status}

</b>



<p className="
text-gray-400
text-sm
">

{item.time}

</p>



</div>




</div>


))

}


</div>

}






</div>


);


}



export default History;