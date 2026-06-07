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


</Routes>


</BrowserRouter>

);

}


export default App;