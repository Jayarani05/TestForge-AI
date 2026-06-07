import {

BrowserRouter,

Routes,

Route

} from "react-router-dom";



import Login from "./pages/Login";

import Register from "./pages/Register";

import Dashboard from "./pages/Dashboard";

import Projects from "./pages/Projects";

import ProtectedRoute from "./routes/ProtectedRoute";




function App(){


return (

<BrowserRouter>


<Routes>


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


</Routes>


</BrowserRouter>

);

}


export default App;