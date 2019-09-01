import React from 'react'

import Tutor from '../components/Tutor'

class Tutors extends React.Component{
    constructor(){
        super()
        this.state = {
           tutor : [] 
        }
    }

    async componentDidMount() {
        try {
          const res = await fetch('http://127.0.0.1:8000/api/tutor/'); // fetch the data drf api
          const tutor = await res.json();
          this.setState({
            tutor
          });
        } catch (e) {
          console.log(e);
        }
      }
    
      render() {

        const tutorComponent = this.state.tutor.map(tutor => (<Tutor key={tutor.id} 
                                                                     firstName={tutor.first_name}
                                                                     lastName={tutor.last_name}
                                                                     email={tutor.email}
                                                                     specialization={tutor.specialization}
                                                                     createdOn={tutor.created_on}
                                                                />)
                                                                )

        return (
          <div>
           {tutorComponent}
          </div>
        );
      }
    

    
}
   


export default Tutors