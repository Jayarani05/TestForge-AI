function StatCard({

title,

value,

icon:Icon,

change

}){


return (

<div
className="
bg-white
border
border-gray-200
rounded-xl
p-5
shadow-sm
"
>


<div
className="
flex
justify-between
items-center
"
>


<div>


<p
className="
text-sm
text-gray-500
"
>

{title}

</p>


<h2
className="
text-3xl
font-bold
mt-2
"
>

{value}

</h2>


{

change &&

<p
className="
text-xs
text-green-600
mt-2
"
>

{change}

</p>

}


</div>


<div
className="
bg-blue-50
text-blue-600
p-3
rounded-lg
"
>


<Icon size={22}/>


</div>



</div>


</div>

);

}


export default StatCard;