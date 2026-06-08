import { useEffect, useState } from "react";

import {
    Download,
    FileText
} from "lucide-react";


import api from "../api/axios";



function Export(){


const [history,setHistory] = useState([]);

const [selected,setSelected] = useState("");

const [loading,setLoading] = useState(false);




useEffect(()=>{

    loadHistory();

},[]);





async function loadHistory(){


try{


const response = await api.get(
    "/history/"
);


setHistory(
    response.data
);


if(response.data.length>0){

setSelected(
    response.data[0].id
);

}


}

catch(error){

console.log(error);

}

}







async function exportFile(){


if(!selected){

alert("Select history");

return;

}



try{


setLoading(true);



const response = await api.get(

`/export/${selected}`,

{
responseType:"blob"
}

);




const url = window.URL.createObjectURL(

new Blob([response.data])

);



const link = document.createElement("a");


link.href = url;


link.setAttribute(

"download",

`testforge-report-${selected}.pdf`

);



document.body.appendChild(
    link
);


link.click();


link.remove();



}

catch(error){


console.log(error);


alert("Export failed");


}



setLoading(false);


}









return (

<div>



<div className="mb-6">


<h1 className="text-2xl font-bold">

Export Center

</h1>


<p className="text-gray-500">

Download generated QA reports

</p>


</div>









<div

className="
bg-white
border
rounded-xl
p-6
shadow-sm
"

>


<h2

className="
font-semibold
flex
gap-2
items-center
mb-5
"

>

<FileText size={18}/>

Select Generation


</h2>






<select


value={selected}


onChange={(e)=>setSelected(e.target.value)}


className="
w-full
border
rounded-lg
p-3
mb-5
"

>


{

history.map(

item=>(


<option

key={item.id}

value={item.id}

>


{

item.user_story?.slice(0,60)

}


</option>


)

)

}


</select>









<button


onClick={exportFile}


className="
bg-blue-600
text-white
px-5
py-3
rounded-lg
flex
gap-2
items-center
"

>


<Download size={18}/>


{

loading

?

"Exporting..."

:

"Download Report"


}



</button>





</div>





</div>

);


}



export default Export;