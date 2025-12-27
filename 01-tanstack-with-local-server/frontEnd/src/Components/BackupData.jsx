

import { useUserList } from '../Hooks/useUserList'

function BackupData() {

const {data:users} = useUserList()
   console.log("BacupData",users)
  return (
    <div>
        <h1>Backup Data</h1>
        <ul>

        {users? users.map((user)=>{
            return(
                <li key={user.id}>{user.name}</li>
            )
        }):""}
        </ul>
    </div>
  )
}

export default BackupData