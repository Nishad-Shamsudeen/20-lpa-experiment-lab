import React from 'react'
import { useUserList } from '../Hooks/useUserList'

function ListUsers() {
  
const {data,error,} = useUserList()

if(error){
    console.log("data fetched failed");
}
  return (
    <div>
        <h1>ListUsers</h1>  
        <ul>
        {data? data.map((user)=>{
            return(
                <li key={user.id}>{user.name}</li>
            )
        }):""}
        </ul>  
    </div>
  )
}

export default ListUsers