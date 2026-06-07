import { useState } from "react";

import {

    FileText,
    Table,
    Code,
    Download

} from "lucide-react";


import api from "../api/axios";




function Export(){


const [loading,setLoading] = useState("");

const [file,setFile] = useState(null);





async function exportFile(type){



try{


setLoading(type);



const response = await api.post(

"/export",

{

export_type:type,


data:{


generated_test_cases:{


functional:[

{

id:"TC001",

title:"Login test",

type:"functional",

priority:"high"

}

]


},


code:

"driver.find_element(By.ID,'login').click()",


language:"python"


}


}

);




setFile(

response.data

);



}


catch(error){


console.log(error);


alert("Export failed");


}



setLoading("");



}









const options=[



{

type:"pdf",

title:"PDF Report",

desc:"Complete QA report",

icon:FileText

},



{

type:"excel",

title:"Excel Sheet",

desc:"Generated test cases",

icon:Table

},



{

type:"code",

title:"Code Export",

desc:"Automation scripts",

icon:Code

}



];








return(

<div>





{/* HEADER */}


<div className="mb-6">


<h1 className="text-2xl font-bold">

Export Center

</h1>


<p className="text-gray-500">

Download reports, test cases and automation files

</p>


</div>










{/* CARDS */}


<div className="grid grid-cols-3 gap-6">



{


options.map(

(item)=>{


const Icon=item.icon;



return(


<div

key={item.type}

className="
bg-white
border
rounded-xl
p-6
shadow-sm
"

>




<div

className="
bg-blue-50
text-blue-600
w-fit
p-3
rounded-lg
mb-5
"

>


<Icon size={24}/>


</div>






<h2 className="font-semibold text-lg">

{item.title}

</h2>



<p className="text-gray-500 text-sm mt-2">

{item.desc}

</p>








<button

onClick={()=>exportFile(item.type)}

className="
mt-6
bg-blue-600
text-white
px-4
py-2
rounded-lg
flex
gap-2
items-center
"

>



<Download size={16}/>



{


loading===item.type

?

"Exporting..."

:

"Export"


}




</button>





</div>


);


}

)

}




</div>










{/* HISTORY */}


<div

className="
bg-white
border
rounded-xl
p-6
mt-6
"

>



<h2 className="font-semibold mb-5">

Recent Export

</h2>






{

file

?


<div

className="
flex
justify-between
items-center
"

>


<span>

Export generated successfully

</span>



<span className="text-green-600">

Ready

</span>



</div>



:


<p className="text-gray-400">

No exports yet

</p>


}





</div>







</div>


);



}



export default Export;