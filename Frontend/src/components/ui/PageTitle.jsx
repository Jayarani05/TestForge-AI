function PageTitle({

title,

subtitle

}){


return (

<div className="mb-6">


<h1
className="
text-2xl
font-bold
"
>

{title}

</h1>


<p
className="
text-gray-500
text-sm
"
>

{subtitle}

</p>


</div>


);

}


export default PageTitle;