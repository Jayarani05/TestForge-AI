const Input = ({
    label,
    type="text",
    value,
    onChange,
    placeholder
}) => {


    return (

        <div className="flex flex-col gap-2">


            <label className="text-sm text-gray-300">

                {label}

            </label>


            <input

                type={type}

                value={value}

                onChange={onChange}

                placeholder={placeholder}


                className="
                bg-gray-900
                border
                border-gray-700
                rounded-lg
                px-4
                py-3
                text-white
                outline-none
                focus:border-blue-500
                "

            />


        </div>

    );

};


export default Input;