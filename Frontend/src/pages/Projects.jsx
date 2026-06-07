import {

    Plus,
    MoreVertical

} from "lucide-react";



function Projects(){



const projects = [


    {

        name:"E-Commerce Platform",

        type:"Web Application",

        stack:[

            "Java",

            "Spring Boot",

            "React"

        ],

        updated:"Updated 2h ago"

    },



    {

        name:"Mobile Banking App",

        type:"Mobile Application",

        stack:[

            "Java",

            "Selenium",

            "TestNG"

        ],

        updated:"Updated 1d ago"

    },



    {

        name:"Inventory Management",

        type:"API Application",

        stack:[

            "Python",

            "FastAPI"

        ],

        updated:"Updated 3d ago"

    }


];






return (

<div>



{/* HEADER */}


<div

className="
flex
justify-between
items-center
mb-6
"

>



<div>


<h1

className="
text-2xl
font-bold
"

>

Projects


</h1>



<p

className="
text-gray-500
"

>

Manage and organize your testing projects


</p>



</div>





<button

className="
bg-blue-600
text-white
px-4
py-2
rounded-lg
flex
items-center
gap-2
"

>


<Plus size={18}/>


Create Project


</button>



</div>









{/* GRID */}



<div

className="
grid
grid-cols-3
gap-5
"

>



{


projects.map(

(project)=>(



<div


key={project.name}


className="
bg-white
border
rounded-xl
p-5
shadow-sm
"

>





<div

className="
flex
justify-between
"

>


<div>


<h2

className="
font-semibold
text-lg
"

>

{project.name}


</h2>



<p

className="
text-gray-500
text-sm
"

>

{project.type}


</p>


</div>




<MoreVertical size={18}/>



</div>








<div

className="
flex
gap-2
flex-wrap
mt-5
"

>


{


project.stack.map(

(item)=>(


<span

key={item}

className="
bg-blue-50
text-blue-600
px-3
py-1
rounded-full
text-xs
"

>


{item}


</span>


)

)

}


</div>









<p

className="
text-sm
text-gray-500
mt-8
"

>


{project.updated}


</p>






</div>


)

)

}



{/* ADD CARD */}



<div

className="
border
border-dashed
rounded-xl
flex
items-center
justify-center
text-gray-500
min-h-52
"

>


+ New Project


</div>





</div>




</div>


);



}



export default Projects;