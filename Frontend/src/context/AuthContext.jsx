import {

    createContext,

    useContext,

    useState

} from "react";


import api from "../api/axios";



const AuthContext = createContext();



export const AuthProvider = (

    {children}

)=>{


    const [user,setUser] =
        useState(null);



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





    const loadUser = async()=>{


        try{


            const response =

                await api.get(

                    "/auth/me"

                );



            setUser(
                response.data
            );

        }

        catch(error){


            setUser(null);

        }


    };





    const logout = ()=>{


        localStorage.removeItem(
            "token"
        );


        setUser(null);

    };





    return (


        <AuthContext.Provider


            value={{

                user,

                login,

                logout,

                loadUser

            }}

        >


            {children}


        </AuthContext.Provider>

    );

};





export const useAuth = ()=>{

    return useContext(
        AuthContext
    );

};