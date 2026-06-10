import {

BrowserRouter,
Routes,
Route,
Navigate

} from "react-router-dom";


import Login from "./pages/Login";
import Register from "./pages/Register";


import Dashboard from "./pages/Dashboard";
import Projects from "./pages/Projects";
import TestGenerator from "./pages/TestGenerator";
import Automation from "./pages/Automation";
import Execution from "./pages/Execution";
import Repository from "./pages/Repository";
import Healing from "./pages/Healing";
import CICD from "./pages/CICD";
import Export from "./pages/Export";
import Settings from "./pages/Settings";
import BugReport from "./pages/BugReport";
import NotFound from "./pages/NotFound";
import History from "./pages/History";
import Workflow from "./pages/Workflow";


import ProtectedRoute from "./routes/ProtectedRoute";


import DashboardLayout from "./layouts/DashboardLayout";




function App(){


return (

<BrowserRouter>


<Routes>



<Route

path="/"

element={<Navigate to="/login" />}

/>





<Route

path="/login"

element={<Login />}

/>



<Route

path="/register"

element={<Register />}

/>






{/* PROTECTED APP LAYOUT */}


<Route

element={

<ProtectedRoute>

<DashboardLayout />

</ProtectedRoute>

}

>





<Route

path="/dashboard"

element={<Dashboard />}

/>




<Route

path="/workflow"

element={<Workflow />}

/>




<Route

path="/projects"

element={<Projects />}

/>





<Route

path="/generate"

element={<TestGenerator />}

/>



<Route

path="/automation"

element={<Automation />}

/>





<Route

path="/execution"

element={<Execution />}

/>





<Route

path="/repository"

element={<Repository />}

/>





<Route

path="/healing"

element={<Healing />}

/>





<Route

path="/cicd"

element={<CICD />}

/>





<Route

path="/export"

element={<Export />}

/>




<Route

path="/settings"

element={<Settings />}

/>




</Route>


<Route

path="/bugs"

element={<BugReport />}

/>

<Route

path="*"

element={<NotFound />}

/>

<Route
    path="/history"
    element={<History />}
/>



</Routes>


</BrowserRouter>


);


}


export default App;
