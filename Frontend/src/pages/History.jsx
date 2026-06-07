function History(){


const history=[

"Generated Login Tests",

"Generated Payment Tests",

"Generated API Tests"

];


return (

<div className="
bg-black
min-h-screen
p-10
">


<h1 className="
text-white
text-3xl
">

Generation History

</h1>


<div className="mt-8 space-y-4">


{

history.map(

(item,index)=>(


<div

key={index}

className="
bg-gray-900
text-white
p-5
rounded-xl
"

>

{item}


</div>


)

)

}


</div>


</div>

);

}


export default History;