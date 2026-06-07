function Card({

title,

value

}){


return (

<div className="
bg-gray-900
rounded-xl
p-6
shadow
">


<p className="text-gray-400">

{title}

</p>


<h2 className="
text-white
text-4xl
font-bold
mt-3
">

{value}

</h2>


</div>

);


}


export default Card;