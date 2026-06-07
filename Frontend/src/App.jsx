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

import ProtectedRoute from "./routes/ProtectedRoute";
import Execution from "./pages/Execution";
import Repository from "./pages/Repository";
import Healing from "./pages/Healing";
import CICD from "./pages/CICD";
import Export from "./pages/Export";

function App(){


return (

<BrowserRouter>


<Routes>


<Route

path="/"

element={

<Navigate to="/login" />

}

/>


<Route

path="/login"

element={<Login />}

/>


<Route

path="/register"

element={<Register />}

/>


<Route

path="/dashboard"

element={

<ProtectedRoute>

<Dashboard />

</ProtectedRoute>

}

/>


<Route

path="/projects"

element={

<ProtectedRoute>

<Projects />

</ProtectedRoute>

}

/>


<Route

path="/generate"

element={

<ProtectedRoute>

<TestGenerator />

</ProtectedRoute>

}

/>


<Route

    path="/execution"

    element={

        <ProtectedRoute>

            <Execution />

        </ProtectedRoute>

    }

/>

<Route

path="/repository"

element={

<ProtectedRoute>

<Repository />

</ProtectedRoute>

}

/>

<Route

    path="/healing"

    element={

        <ProtectedRoute>

            <Healing />

        </ProtectedRoute>

    }

/>

<Route

path="/cicd"

element={

<ProtectedRoute>

<CICD />

</ProtectedRoute>

}

/>

<Route

path="/export"

element={

<ProtectedRoute>

<Export />

</ProtectedRoute>

}

/>


</Routes>


</BrowserRouter>

);

}


export default App;