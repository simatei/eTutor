import React from 'react'

function Tutor(props){
    return(
        <div>
            <p> firstName={props.firstName}</p>
            <p> lastName={props.lastName}</p>
            <p> Email={props.email}</p>
            <p> specialization={props.specialization}</p>
            <p> created on={props.createdOn}</p>
        </div>
    )
}

export default Tutor