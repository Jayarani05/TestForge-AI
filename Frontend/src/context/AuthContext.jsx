import {

    createContext,
    useContext,
    useState,
    useEffect

} from "react";


import api from "../api/axios";



const AuthContext = createContext();





export const AuthProvider = ({children})=>{



const [user,setUser] = useState(null);


const [loading,setLoading] = useState(true);







useEffect(()=>{


    checkAuth();


},[]);








const checkAuth = async()=>{



const token = localStorage.getItem("token");



if(!token){


    setLoading(false);


    return;


}





try{


const response = await api.get(

    "/auth/me"

);



setUser(

    response.data

);



}


catch(error){



localStorage.removeItem(

    "token"

);



setUser(null);



}




setLoading(false);



};









const login = async(

    email,

    password

)=>{



const response = await api.post(

    "/auth/login",

    {

        email,

        password

    }

);





const token =

response.data.access_token;






localStorage.setItem(

    "token",

    token

);





await checkAuth();



};










const logout = ()=>{



localStorage.removeItem(

    "token"

);



setUser(null);



window.location.href="/login";



};









return(


<AuthContext.Provider

value={{

    user,

    loading,

    login,

    logout

}}

>


{children}


</AuthContext.Provider>


);



};








export const useAuth=()=>{


return useContext(

    AuthContext

);


};