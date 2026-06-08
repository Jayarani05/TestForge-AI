import {

    Bell,
    Search,
    User

} from "lucide-react";




function Header(){



    return (


        <div
        className="
        h-16
        bg-white
        border-b
        border-gray-200
        flex
        items-center
        justify-between
        px-6
        "
        >



            <div
            className="
            flex
            items-center
            bg-gray-100
            px-4
            py-2
            rounded-lg
            w-96
            "
            >


                <Search size={18}/>


                <input

                placeholder="Search projects, tests, bugs..."

                className="
                bg-transparent
                outline-none
                ml-3
                w-full
                "

                />


            </div>






            <div
            className="
            flex
            items-center
            gap-5
            "
            >


                <Bell size={20}/>



                <div
                className="
                flex
                items-center
                gap-2
                "
                >

                    <User size={20}/>

                    <div>

                        <p className="text-sm font-medium">

                            Jayarani

                        </p>

                        <p className="text-xs text-gray-500">

                            QA Engineer

                        </p>


                    </div>


                </div>


            </div>


        </div>


    );


}



export default Header;