import React, {useEffect, useState} from "react";


const CarList = () => {
    const [Cars, setCars] = useState([]);

    useEffect(() => {
        fetch("/api/cars")
        .then(response => response.json())
        // .then(data => console.log(typeof data))
        // .then(data => setCars(data[0]["model"]))
        .then(data => setCars(data)) 
      },[])


    return ( 
        <ul>
            { Cars.length && Cars.map(m => <li key={m.id}>{m.id} - {m.model} - {m.production_date}</li>)}
        </ul>
        
     );
}

export default CarList;