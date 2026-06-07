import {

createContext,
useContext,
useState,
useEffect

} from "react";


import api from "../api/axios";



const AuthContext =
createContext();



export function AuthProvider({children}){


const [user,setUser]=useState(null);


const [loading,setLoading]=useState(true);



const login = async(

email,

password

)=>{


const response =
await api.post(

"/auth/login",

{
email,
password
}

);



localStorage.setItem(

"token",

response.data.access_token

);



await loadUser();


return response.data;

};




const register = async(data)=>{


return await api.post(

"/auth/register",

data

);

};




const loadUser = async()=>{


try{


const response =
await api.get(

"/auth/me"

);


setUser(response.data);


}

catch(error){


localStorage.removeItem(
"token"
);


setUser(null);


}


setLoading(false);


};





const logout=()=>{


localStorage.removeItem(
"token"
);


setUser(null);


};





useEffect(()=>{


loadUser();


},[]);





return (

<AuthContext.Provider

value={{

user,

login,

register,

logout,

loading

}}

>


{children}


</AuthContext.Provider>


);


}





export function useAuth(){


return useContext(
AuthContext
);


}