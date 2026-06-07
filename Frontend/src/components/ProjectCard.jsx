function ProjectCard({
    name,
    description,
    technology
}) {


return (

<div className="
bg-gray-900
rounded-xl
p-6
border
border-gray-800
">


<h2 className="
text-white
text-xl
font-bold
">

{name}

</h2>


<p className="
text-gray-400
mt-3
">

{description}

</p>


<span className="
inline-block
mt-5
bg-blue-600
px-3
py-1
rounded
text-white
text-sm
">

{technology}

</span>


</div>

);

}


export default ProjectCard;