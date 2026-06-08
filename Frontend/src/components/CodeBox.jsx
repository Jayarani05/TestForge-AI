function CodeBox({

value

}){


return (

<div
className="
bg-gray-950
border
border-gray-800
rounded-xl
p-5
"
>


<pre
className="
text-green-400
whitespace-pre-wrap
"
>

{value}

</pre>


</div>

);


}


export default CodeBox;