import { useEffect, useState } from "react";
import {
    Trash,
    Clock,
    FileText,
    CheckCircle,
    Shield,
    XCircle
} from "lucide-react";

import api from "../api/axios";


function TestItem({ test }) {

    return (

        <div className="
        border
        rounded-lg
        p-3
        mb-2
        ">

            <div className="
            flex
            justify-between
            ">

                <b>
                    {test.id}
                </b>

                <span className="
                text-blue-600
                text-sm
                ">
                    {test.priority}
                </span>

            </div>


            <p className="
            text-gray-600
            text-sm
            mt-2
            ">

                {test.title}

            </p>

        </div>

    )

}





function History(){


const [history,setHistory] = useState([]);

const [selected,setSelected] = useState(null);



useEffect(()=>{

    loadHistory();

},[]);




const loadHistory = async()=>{

try{

    const response = await api.get(
        "/history/"
    );


    setHistory(response.data);


}
catch(error){

    console.log(error);

}

};







const deleteHistory = async(id)=>{

try{


if(!confirm("Delete history?")){

    return;

}


await api.delete(
    `/history/${id}`
);


loadHistory();


setSelected(null);


}
catch(error){

alert("Delete API not available");

}

};









return(

<div>



<h1 className="
text-2xl
font-bold
mb-6
">

Generation History

</h1>







<div className="
grid
grid-cols-3
gap-6
">







{/* LEFT */}


<div className="
bg-white
border
rounded-xl
p-5
">


<h2 className="
font-semibold
flex
gap-2
mb-5
">

<Clock size={18}/>

Previous Runs

</h2>






{

history.length===0

?

<p className="text-gray-400">

No history found

</p>


:


history.map(item=>(


<div

key={item.id}

onClick={()=>setSelected(item)}

className="
border
rounded-lg
p-3
mb-3
cursor-pointer
hover:bg-gray-50
"

>


<div className="
flex
gap-2
items-center
">

<FileText size={16}/>


<p className="
font-medium
truncate
">

{
item.user_story ||
item.input_story ||
"Generated Test"
}

</p>


</div>



<button

onClick={(e)=>{

e.stopPropagation();

deleteHistory(item.id);

}}

className="
text-red-500
text-sm
flex
gap-1
mt-3
"

>

<Trash size={14}/>

Delete


</button>



</div>


))

}



</div>









{/* RIGHT */}


<div className="
bg-white
border
rounded-xl
p-5
col-span-2
overflow-y-auto
h-[650px]
">



{

selected

?

<div>



<h2 className="
font-bold
mb-4
">

Generated Result

</h2>





<h3 className="
font-semibold
mb-2
">

Requirement

</h3>


<p className="
bg-gray-100
rounded-lg
p-3
mb-5
">

{
selected.user_story ||
selected.input_story
}

</p>







<h3 className="
font-bold
flex
gap-2
mb-3
">

<CheckCircle/>

Positive Tests

</h3>



{

selected.generated_output
?.generated_test_cases
?.result
?.positive_tests
?.map(test=>(

<TestItem

key={test.id}

test={test}

/>

))

}









<h3 className="
font-bold
flex
gap-2
mt-5
mb-3
">

<XCircle/>

Negative Tests

</h3>



{

selected.generated_output
?.generated_test_cases
?.result
?.negative_tests
?.map(test=>(


<TestItem

key={test.id}

test={test}

/>


))

}










<h3 className="
font-bold
flex
gap-2
mt-5
mb-3
">

<Shield/>

Security Tests

</h3>



{

selected.generated_output
?.generated_test_cases
?.result
?.security_tests
?.map(test=>(


<TestItem

key={test.id}

test={test}

/>


))

}




</div>


:


<div className="
h-full
flex
items-center
justify-center
text-gray-400
">

Select history item

</div>


}



</div>



</div>


</div>


);


}


export default History;