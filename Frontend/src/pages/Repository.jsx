function Repository(){


const features=[

"FastAPI Backend",

"JWT Authentication",

"AI Test Generator",

"CI/CD Support"

];


return (

<div className="bg-black min-h-screen p-10">


<h1 className="
text-white
text-3xl
">

Repository Intelligence

</h1>



<div className="mt-8 space-y-4">


{

features.map(

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


export default Repository;