function ResultViewer({title,content}){


return (

<div className="
bg-gray-900
rounded-xl
p-5
mt-5
">


<h2 className="
text-white
font-bold
text-xl
">

{title}

</h2>


<pre className="
text-gray-300
mt-4
whitespace-pre-wrap
">

{content}

</pre>


</div>

);

}


export default ResultViewer;