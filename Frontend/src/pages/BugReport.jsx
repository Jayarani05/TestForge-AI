function BugReport(){


const bug={

title:"Login Redirect Failure",

severity:"High",

root:"Dashboard navigation failed",

fix:"Update redirect logic"

};



return (

<div className="bg-black min-h-screen p-10">


<h1 className="
text-white
text-3xl
">

Bug Analysis

</h1>



<div className="
bg-gray-900
rounded-xl
p-6
mt-8
text-white
">


<h2 className="text-xl">

{bug.title}

</h2>


<p>

Severity: {bug.severity}

</p>


<p>

Root Cause: {bug.root}

</p>


<p>

Fix: {bug.fix}

</p>


</div>


</div>

);


}


export default BugReport;