import React, {useEffect, useState} from "react";
import { useParams } from "react-router-dom";

const CarDetail = () => {
    const [Car, setCar] = useState();
    const {id} = useParams();

    useEffect(() => {
        fetch(`/api/cars/${id}`)
        .then(response => response.json())
        .then(data => setCar(data));

    }, [id]);

    return ( 
        <div>
            
            {(typeof Car === 'undefined')? (
                <p>Loading ... </p>
            ):
            (
                Car.model
            )}
        </div>

    );
}
 
export default CarDetail;